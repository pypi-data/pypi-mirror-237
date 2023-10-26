# Copyright 2022 Zurich Instruments AG
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

import abc
import itertools
import logging
import warnings
from typing import TYPE_CHECKING, Callable, Dict, Iterator, List, Optional, Tuple, Union

import jsonschema

import laboneq.core.path as qct_path
from laboneq.core.exceptions import LabOneQException
from laboneq.core.types.enums import ReferenceClockSource
from laboneq.dsl.device import Instrument
from laboneq.dsl.device.connection import Connection
from laboneq.dsl.device.instruments import (
    HDAWG,
    PQSC,
    SHFPPC,
    SHFQA,
    SHFQC,
    SHFSG,
    UHFQA,
    NonQC,
)
from laboneq.dsl.device.io_units import (
    LogicalSignal,
    PhysicalChannel,
    PhysicalChannelType,
)
from laboneq.dsl.device.logical_signal_group import LogicalSignalGroup
from laboneq.dsl.device.physical_channel_group import PhysicalChannelGroup
from laboneq.dsl.device.servers import DataServer
from laboneq.dsl.enums import IODirection, IOSignalType

if TYPE_CHECKING:
    from laboneq.dsl.quantum import QuantumElement


_logger = logging.getLogger(__name__)


# Terminal Symbols
T_HDAWG_DEVICE = "HDAWG"
T_UHFQA_DEVICE = "UHFQA"
T_SHFQA_DEVICE = "SHFQA"
T_SHFSG_DEVICE = "SHFSG"
T_SHFQC_DEVICE = "SHFQC"
T_SHFPPC_DEVICE = "SHFPPC"
T_PQSC_DEVICE = "PQSC"
T_ALL_DEVICE_TYPES = [
    T_HDAWG_DEVICE,
    T_UHFQA_DEVICE,
    T_SHFQA_DEVICE,
    T_SHFSG_DEVICE,
    T_SHFQC_DEVICE,
    T_SHFPPC_DEVICE,
    T_PQSC_DEVICE,
]
T_UID = "uid"
T_ADDRESS = "address"
T_OPTIONS = "options"
T_INTERFACE = "interface"
T_IQ_SIGNAL = "iq_signal"
T_ACQUIRE_SIGNAL = "acquire_signal"
T_RF_SIGNAL = "rf_signal"
T_TO = "to"
T_EXTCLK = "external_clock_signal"
T_INTCLK = "internal_clock_signal"
T_PORT = "port"
T_PORTS = "ports"


# Models 'instruments' (former 'instrument_list') part of the descriptor:
#     instruments:
#       HDAWG:
#       - address: DEV8001
#         uid: device_hdawg
#         options: HDAWG8/CNT/ME/MF
#       SHFQA:
#       - address: DEV12001
#         uid: device_shfqa
#         options: SHFQA2
#       PQSC:
#       - address: DEV10001
#         uid: device_pqsc
InstrumentsType = Dict[str, List[Dict[str, str]]]

# Models 'connections' part of the descriptor:
#     connections:
#       device_hdawg:
#         - iq_signal: q0/drive_line
#           ports: [SIGOUTS/0, SIGOUTS/1]
#         - to: device_uhfqa
#           port: DIOS/0
#       device_uhfqa:
#         - iq_signal: q0/measure_line
#           ports: [SIGOUTS/0, SIGOUTS/1]
#         - acquire_signal: q0/acquire_line
#       device_pqsc:
#         - to: device_hdawg
#           port: ZSYNCS/0
ConnectionsType = Dict[str, List[Dict[str, Union[str, List[str]]]]]

# Models 'dataservers' part of the descriptor:
#     dataservers:
#       zi_server:
#         host: 127.0.0.1
#         port: 8004
#         instruments: [device_hdawg, device_uhfqa, device_pqsc]
DataServersType = Dict[str, Dict[str, Union[str, List[str]]]]


def _iterate_over_descriptors_of_type(instruments: InstrumentsType, device_type: str):
    for descriptor in instruments.get(device_type, []):
        yield (
            descriptor[T_UID],
            descriptor[T_ADDRESS],
            descriptor.get(T_INTERFACE),
            descriptor.get(T_OPTIONS),
        )


def _skip_nones(**kwargs):
    return {k: v for k, v in kwargs.items() if v is not None}


class _ProcessorBase(abc.ABC):
    @classmethod
    def process(
        cls,
        instruments: InstrumentsType,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates: List[Dict],
        physical_signals: Dict[str, PhysicalChannel],
    ) -> Iterator[Instrument]:
        ...


