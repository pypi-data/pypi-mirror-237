# future annotations
from __future__ import annotations
# enumeration
from enum import IntEnum, auto
# typing
import typing
# numpy
import numpy as np
# matplolib for maker/line style
from matplotlib.lines import Line2D

# qiskit
import qiskit
# ibm login account
from qiskit_ibm_provider import IBMProvider
# aws login account
from qiskit_braket_provider import AWSBraketProvider
# Aer provider for simulation
from qiskit_aer import AerProvider
# fake provider v2
from qiskit.providers.fake_provider import FakeProviderForBackendV2
# fake provider v1
from qiskit.providers.fake_provider import FakeProvider
# aer simulator for emulation
from qiskit_aer import AerSimulator
# pqcee provider
from qiskit_pqcee_provider import PqceeProvider

__all__ = ["Provider", "QuantumDataProvider"]


class Provider(IntEnum):
    r"""The types of providers.
    """

    AWS = auto()
    r"""
    AWS provider.
    """
    IBM = auto()
    r"""
    IBM provider.
    """
    FAKEV1 = auto()
    r"""
    Fake provider v1 from qiskit.
    """
    FAKEV2 = auto()
    r"""
    Fake provider v2 from qiskit.
    """
    AER = auto()
    r"""
    Local Aer provider for simulation.
    """
    EMULATOR = auto()
    r"""
    Emulator provider using Local Aer provider for simulation.
    """
    PQCEE = auto()
    r"""
    pQCee blockchain provider
    """

    @classmethod
    def _missing_(cls, value: typing.Any) -> Provider:
        if type(value) is str:
            value = value.upper()
            if value in dir(cls):
                return cls[value]
        raise ValueError("%r is not a valid %s" % (value, cls.__name__))

    @staticmethod
    def get_options() -> list[str]:
        r"""
        Return a list of the possible providers in string format.

        Returns:
            providers
                Return a list of string with the names of providers

        Examples:
            >>> import lep.core
            >>> lep.core.Provider.get_options()
            ['AWS', 'IBM', 'FAKEV1', 'FAKEV2', 'AER', 'EMULATOR']
        """
        return list(map(lambda x: x.name, list(Provider)))

    """
    # maybe to implement
    def __init__(self):
        match self.name:
            case "AWS":
                self.provider = AWSBraketProvider()
            case "IBM":
                self.provider = IBMProvider()
            case "FAKEV1":
                self.provider = FakeProvider()
            case "FAKEV2":
                self.provider = FakeProviderForBackendV2()
            case "AER":
                self.provider = AerProvider()
            case "EMULATOR":
                self.provider = None
            case _:
                self.provider = None
    """

    def get_qiskit_provider(self) -> qiskit.providers.Provider:
        match self.name:
            case "AWS":
                return AWSBraketProvider()
            case "IBM":
                return IBMProvider()
            case "FAKEV1":
                return FakeProvider()
            case "FAKEV2":
                return FakeProviderForBackendV2()
            case "AER":
                return AerProvider()
            case "EMULATOR":
                return AerProvider()
            case "PQCEE":
                return PqceeProvider()
            case _:
                raise ValueError("The provider %s is not implemented" %
                                 self.name)

    def get_qiskit_backend(
            self,
            backend_name: str
    ) -> qiskit.providers.Backend:
        r"""
        Return the qiskit backend with the given name from
        the current provider.

        Args:
            backend_name :
                The name of the backend to get.

        Returns:
            qiskit_backend
                The qiskit backend with the given name.
        """
        provider: qiskit.providers.Provider = self.get_qiskit_provider()
        match self.name:
            case "FAKEV2":
                # a little modified get_backend function
                qiskit_backend = provider.backends()[0]
                if backend_name:
                    filtered_backends = [
                        fake_backend
                        for fake_backend in provider.backends()
                        if fake_backend.name == backend_name
                    ]
                    if not filtered_backends:
                        raise qiskit.providers.QiskitBackendNotFoundError()

                    qiskit_backend = filtered_backends[0]

                return qiskit_backend
            case "EMULATOR":
                # get provider and backend to emulate
                emulate_provider_name = backend_name.split("_", 1)[0]
                emulate_backend_name = backend_name.split("_", 1)[1]
                # get the provider to emulate
                emulate_provider = Provider(emulate_provider_name)
                # get the backend to emulate
                emulate_backend = emulate_provider.get_qiskit_backend(
                    backend_name=emulate_backend_name
                )
                # get the emulated backend
                qiskit_backend = AerSimulator.from_backend(
                    emulate_backend
                )
                qiskit_backend.emulate_name = backend_name
                return qiskit_backend
            case _:
                return provider.get_backend(backend_name)

    def get_backends_name(self) -> list[str]:
        r"""
        Return a list with the names of the backends of the current provider.

        Returns:
            backends_name
                The list with the names of the backends of the current
                provider.
        """
        provider: qiskit.providers.Provider = self.get_qiskit_provider()
        match self.name:
            case "AER" | "FAKEV1":
                return [backend.name() for backend in provider.backends()]
            case "EMULATOR":
                return list("PROVIDER_BACKEND")
            case _:
                return [backend.name for backend in provider.backends()]

    def is_local(self) -> bool:
        r"""
        Return True if the provider is local.

        Returns:
            is_local
                True if the provider is local.
        """
        match self.name:
            case "AER" | "FAKEV1" | "FAKEV2" | "EMULATOR" | "PQCEE":
                return True
            case _:
                return False

    def is_simulator(
            self,
            backend_name: str
    ) -> bool:
        r"""
        Return True if the backend is a simulator.

        Args:
            backend_name :
                The name of the backend to get.

        Returns:
            is_simulator
                True if the backend is a simulator.
        """
        if self.is_local():
            return True

        provider: qiskit.providers.Provider = self.get_qiskit_provider()
        match self.name:
            case "AWS":
                return [backend.name
                        for backend in provider.backends(types=["SIMULATOR"])
                        ].count(backend_name) > 0
            case "IBM":
                return [backend.name
                        for backend in provider.backends(simulator=True)
                        ].count(backend_name) > 0
            case _:
                raise ValueError("The provider %s is not implemented" %
                                 self.name)

    def get_marker_fill_style(self) -> str:
        r"""
        Return the marker fill style depending on the provider.

        Returns:
            marker_fill_style
                The marker fill style depending on the provider.
        """
        fill_styles: list[str] = Line2D.fillStyles
        providers: list[str] = list(Provider)
        fill_styles_dict = dict(zip(providers, fill_styles))
        return fill_styles_dict[self]


