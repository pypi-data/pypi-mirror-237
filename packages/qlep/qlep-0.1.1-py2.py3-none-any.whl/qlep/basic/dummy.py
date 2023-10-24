r"""
The module with the Dummy state quantum leader election protocol
"""
# lep core
import qlep.core
# numpy
import numpy as np
# qiskit
import qiskit
# override decorator
from typing_extensions import override


class DummyQLEP(qlep.core.QuantumLeaderElectionProtocol):
    r"""
    An example class for a dummy quantum leader election protocol
    """
    def __init__(
                self,
                no_nodes: int,
                no_elections: int = 1,
                quantum_data_provider: qlep.core.QuantumDataProvider = None,
                committee: qlep.core.Committee = None,
            ) -> None:
        super().__init__(
            election_type=qlep.core.ElectionType.DUMMY,
            no_nodes=no_nodes,
            no_elections=no_elections,
            quantum_data_provider=quantum_data_provider,
            committee=committee
        )

    @override
    def get_quantum_circuits(
            self,
            measure: bool = True
    ) -> list[qiskit.QuantumCircuit]:
        return [DummyStateGenerator.get_quantum_circuits(
                    no_nodes=self.quantum_no_nodes,
                    measure=measure
                )]

    @override
    def get_leader_election_algorithm(
            self
    ) -> qlep.core.LeaderElectionAlgorithm:
        return DummyLeaderElectionAlgorithm()

    @override
    def get_malicious_attacker(self) -> qlep.core.MaliciousAttacker:
        return DummyMaliciousAttacker()


class DummyStateGenerator:
    @staticmethod
    def get_quantum_circuits(
        no_nodes: int,
        measure: bool = True
    ) -> qiskit.QuantumCircuit:
        # the number of qubits
        no_qubits = no_nodes
        # the qubits register
        quantum_registers = qiskit.QuantumRegister(no_qubits, 'q')
        if measure:
            # the classic registers
            classic_registers = qiskit.ClassicalRegister(no_qubits, 'c')
            # the quantum circuit which use the qubits
            # and the classic bits registers
            quantum_circuit = qiskit.QuantumCircuit(quantum_registers,
                                                    classic_registers)
        else:
            quantum_circuit = qiskit.QuantumCircuit(quantum_registers)

        # create the superposition for the first two qubits
        quantum_circuit.h(quantum_registers[0])
        quantum_circuit.cx(quantum_registers[0], quantum_registers[1])
        quantum_circuit.x(quantum_registers[0])
        quantum_circuit.barrier()
        if measure:
            quantum_circuit.measure(quantum_registers, classic_registers)
        return quantum_circuit


class DummyLeaderElectionAlgorithm(qlep.core.LeaderElectionAlgorithm):
    def __init__(self) -> None:
        super().__init__()

    @override
    def elect(self, data: np.ndarray) -> int:
        match (data[0, 0, 0], data[0, 0, 1]):
            case (1, 0):
                return 0
            case (0, 1):
                return 1
            case _:
                return -1


class DummyMaliciousAttacker(qlep.core.MaliciousAttacker):
    def __init__(self) -> None:
        super().__init__()

    @override
    def attack(
        self,
        register_ids: np.ndarray,
        data: np.ndarray,
        malicious_ids: np.ndarray
    ) -> np.ndarray:
        # get the malicious nodes
        malicious_nodes = [x for x in register_ids if x in malicious_ids]
        # if no malicious nodes under our control than return the given data
        if not malicious_nodes:
            return data
        # init return data
        modified_data = np.copy(data)
        # verify if the first two nodes are malicious
        match (register_ids[0] in malicious_ids,
               register_ids[1] in malicious_ids):
            case (True, False):
                modified_data[0, 0, 0] = 1
            case (False, True):
                modified_data[0, 0, 1] = 1
            case (True, True):
                modified_data[0, 0, 0] = 1
                modified_data[0, 0, 1] = 0
            case _:
                pass
        return modified_data