class _HDAWGProcessor(_ProcessorBase):
    @classmethod
    def process(
        cls,
        instruments: InstrumentsType,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates,
        physical_signals,
    ) -> Iterator[Instrument]:
        for uid, address, interface, options in _iterate_over_descriptors_of_type(
            instruments, T_HDAWG_DEVICE
        ):
            yield cls.make_device(
                uid,
                address,
                interface,
                options,
                connections,
                server_finder,
                logical_signals_candidates,
                physical_signals,
            )

    @staticmethod
    def make_device(
        uid,
        address,
        interface,
        options,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates,
        physical_signals,
    ) -> Instrument:
        device_connections = []
        external_clock_signal = None
        if uid in connections:
            signal_type_of_port = {}
            for port_desc in connections[uid]:
                signal_type_keyword, remote_path, local_ports = _port_decoder(
                    port_desc, [T_EXTCLK]
                )
                for local_port in local_ports:
                    if (
                        signal_type_of_port.setdefault(local_port, signal_type_keyword)
                        != signal_type_keyword
                    ):
                        raise LabOneQException(
                            f"Multiple signal types specified for {local_port}"
                        )
                if signal_type_keyword == T_EXTCLK:
                    external_clock_signal = ReferenceClockSource.EXTERNAL
                else:
                    physical_channel = _create_physical_channel(
                        local_ports, signal_type_keyword, uid, physical_signals
                    )
                    _logger.debug(
                        "%s Creating port remote_path=%s local_port=%s from %s",
                        uid,
                        remote_path,
                        local_ports,
                        port_desc,
                    )
                    if signal_type_keyword == T_IQ_SIGNAL:
                        if len(local_ports) != 2:
                            raise LabOneQException(
                                f"IQ signal connection for {uid} requires two local ports, where the first is the I channel and the second is the Q channel."
                            )
                        for i, local_port in enumerate(local_ports):
                            device_connections.append(
                                Connection(
                                    local_port=local_port,
                                    remote_path=remote_path,
                                    remote_port=str(i),
                                    signal_type=[IOSignalType.I, IOSignalType.Q][i],
                                )
                            )

                    else:
                        signal_type = (
                            IOSignalType.RF
                            if signal_type_keyword == T_RF_SIGNAL
                            else IOSignalType.DIO
                        )
                        if len(local_ports) != 1:
                            raise LabOneQException(
                                f"Connection with signal type {signal_type.value} for {uid} requires exactly one local port."
                            )
                        device_connections.append(
                            Connection(
                                local_port=local_ports[0],
                                remote_path=remote_path,
                                remote_port="0",
                                signal_type=signal_type,
                            )
                        )

                    ls_candidate = _path_to_signal(remote_path)

                    if ls_candidate is not None:
                        logical_signals_candidates.append(
                            {
                                "lsg_uid": ls_candidate[0],
                                "signal_id": ls_candidate[1],
                                "dir": IODirection.OUT,
                                "physical_channel": physical_channel,
                            }
                        )

        return HDAWG(
            **_skip_nones(
                server_uid=server_finder(uid),
                uid=uid,
                address=address,
                interface=interface,
                device_options=options,
                connections=device_connections,
                reference_clock_source=external_clock_signal,
            )
        )