class QuantumDataProvider():
    r"""
    The provider of quantum data.
    """
    provider: Provider = None
    r"""
    The provider of the quantum data.
    """
    backend_name: str = None
    r"""
    The name of the backend
    """
    stake_state: np.random.RandomState = None
    r"""
    The stake random state
    """
    def __init__(
            self,
            provider: Provider,
            backend_name: str,
            stake_seed: int = 0
    ) -> None:
        r"""
        Initialize the quantum data provider.

        Args:
            provider :
                The provider of the quantum data.
            backend_name :
                The name of the backend to get.
            stake_seed :
                The seed for the stake runs
        """
        self.provider: Provider = provider
        self.backend_name: str = backend_name
        self.stake_state = np.random.RandomState(
            np.random.MT19937(
                np.random.SeedSequence(stake_seed)
            )
        )

    def _get_qiskit_backend(self) -> qiskit.providers.Backend:
        r"""
        Return the qiskit backend.

        Returns:
            qiskit_backend
                The qiskit backend.
        """
        return self.provider.get_qiskit_backend(backend_name=self.backend_name)

    def get_bakend_num_qubits(self) -> int:
        r"""
        Return the number of qubits of the qiskit backend.

        Returns:
            qiskit_backend_num_qubits
                The number of qubits of the qiskit backend.
        """
        qiskit_backend = self._get_qiskit_backend()
        match qiskit_backend.version:
            case 2:
                if self.provider is Provider.IBM:
                    return qiskit_backend.configuration().num_qubits
                return qiskit_backend.num_qubits
            case 1:
                return qiskit_backend.configuration().num_qubits
            case _:
                return -1

    def send_job(
            self,
            quantum_circuits: list[qiskit.QuantumCircuit],
            shots: int = 1,
            seed_simulator: int = 0
    ) -> qiskit.providers.JobV1:
        r"""
        Send the quantum circuits to the backend for execution.

        Args:
            quantum_circuits :
                The quantum circuits to execute.
            shots :
                The number of shots for the execution.
            seed_simulator :
                The random seed for simulators

        Returns:
            job
                The job for the execution of the quantum circuits.
        """
        if np.any([qc.num_qubits > self.get_bakend_num_qubits()
                   for qc in quantum_circuits]):
            raise ValueError(
                "The quantum circuit has more qubits than "
                "the backend %d > %d" % (
                    quantum_circuits[0].num_qubits,
                    self.get_bakend_num_qubits()
                )
            )
        qiskit_backend = self._get_qiskit_backend()
        if self.provider is Provider.IBM:
            tqc = qiskit.transpile(
                quantum_circuits,
                backend=qiskit_backend,
                optimization_level=0,
                seed_transpiler=0
            )
            return qiskit_backend.run(
                tqc,
                seed_simulator=seed_simulator,
                shots=shots,
                init_qubits=True
            )
        if self.provider is Provider.AWS:
            return qiskit_backend.run(
                quantum_circuits,
                shots=shots
            )
        if self.provider is Provider.PQCEE:
            return qiskit_backend.run(
                quantum_circuits,
                shots=shots
            )
        return qiskit.execute(
            quantum_circuits,
            backend=qiskit_backend,
            shots=shots,
            seed_simulator=seed_simulator,
            seed_transpiler=0
        )

    def get_job_result(
            self,
            job: qiskit.providers.JobV1 = None,
            job_id: str = None
    ) -> list[np.ndarray]:
        r"""
        Return the result of the job.

        Args:
            job :
                The job to get the result.

        Returns:
            quantum_data
                The result of the job.
        """
        if job_id is None:
            job_id = job.job_id()
        match self.provider:
            case Provider.IBM:
                job = self.provider.get_qiskit_provider().backend.retrieve_job(
                    job_id
                )
            case Provider.AWS:
                job = self._get_qiskit_backend().retrieve_job(
                    job_id
                )
            case _:
                job = job
        quantum_results = job.result().get_counts()
        if type(quantum_results) is not list:
            quantum_results = [quantum_results]
        quantum_data_list = []
        for quatum_result_dict in quantum_results:
            # shufle the results
            temp = np.zeros(0)
            for key in quatum_result_dict:
                # repeat the key how many times it appears
                # in the results dictionary
                temp = np.hstack(
                    (temp, np.repeat(key, quatum_result_dict[key]))
                )
            # shufle the results
            # the results are stacked
            # to get a memory results we repeat the results and shufle
            # reproductible results
            rs = np.random.RandomState(
                np.random.MT19937(
                    np.random.SeedSequence(0)
                )
            )
            rs.shuffle(temp)
            quantum_result = temp
            # flip from big endian to little endian
            quantum_result = list(map(lambda y: y[::-1], quantum_result))
            # transform in a numpy array of int with values 0 or 1
            quantum_data = np.array(
                list(map(lambda y: list(map(int, y)), quantum_result))
            )
            quantum_data_list.append(quantum_data)
        return quantum_data_list

    def run_job(
            self,
            quantum_circuits: list[qiskit.QuantumCircuit],
            shots: int = 1,
            seed_simulator: int = 0
    ) -> list[np.ndarray]:
        r"""
        Send the quantum circuits to the backend for execution and
        return the result.

        Args:
            quantum_circuits :
                The quantum circuits to execute.
            shots :
                The number of shots for the execution.
            seed_simulator :
                The random seed for simulators

        Returns:
            quantum_data
                The result of the job.
        """
        job = self.send_job(
            quantum_circuits=quantum_circuits,
            shots=shots,
            seed_simulator=seed_simulator
        )
        quantum_data = self.get_job_result(job=job)
        return quantum_data

    def run_stake(
        self,
        quantum_circuits: list[qiskit.QuantumCircuit]
    ) -> list[np.ndarray]:
        r"""

        """
        if self.is_local() is False:
            raise ValueError(
                "Only local providers for stake"
            )
        return self.run_job(
            quantum_circuits=quantum_circuits,
            shots=1,
            seed_simulator=self.stake_state.randint(low=0, high=65535)
        )

    def is_simulator(self) -> bool:
        r"""
        Return True if the backend is a simulator.

        Returns:
            is_simulator
                True if the backend is a simulator.
        """
        return self.provider.is_simulator(
            backend_name=self.backend_name
        )

    def is_local(self) -> bool:
        r"""
        Return True if the backend is a simulator.

        Returns:
            is_simulator
                True if the backend is a simulator.
        """
        return self.provider.is_local()

    def get_line_style(self) -> str:
        r"""
        Return the line style depending on the backend.
        - : for teoretical
        -- : for simulation
        : : for QPU

        Returns:
            line_style
                The line style depending on the backend.
        """
        return "--" if self.is_simulator() else ":"

    def get_name(self) -> str:
        r"""
        Return the name of the quantum data provider.

        Returns:
            name
                The name of the quantum data provider.
        """
        return self.provider.name + r'_' + self.backend_name

    def get_latex_name(self) -> str:
        r"""
        Return the latex name of the quantum data provider.

        Returns:
            latex_name
                The latex name of the quantum data provider.
        """
        return self.get_name()