class _UHFQAProcessor(_ProcessorBase):
    @classmethod
    def process(
        cls,
        instruments: InstrumentsType,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates,
        physical_signals,
    ) -> Iterator[Instrument]:
        for uid, address, interface, options in _iterate_over_descriptors_of_type(
            instruments, T_UHFQA_DEVICE
        ):
            yield cls.make_device(
                uid,
                address,
                interface,
                options,
                connections,
                server_finder,
                logical_signals_candidates,
                physical_signals,
            )

    @staticmethod
    def make_device(
        uid,
        address,
        interface,
        options,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates,
        physical_signals,
    ) -> Instrument:
        device_connections = []
        external_clock_signal = None
        if uid in connections:
            signal_type_of_port = {}
            for port_desc in connections[uid]:
                signal_type_keyword, remote_path, local_ports = _port_decoder(
                    port_desc, [T_EXTCLK]
                )
                for local_port in local_ports:
                    if (
                        signal_type_of_port.setdefault(local_port, signal_type_keyword)
                        != signal_type_keyword
                    ):
                        raise LabOneQException(
                            f"Multiple signal types specified for {local_port}"
                        )
                if signal_type_keyword == T_EXTCLK:
                    external_clock_signal = ReferenceClockSource.EXTERNAL
                else:
                    _UHFQAProcessor._validate_local_ports(local_ports)
                    is_output = True
                    if signal_type_keyword == T_ACQUIRE_SIGNAL:
                        is_output = False
                        if len(local_ports) > 0:
                            raise LabOneQException(
                                f"Specifying ports in {uid} {T_ACQUIRE_SIGNAL} {remote_path} is not allowed, but found {local_ports}"
                            )
                        local_ports = ["QAS/0", "QAS/1"]
                    physical_channel = _create_physical_channel(
                        local_ports, signal_type_keyword, uid, physical_signals
                    )
                    ls_candidate = _path_to_signal(remote_path)
                    if ls_candidate is not None:
                        logical_signals_candidates.append(
                            {
                                "lsg_uid": ls_candidate[0],
                                "signal_id": ls_candidate[1],
                                "dir": IODirection.OUT if is_output else IODirection.IN,
                                "physical_channel": physical_channel,
                            }
                        )

                    _logger.debug(
                        "%s Creating port remote_path=%s local_ports=%s from description: %s",
                        uid,
                        remote_path,
                        local_ports,
                        port_desc,
                    )

                    if signal_type_keyword == T_ACQUIRE_SIGNAL:
                        for i, local_port in enumerate(local_ports):
                            device_connections.append(
                                Connection(
                                    local_port=local_port,
                                    remote_path=remote_path,
                                    remote_port=str(i),
                                    signal_type=IOSignalType.IQ,
                                    direction=IODirection.IN,
                                )
                            )
                    elif signal_type_keyword == T_IQ_SIGNAL:
                        if len(local_ports) != 2:
                            raise LabOneQException(
                                f"IQ signal connection for {uid} requires two local ports defined, where the first is the I channel and the second is the Q channel."
                            )
                        for i, local_port in enumerate(local_ports):
                            device_connections.append(
                                Connection(
                                    local_port=local_port,
                                    remote_path=remote_path,
                                    remote_port=str(i),
                                    signal_type=[IOSignalType.I, IOSignalType.Q][i],
                                )
                            )
                    elif signal_type_keyword == T_RF_SIGNAL:
                        raise LabOneQException(f"RF signal not supported on {uid}.")

        return UHFQA(
            **_skip_nones(
                server_uid=server_finder(uid),
                uid=uid,
                address=address,
                interface=interface,
                device_options=options,
                connections=device_connections,
                reference_clock_source=external_clock_signal,
            )
        )

    @staticmethod
    def _validate_local_ports(local_ports):
        dummy_device = UHFQA()
        available_ports = [port.uid for port in dummy_device.ports]
        for local_port in local_ports:
            if local_port not in available_ports:
                raise LabOneQException(
                    f"Device {T_UHFQA_DEVICE} has no port with uid {local_port}. Available port uids are: {available_ports}."
                )


class _SHFQAProcessor(_ProcessorBase):
    @classmethod
    def process(
        cls,
        instruments: InstrumentsType,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates,
        physical_signals,
    ) -> Iterator[Instrument]:
        for uid, address, interface, options in _iterate_over_descriptors_of_type(
            instruments, T_SHFQA_DEVICE
        ):
            yield cls.make_device(
                uid,
                address,
                interface,
                options,
                connections,
                server_finder,
                logical_signals_candidates,
                physical_signals,
            )

    @staticmethod
    def make_device(
        uid,
        address,
        interface,
        options,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates,
        physical_signals,
        is_qc: bool = False,
    ) -> Instrument:
        device_connections = []
        external_clock_signal = None
        if uid in connections:
            signal_type_of_port = {}
            for port_desc in connections[uid]:
                signal_type_keyword, remote_path, local_ports = _port_decoder(
                    port_desc, [T_EXTCLK]
                )
                physical_channel = _create_physical_channel(
                    local_ports, signal_type_keyword, uid, physical_signals
                )
                for local_port in local_ports:
                    if (
                        signal_type_of_port.setdefault(local_port, signal_type_keyword)
                        != signal_type_keyword
                    ):
                        raise LabOneQException(
                            f"Multiple signal types specified for {local_port}"
                        )

                if signal_type_keyword == T_EXTCLK:
                    external_clock_signal = ReferenceClockSource.EXTERNAL
                    continue
                if (
                    is_qc
                    and len(local_ports) == 1
                    and local_ports[0].upper().startswith("SGCHANNELS/")
                ):
                    continue  # Skip over SG ports for QA part of QC
                _SHFQAProcessor._validate_local_ports(local_ports, remote_path)
                ls_candidate = _path_to_signal(remote_path)
                is_output = signal_type_keyword != T_ACQUIRE_SIGNAL

                if ls_candidate is not None:
                    logical_signals_candidates.append(
                        {
                            "lsg_uid": ls_candidate[0],
                            "signal_id": ls_candidate[1],
                            "dir": IODirection.OUT if is_output else IODirection.IN,
                            "physical_channel": physical_channel,
                        }
                    )

                _logger.debug(
                    "%s Creating port remote_path=%s local_port=%s from description: %s",
                    uid,
                    remote_path,
                    local_ports,
                    port_desc,
                )

                if signal_type_keyword == T_ACQUIRE_SIGNAL:
                    for i, local_port in enumerate(local_ports):
                        device_connections.append(
                            Connection(
                                local_port=local_port,
                                remote_path=remote_path,
                                remote_port=str(i),
                                signal_type=IOSignalType.IQ,
                                direction=IODirection.IN,
                            )
                        )
                elif signal_type_keyword == T_IQ_SIGNAL:
                    for i, local_port in enumerate(local_ports):
                        device_connections.append(
                            Connection(
                                local_port=local_port,
                                remote_path=remote_path,
                                remote_port=str(i),
                                signal_type=IOSignalType.IQ,
                            )
                        )
                elif signal_type_keyword == T_RF_SIGNAL:
                    raise LabOneQException(f"RF signal not supported on {uid}.")

        if len(device_connections) == 0:
            return None

        return SHFQA(
            **_skip_nones(
                server_uid=server_finder(uid),
                uid=uid,
                address=address,
                interface=interface,
                device_options=options,
                connections=device_connections,
                reference_clock_source=external_clock_signal,
            )
        )

    @staticmethod
    def _validate_local_ports(local_ports: List[str], remote_path):
        if len(local_ports) != 1:
            raise LabOneQException(
                f"{T_SHFQA_DEVICE} signals require exactly one port, but got {local_ports} for {remote_path}"
            )
        dummy_device = SHFQA()
        available_ports = [port.uid for port in dummy_device.ports]
        for local_port in local_ports:
            if local_port not in available_ports:
                raise LabOneQException(
                    f"Device {T_SHFQA_DEVICE} has no port with uid {local_port}. Available port uids are: {available_ports}.",
                    _logger,
                )


class _SHFSGProcessor(_ProcessorBase):
    @classmethod
    def process(
        cls,
        instruments: InstrumentsType,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates,
        physical_signals,
    ) -> Iterator[Instrument]:
        for uid, address, interface, options in _iterate_over_descriptors_of_type(
            instruments, T_SHFSG_DEVICE
        ):
            yield cls.make_device(
                uid,
                address,
                interface,
                options,
                connections,
                server_finder,
                logical_signals_candidates,
                physical_signals,
            )

    @staticmethod
    def make_device(
        uid,
        address,
        interface,
        options,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates,
        physical_signals,
        is_qc: bool = False,
    ) -> Instrument:
        device_connections = []
        used_ports = set()
        external_clock_signal = None
        if uid in connections:
            signal_type_of_port = {}
            for port_desc in connections[uid]:
                signal_type_keyword, remote_path, local_ports = _port_decoder(
                    port_desc, [T_EXTCLK]
                )
                physical_channel = _create_physical_channel(
                    local_ports, signal_type_keyword, uid, physical_signals
                )
                for local_port in local_ports:
                    if (
                        signal_type_of_port.setdefault(local_port, signal_type_keyword)
                        != signal_type_keyword
                    ):
                        raise LabOneQException(
                            f"Multiple signal types specified for {local_port}"
                        )
                if signal_type_keyword == T_EXTCLK:
                    external_clock_signal = ReferenceClockSource.EXTERNAL
                elif (
                    is_qc
                    and len(local_ports) == 1
                    and local_ports[0].upper().startswith("QACHANNELS/")
                ):
                    continue  # Skip over QA ports for SG part of QC
                else:
                    _SHFSGProcessor._validate_local_ports(local_ports, remote_path)
                    for port in local_ports:
                        used_ports.add(port)
                    ls_candidate = _path_to_signal(remote_path)

                    if ls_candidate is not None:
                        logical_signals_candidates.append(
                            {
                                "lsg_uid": ls_candidate[0],
                                "signal_id": ls_candidate[1],
                                "dir": IODirection.OUT,
                                "physical_channel": physical_channel,
                            }
                        )

                    _logger.debug(
                        "%s Creating port remote_path=%s local_port=%s from description: %s",
                        uid,
                        remote_path,
                        local_ports,
                        port_desc,
                    )

                    if signal_type_keyword == T_IQ_SIGNAL:
                        for i, local_port in enumerate(local_ports):
                            device_connections.append(
                                Connection(
                                    local_port=local_port,
                                    remote_path=remote_path,
                                    remote_port=str(i),
                                    signal_type=IOSignalType.IQ,
                                )
                            )
                    elif signal_type_keyword == T_RF_SIGNAL:
                        raise LabOneQException(f"RF signal not supported on {uid}.")

        if len(device_connections) == 0:
            return None

        return SHFSG(
            **_skip_nones(
                server_uid=server_finder(uid),
                uid=uid,
                address=address,
                interface=interface,
                device_options=options,
                connections=device_connections,
                reference_clock_source=external_clock_signal,
            )
        )

    @staticmethod
    def _validate_local_ports(local_ports: List[str], remote_path):
        if len(local_ports) != 1:
            raise LabOneQException(
                f"SHFSG signals require exactly one port, but got {local_ports} for {remote_path}"
            )
        dummy_device = SHFSG()
        available_ports = [port.uid for port in dummy_device.ports]
        for local_port in local_ports:
            if local_port not in available_ports:
                raise LabOneQException(
                    f"Device {T_SHFSG_DEVICE} has no port with uid {local_port}. Available port uids are: {available_ports}.",
                    _logger,
                )


class _SHFQCProcessor(_ProcessorBase):
    @classmethod
    def process(
        cls,
        instruments: InstrumentsType,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates,
        physical_signals,
    ) -> Iterator[Instrument]:
        for uid, address, interface, options in _iterate_over_descriptors_of_type(
            instruments, T_SHFQC_DEVICE
        ):
            maybe_sg = _SHFSGProcessor.make_device(
                uid,
                address,
                interface,
                options,
                connections,
                server_finder,
                logical_signals_candidates,
                physical_signals,
                is_qc=True,
            )
            maybe_qa = _SHFQAProcessor.make_device(
                uid,
                address,
                interface,
                options,
                connections,
                server_finder,
                logical_signals_candidates,
                physical_signals,
                is_qc=True,
            )
            conns = []
            if maybe_qa is not None and maybe_qa.connections is not None:
                conns += maybe_qa.connections
            if maybe_sg is not None and maybe_sg.connections is not None:
                conns += maybe_sg.connections
            ref_clk_src = (
                ReferenceClockSource.EXTERNAL if T_EXTCLK in connections[uid] else None
            )
            yield SHFQC(
                **_skip_nones(
                    uid=uid,
                    interface=interface,
                    server_uid=server_finder(uid),
                    address=address,
                    reference_clock_source=ref_clk_src,
                    connections=conns,
                    device_options=options,
                )
            )


class _SHFPPCProcessor(_ProcessorBase):
    @classmethod
    def process(
        cls,
        instruments: InstrumentsType,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates,
        physical_signals,
    ) -> Iterator[Instrument]:
        for uid, address, interface, options in _iterate_over_descriptors_of_type(
            instruments, T_SHFPPC_DEVICE
        ):
            yield cls.make_device(
                uid,
                address,
                interface,
                options,
                connections,
                server_finder,
                logical_signals_candidates,
                physical_signals,
            )

    @staticmethod
    def make_device(
        uid,
        address,
        interface,
        options,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates,
        physical_signals,
    ) -> Instrument:
        device_connections = []
        external_clock_signal = None
        if uid in connections:
            for port_desc in connections[uid]:
                signal_type_keyword, remote_path, local_ports = _port_decoder(
                    port_desc, [T_EXTCLK], to_ls=True
                )

                if signal_type_keyword == T_EXTCLK:
                    external_clock_signal = ReferenceClockSource.EXTERNAL
                    continue
                _SHFPPCProcessor._validate_local_ports(local_ports, remote_path)
                device_connections.append(
                    Connection(
                        local_port=local_ports[0],
                        remote_path=remote_path,
                        remote_port=None,
                        signal_type=IOSignalType.PPC,
                    )
                )

        return SHFPPC(
            **_skip_nones(
                server_uid=server_finder(uid),
                uid=uid,
                address=address,
                interface=interface,
                device_options=options,
                connections=device_connections,
                reference_clock_source=external_clock_signal,
            )
        )

    @staticmethod
    def _validate_local_ports(local_ports: List[str], remote_path):
        if len(local_ports) != 1:
            raise LabOneQException(
                f"{T_SHFPPC_DEVICE} signals require exactly one port, but got {local_ports} for {remote_path}"
            )
        dummy_device = SHFPPC()
        available_ports = [port.uid for port in dummy_device.ports]
        for local_port in local_ports:
            if local_port not in available_ports:
                raise LabOneQException(
                    f"Device {T_SHFPPC_DEVICE} has no port with uid {local_port}. Available port uids are: {available_ports}.",
                    _logger,
                )


class _PQSCProcessor:
    @classmethod
    def process(
        cls,
        instruments: InstrumentsType,
        out_instrument_list,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates,
        physical_signals,
    ):
        for uid, address, interface, options in _iterate_over_descriptors_of_type(
            instruments, T_PQSC_DEVICE
        ):
            dev = cls.make_device(
                uid,
                address,
                interface,
                options,
                connections,
                server_finder,
                logical_signals_candidates,
                physical_signals,
            )
            dev.connections
            yield dev

    @staticmethod
    def make_device(
        uid,
        address,
        interface,
        options,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates,
        physical_signals,
    ):
        internal_clock_signal = None
        device_connections = []
        for port_desc in connections.get(uid, []):
            signal_type_keyword, remote_path, local_ports = _port_decoder(
                port_desc, [T_INTCLK]
            )
            if signal_type_keyword == T_INTCLK:
                internal_clock_signal = ReferenceClockSource.INTERNAL
            else:
                device_connections.append(
                    Connection(
                        local_port=local_ports[0],
                        remote_path=remote_path,
                        remote_port="0",
                        signal_type=IOSignalType.ZSYNC,
                    )
                )

        return PQSC(
            **_skip_nones(
                server_uid=server_finder(uid),
                uid=uid,
                address=address,
                interface=interface,
                device_options=options,
                connections=device_connections,
                reference_clock_source=internal_clock_signal,
                reference_clock=10e6,
            )
        )


class _NonQCProcessor(_ProcessorBase):
    @classmethod
    def process(
        cls,
        instruments: InstrumentsType,
        connections: ConnectionsType,
        server_finder: Callable[[str], str],
        logical_signals_candidates,
        physical_signals,
    ) -> Iterator[Instrument]:
        for dev_type, devices in instruments.items():
            if dev_type not in T_ALL_DEVICE_TYPES:
                for descriptor in devices:
                    uid = descriptor[T_UID]
                    yield NonQC(
                        **_skip_nones(
                            server_uid=server_finder(uid),
                            uid=uid,
                            address=descriptor[T_ADDRESS],
                            interface=descriptor.get(T_INTERFACE),
                            dev_type=dev_type,
                        )
                    )


def _port_decoder(
    port_desc, additional_switch_keys=None, to_ls=False
) -> Tuple[str, str, List[str]]:
    if additional_switch_keys is None:
        additional_switch_keys = []
    if isinstance(port_desc, dict):
        port_desc = dict(port_desc)  # make a copy
    else:
        port_desc = {port_desc: None}

    port = port_desc.pop(T_PORT, None)
    ports = port_desc.pop(T_PORTS, None)
    if ports is not None and port is not None:
        raise LabOneQException(
            f"Both ports and port specified, but only one is allowed: {port_desc}"
        )
    if ports is None:
        if port is None:
            local_ports = []
        else:
            local_ports = [port]
    elif isinstance(ports, str):
        local_ports = [ports]
    else:
        local_ports = ports

    signal_keys = [T_IQ_SIGNAL, T_ACQUIRE_SIGNAL, T_RF_SIGNAL]
    trigger_keys = []
    (signal_keys if to_ls else trigger_keys).append(T_TO)
    path_keys = signal_keys + trigger_keys
    all_keys = path_keys + additional_switch_keys

    signal_type_keyword = None
    remote_path = None
    for key in all_keys:
        if key in port_desc:
            signal_type_keyword = key
            remote_path = port_desc.pop(key)
            break

    if signal_type_keyword is None:
        raise LabOneQException(
            "Missing signal type: Expected one of the following keywords: "
            + ", ".join(all_keys)
        )
    if signal_type_keyword in path_keys and not remote_path:
        raise LabOneQException(
            f"Missing path: specify '{signal_type_keyword}: <group>{qct_path.Separator}<line>'"
        )
    if signal_type_keyword in signal_keys:
        if len(remote_path.split(qct_path.Separator)) != 2:
            raise LabOneQException(
                f"Invalid path: specify '{signal_type_keyword}: <group>{qct_path.Separator}<line>'"
            )
        if not all(remote_path.split(qct_path.Separator)):
            raise LabOneQException(
                f"Invalid path: specify '{signal_type_keyword}: <group>{qct_path.Separator}<line>'"
            )
        remote_path = qct_path.Separator.join(
            ["", qct_path.LogicalSignalGroups_Path, remote_path]
        )

    if port_desc:
        raise LabOneQException(f"Unknown keyword found: {list(port_desc.keys())[0]}")

    return signal_type_keyword, remote_path, local_ports


def _path_to_signal(path):
    if qct_path.Separator in path:
        split_path = path.split(qct_path.Separator)
        if split_path[1] == qct_path.LogicalSignalGroups_Path:
            return split_path[2], split_path[3]
        else:
            return split_path[0], split_path[1]
    return None


def _create_physical_channel(
    ports: List[str], signal_type_token: str, device_id, physical_signals
) -> Optional[PhysicalChannel]:
    if signal_type_token in (T_IQ_SIGNAL, T_ACQUIRE_SIGNAL):
        channel_type = PhysicalChannelType.IQ_CHANNEL
    elif signal_type_token == T_RF_SIGNAL:
        channel_type = PhysicalChannelType.RF_CHANNEL
    else:
        return None

    split_ports = [port.split(qct_path.Separator) for port in ports]
    signal_name = "_".join(
        (
            group[0]
            for group in itertools.groupby([x for y in zip(*split_ports) for x in y])
        )
    ).lower()

    path = qct_path.Separator.join(
        [qct_path.PhysicalChannelGroups_Path_Abs, device_id, signal_name]
    )

    if device_id not in physical_signals:
        physical_signals[device_id] = []
    else:
        other_signal: PhysicalChannel = next(
            (ps for ps in physical_signals[device_id] if ps.path == path), None
        )
        if other_signal is not None:
            assert other_signal.name == signal_name
            return other_signal

    physical_channel = PhysicalChannel(
        uid=f"{device_id}/{signal_name}", name=signal_name, type=channel_type, path=path
    )
    physical_signals[device_id].append(physical_channel)
    return physical_channel


def make_qubits(
    qubit_descriptor: list[dict],
    logical_signal_groups: list[LogicalSignalGroup],
    types: dict[str, QuantumElement],
) -> dict[str, QuantumElement]:
    """Make qubits from their descriptor in Device Setup descriptor.

    Args:
        qubit_descriptor: `qubits` section the descriptor.
        logical_signal_groups: Logical signal groups.
        types: Mapping of types.
            Mapping keys are used to select the correct `QuantumElement` to make
            qubit `type`.

    Returns:
        Dictionary of `QuantumElements`, with their `uid` as key.
            The keys are sorted.

    Raises:
        LabOneQException: If the qubits are defined incorrectly.
    """
    if not isinstance(qubit_descriptor, list):
        msg = "Invalid 'qubits' definition: Must be a list of qubits."
        raise LabOneQException(msg)
    schema = {
        "type": "object",
        "properties": {
            "name": {
                "type": ["string", "array"],
                "items": {
                    "type": "string",
                },
                "uniqueItems": True,
            },
            "type": {"type": "string"},
        },
        "required": ["name", "type"],
        "additionalProperties": False,
    }
    qubits = {}
    for desc in qubit_descriptor:
        try:
            jsonschema.validate(desc, schema=schema)
        except jsonschema.exceptions.ValidationError as error:
            msg = error.message
            raise LabOneQException(f"Invalid 'qubit' definition: {msg}") from error
        q_type = desc["type"]
        try:
            quantum_element = types[q_type]
        except KeyError:
            msg = f"'type': '{q_type}' not one of {list(types.keys())}."
            raise LabOneQException(f"Invalid 'qubit' definition: {msg}")
        q_defs = desc["name"] if isinstance(desc["name"], list) else [desc["name"]]
        for q_def in q_defs:
            if q_def in qubits:
                msg = f"Qubit '{q_def}' has multiple definitions."
                raise LabOneQException(f"Invalid 'qubit' definition: {msg}")
            q_type = desc["type"]
            try:
                lsg = logical_signal_groups[q_def]
            except KeyError:
                msg = f"Qubit '{q_def}' has no connections."
                raise LabOneQException(f"Invalid 'qubit' definition: {msg}")
            qubits[q_def] = quantum_element.from_logical_signal_group(q_def, lsg=lsg)
    return {key: qubits[key] for key in sorted(qubits)}


class _DeviceSetupGenerator:
    @staticmethod
    def from_descriptor(
        yaml_text: str,
        server_host: str = None,
        server_port: str = None,
        setup_name: str = None,
    ):
        from yaml import load

        try:
            from yaml import CLoader as Loader
        except ImportError:
            from yaml import Loader

        setup_desc = load(yaml_text, Loader=Loader)

        return _DeviceSetupGenerator.from_dicts(
            instrument_list=setup_desc.get("instrument_list"),
            instruments=setup_desc.get("instruments"),
            connections=setup_desc.get("connections"),
            dataservers=setup_desc.get("dataservers"),
            qubits=setup_desc.get("qubits", []),
            server_host=server_host,
            server_port=server_port,
            setup_name=setup_desc.get("setup_name")
            if setup_name is None
            else setup_name,
        )

    @staticmethod
    def from_yaml(
        filepath,
        server_host: str = None,
        server_port: str = None,
        setup_name: str = None,
    ):
        from yaml import load

        try:
            from yaml import CLoader as Loader
        except ImportError:
            from yaml import Loader

        with open(filepath) as fp:
            setup_desc = load(fp, Loader=Loader)

        return _DeviceSetupGenerator.from_dicts(
            instrument_list=setup_desc.get("instrument_list"),
            instruments=setup_desc.get("instruments"),
            connections=setup_desc.get("connections"),
            dataservers=setup_desc.get("dataservers"),
            qubits=setup_desc.get("qubits", []),
            server_host=server_host,
            server_port=server_port,
            setup_name=setup_desc.get("setup_name")
            if setup_name is None
            else setup_name,
        )

    @staticmethod
    def from_dicts(
        instrument_list: InstrumentsType = None,
        instruments: InstrumentsType = None,
        connections: ConnectionsType = None,
        dataservers: DataServersType = None,
        qubits: list = [],
        server_host: str = None,
        server_port: str = None,
        setup_name: str = None,
    ):
        # To avoid circular imports
        from laboneq.dsl import quantum

        if instrument_list is not None:
            if instruments is None:
                warnings.warn(
                    "'instrument_list' section is deprecated in setup descriptor, use 'instruments' instead.",
                    FutureWarning,
                )
                instruments = instrument_list
            else:
                warnings.warn(
                    "Both 'instrument_list' and 'instruments' are present in the setup descriptor, deprecated 'instrument_list' ignored.",
                    FutureWarning,
                )

        if instruments is None:
            raise LabOneQException(
                "'instruments' section is mandatory in the setup descriptor."
            )

        # Check for unique device UIDs
        instrument_uids = []
        for instrument_info in instruments.values():
            for info in instrument_info:
                instrument_uids.append(info["uid"])
        if len(instrument_uids) > len(set(instrument_uids)):
            raise LabOneQException("Device setup instrument UIDs must be unique.")

        if connections is None:
            connections = {}
        if setup_name is None:
            setup_name = "unknown"

        if server_host is not None:
            if dataservers is not None:
                _logger.warning(
                    "Servers definition in the descriptor will be overridden by the server passed to the constructor."
                )
            dataservers = {
                "zi_server": {
                    "host": server_host,
                    "port": "8004" if server_port is None else server_port,
                }
            }

        if dataservers is None:
            raise LabOneQException(
                "At least one server must be defined either in the descriptor or in the constructor."
            )

        # Construct servers
        servers: List[Tuple[DataServer, List[str]]] = [
            (
                DataServer(
                    uid=server_uid,
                    host=server_def["host"],
                    port=server_def.get("port", 8004),
                    api_level=6,
                ),
                server_def.get("instruments", []),
            )
            for server_uid, server_def in dataservers.items()
        ]

        def server_finder(device_uid: str) -> str:
            default_data_server: DataServer = None
            explicit_data_server: DataServer = None
            for data_server, devices in servers:
                if default_data_server is None and len(devices) == 0:
                    default_data_server = data_server
                if device_uid in devices:
                    if explicit_data_server is not None:
                        raise LabOneQException(
                            f"Device '{device_uid}' assigned to multiple data servers: "
                            f"[{explicit_data_server.uid}, {data_server.uid}]."
                        )
                    explicit_data_server = data_server
            if explicit_data_server is not None:
                return explicit_data_server.uid
            if default_data_server is None:
                raise LabOneQException(
                    f"Couldn't determine the data server for the device '{device_uid}'."
                )
            return default_data_server.uid

        processors: List[_ProcessorBase] = [
            _HDAWGProcessor,
            _UHFQAProcessor,
            _SHFQAProcessor,
            _SHFSGProcessor,
            _SHFQCProcessor,
            _SHFPPCProcessor,
            _NonQCProcessor,
        ]

        # Define instruments
        out_instruments: List[Instrument] = []
        logical_signals_candidates = []
        physical_signals = {}  # device_uid -> PhysicalChannel
        for processor in processors:
            out_instruments += processor.process(
                instruments,
                connections,
                server_finder,
                logical_signals_candidates,
                physical_signals,
            )
        # PQSC processor needs to know about yielded instruments:
        out_instruments += _PQSCProcessor.process(
            instruments,
            out_instruments,
            connections,
            server_finder,
            logical_signals_candidates,
            physical_signals,
        )

        logical_signal_groups = {}

        logical_signal_group_uids = set(
            [ls["lsg_uid"] for ls in logical_signals_candidates]
        )
        for lsg_uid in logical_signal_group_uids:
            signals = {
                ls["signal_id"]: LogicalSignal(
                    uid=f"{lsg_uid}/{ls['signal_id']}",
                    name=ls["signal_id"],
                    direction=ls["dir"],
                    path=qct_path.Separator.join(
                        [
                            qct_path.LogicalSignalGroups_Path_Abs,
                            lsg_uid,
                            ls["signal_id"],
                        ]
                    ),
                    physical_channel=ls["physical_channel"],
                )
                for ls in logical_signals_candidates
                if ls["lsg_uid"] == lsg_uid
            }
            logical_signal_groups[lsg_uid] = LogicalSignalGroup(lsg_uid, signals)

        logical_signal_groups = dict(sorted(logical_signal_groups.items()))

        physical_channel_groups = {
            device: PhysicalChannelGroup(
                uid=device, channels={channel.name: channel for channel in channels}
            )
            for device, channels in physical_signals.items()
        }

        device_setup_constructor_args = {
            "uid": setup_name,
            "servers": {server.uid: server for server, _ in servers},
            "instruments": out_instruments,
            "qubits": make_qubits(
                qubits,
                logical_signal_groups,
                types={
                    "qubit": quantum.Qubit,
                    "transmon": quantum.Transmon,
                },
            ),
            "logical_signal_groups": logical_signal_groups,
            "physical_channel_groups": physical_channel_groups,
        }

        return device_setup_constructor_args
