r"""
The module with the W state quantum leader election protocol.
"""
# logging
import logging
# lep base
import qlep.core
# numpy
import numpy as np
# qiskit
import qiskit
# typing
import typing
# override decorator
from typing_extensions import override


class WStateQLEP(qlep.core.QuantumLeaderElectionProtocol):
    r"""
    Quantum Leader Election Protocol with W state

    Note:
        The W state is generated using the method proposed in [2]_ [3]_.
        The election algorithm is the one proposed in [1]_. A more efficient
        circuit is proposed in [4]_.

    References:
        .. [1] D'Hondt, Ellie, and Prakash Panangaden. "Leader election and distributed consensus with quantum resources ArXiv Quantum Physics e-prints (2005).
        .. [2] Diker, Firat. "Deterministic construction of arbitrary $ W $ states with quadratically increasing number of two-qubit gates." arXiv preprint arXiv:1606.09290 (2016).
        .. [3] Ozaydin, Fatih, et al. "Fusing multiple W states simultaneously with a Fredkin gate." Physical Review A 89.4 (2014): 042311.
        .. [4] Sheng, YuBo, et al. "Efficient N-particle W state concentration with different parity check gates." Science China Physics, Mechanics & Astronomy 58 (2015): 1-11.
    """

    use_history: bool = False
    r"""
    The flag to use the history of the quantum leader election protocol.
    Default value is False. If True, the malicious attacker will use
    the history of the elections to not create more than the tolerance
    given conflicts with the honest nodes for a malicious node.
    """
    tolerance: int = None
    r"""
    The tolerance of the quantum leader election protocol. Default value
    is None. If None, the tolerance is set to the square root of the
    number of nodes.
    """
    def __init__(
            self,
            no_nodes: int,
            no_elections: int = 1,
            quantum_data_provider: qlep.core.QuantumDataProvider = None,
            committee: qlep.core.Committee = None,
            use_history: bool = False,
            tolerance: int = None) -> None:
        r"""
        Quantum Leader Election Protocol with W state

        Args:
            no_nodes :
                The number of nodes in the quantum leader election protocol.
            no_elections :
                The number of elections in the quantum leader election
                protocol.
            quantum_data_provider :
                The provider of quantum data for the experiments.
            committee :
                The committee of the election. If None, the committee is
                computed as an ALL type committee. If not None, the
                committee is used as the committee of the election.
            use_history :
                The flag to use the history of the quantum leader election
                protocol. Default value is False. If True, the malicious
                attacker will use the history of the elections to not
                create more than the tolerance given conflicts with the
                honest nodes for a malicious node.
            tolerance :
                The tolerance of the quantum leader election protocol. Default
                value is None. If None, the tolerance is set to the square root
                of thenumber of nodes.
        """
        # call super class QuantumLeaderElectionProtocol constructor
        super().__init__(
            election_type=qlep.core.ElectionType.WSTATE,
            no_nodes=no_nodes,
            no_elections=no_elections,
            quantum_data_provider=quantum_data_provider,
            committee=committee
        )
        self.use_history = use_history
        if tolerance is None:
            self.tolerance = int(np.floor(np.sqrt(self.quantum_no_nodes)))
        else:
            self.tolerance = tolerance

    @override
    def get_quantum_circuits(
            self,
            measure: bool = True
    ) -> list[qiskit.QuantumCircuit]:
        return [WStateGenerator.get_quantum_circuits(
            no_nodes=self.quantum_no_nodes,
            measure=measure)
        ]

    @override
    def get_leader_election_algorithm(
            self
    ) -> qlep.core.LeaderElectionAlgorithm:
        return WStateLeaderelectionAlgorithm()

    @override
    def get_malicious_attacker(self) -> qlep.core.MaliciousAttacker:
        return WStateMaliciousAttacker(
            use_history=self.use_history,
            tolerance=self.tolerance
        )


class WStateGenerator:
    r"""
    W state quantum circuit generator
    """
    @staticmethod
    def FGate(n: int, k: int) -> qiskit.QuantumCircuit:
        """
        Fredkin gate for W state generation

        Args:
            n :
                The number of qubits in the W state
            k :
                The index of the qubit in the W state

        Returns:
            The Fredkin gate
        """
        quantum_circuit = qiskit.QuantumCircuit(2)
        theta = np.arccos(np.sqrt(1/(n-k+1)))
        quantum_circuit.ry(theta=-theta, qubit=1)
        quantum_circuit.cz(control_qubit=0, target_qubit=1)
        quantum_circuit.ry(theta=theta, qubit=1)
        return quantum_circuit.to_gate(label='F')

    @staticmethod
    def CXRVGate() -> qiskit.QuantumCircuit:
        """
        CXRV gate (inverse CNOT) for W state generation

        Returns:
            The CXRV gate
        """
        quantum_circuit = qiskit.QuantumCircuit(2)
        quantum_circuit.h(qubit=0)
        quantum_circuit.h(qubit=1)
        quantum_circuit.cx(control_qubit=1, target_qubit=0)
        quantum_circuit.h(qubit=0)
        quantum_circuit.h(qubit=1)
        return quantum_circuit.to_gate(label='CXRV')

    @staticmethod
    def get_quantum_circuits(
            no_nodes: int,
            measure: bool = True
    ) -> qiskit.QuantumCircuit:
        r"""
        Returns the quantum circuit for the W state

        Args:
            no_nodes :
                The number of nodes in the W state
            measure :
                The flag to measure the qubits in the W state.

        Returns:
            quantum_circuit
                The quantum circuit for the W state
        """
        quantum_registers = qiskit.QuantumRegister(no_nodes, 'q')
        if measure:
            classic_registers = qiskit.ClassicalRegister(no_nodes, 'c')
            quantum_circuit = qiskit.QuantumCircuit(quantum_registers,
                                                    classic_registers)
        else:
            quantum_circuit = qiskit.QuantumCircuit(quantum_registers)
        quantum_circuit.x(quantum_registers[no_nodes-1])
        for node_index in range(0, no_nodes-1):
            quantum_circuit.append(
                WStateGenerator.FGate(no_nodes, k=node_index+1),
                [
                    quantum_registers[no_nodes-node_index-1],
                    quantum_registers[no_nodes-node_index-2]
                ]
            )
            # quantum_circuit.barrier(quantum_registers[n-node_index-1])
            quantum_circuit.barrier(
                [quantum_registers[no_nodes-node_index-2],
                 quantum_registers[no_nodes-node_index-1]]
            )
        for node_index in range(0, no_nodes-1):
            quantum_circuit.append(
                WStateGenerator.CXRVGate(),
                [
                    quantum_registers[no_nodes-node_index-2],
                    quantum_registers[no_nodes-node_index-1]
                ]
            )
            quantum_circuit.barrier(
                [quantum_registers[no_nodes-node_index-2],
                 quantum_registers[no_nodes-node_index-1]]
            )
        if measure:
            quantum_circuit.measure(quantum_registers, classic_registers)
        return quantum_circuit


class WStateLeaderelectionAlgorithm(qlep.core.LeaderElectionAlgorithm):
    r"""
    Leader election algorithm for the W state
    """
    def __init__(self) -> None:
        super().__init__()

    @override
    def elect(self, data: np.ndarray) -> int:
        r"""
        Returns the leader index from the given data.
        If no leader is found, returns -1.

        Args:
            data :
                The data from the quantum leader election protocol
                The shape of the data is (1, no_nodes). Only one
                position in the data is expected to be 1, the rest
                are 0. If there is no 1 in the data, or more than
                1 1s in the data, then the election is invalid.

        Returns:
            leader_index :
                The index of the leader in the data. If no leader
                is found, returns -1.
        """
        # first zero for only one circuit
        # second zero for only one round
        valid_leader = np.count_nonzero(data[0][0]) == 1
        if (valid_leader):
            return np.where(data[0][0] == 1)[0][0]
        else:
            return -1


class WStateMaliciousAttacker(qlep.core.MaliciousAttacker):
    r"""
    Malicious attacker for the W state
    """

    use_history: bool = False
    r"""
    The flag to use the history of the quantum leader election protocol.
    Default value is False. If True, the malicious attacker will use
    the history of the elections to not create more than the tolerance
    given conflicts with the honest nodes for a malicious node.
    """
    tolerance: int = None
    r"""
    The tolerance of the quantum leader election protocol. Default
    value is None.
    """
    conflicts: dict[int, list[int]] = {}
    r"""
    The conflicts of the malicious attacker. The key is the malicious
    node ID, and the value is the list of the honest node IDs with
    which the malicious node has conflicts.
    """
    def __init__(
                self,
                use_history: bool = False,
                tolerance: int = None
    ) -> None:
        r"""
        Malicious attacker for the W state

        Args:
            use_history :
                The flag to use the history of the quantum leader election
                protocol. Default value is False. If True, the malicious
                attacker will use the history of the elections to not create
                more than the tolerance given conflicts with the honest nodes
                for a malicious node.
            tolerance :
                The tolerance of the quantum leader election protocol. Default
                value is None.
        """
        super().__init__()
        self.use_history = use_history
        self.tolerance = tolerance
        # setup the conflicts
        if self.use_history:
            self.conflicts: dict[int, list[int]] = {}

    def reset(self) -> None:
        r"""
        Resets the conflicts of the malicious attacker
        """
        if self.use_history:
            logging.info("""[WStateMaliciousAttacker][reset] no_elections
                         conflicts""" + str(self.conflicts) + " %d, %d",
                         self.use_history, self.tolerance)
            self.conflicts: dict[int, list[int]] = {}

    @override
    def attack(
                self,
                register_ids: np.ndarray,
                data: np.ndarray,
                malicious_ids: np.ndarray
            ) -> np.ndarray:
        r"""
        Returns the modified data from the given data.
        If no malicious nodes are under our control, then
        the given data is returned. If there are malicious
        nodes under our control, then the given data is
        modified to invalidate the election or make one
        of the malicious nodes the leader.

        Args:
            register_ids :
                The register IDs of the nodes in the quantum leader
                election protocol. The shape of the register IDs is
                (no_nodes).
            data :
                The data from the quantum leader election protocol
                The shape of the data is (1, no_nodes). Only one
                position in the data is expected to be 1, the rest
                are 0. If there is no 1 in the data, or more than
                1 1s in the data, then the election is invalid.
            malicious_ids :
                The IDs of the malicious nodes under our control.
                The shape of the malicious IDs is (no_malicious_nodes).

        Returns:
            modified_data :
                The modified data from the given data. If no malicious
                nodes are under our control, then the given data is
                returned. If there are malicious nodes under our control,
                then the given data is modified to invalidate the election
                or make one of the malicious nodes the leader. The shape
                of the modified data is (1, no_nodes).
        """
        # get the malicious no_nodes
        active_malicious_nodes = [x for x in register_ids
                                  if x in malicious_ids]
        # if no malicious no_nodes under our control than return the given data
        if not active_malicious_nodes:
            return data
        # init return data
        modified_data = np.copy(data)
        # getting the current result
        # one circuit one round
        results = np.where(data[0][0] == 1)[0]
        # invalidate_election if the election can be invalidated
        # malicious_leader_id is the id of the malicious node that will be
        # leader or will invalidate the election
        invalidate_election = False
        malicious_leader_id = -1
        # CASE 1 no winner
        # jsut get the first malicious node and made him leader
        if (len(results) == 0):
            malicious_leader_id = active_malicious_nodes[0]
            invalidate_election = True
        # CASE 2 one winner
        elif (len(results) == 1):
            leader_index = results[0]
            leader_id = register_ids[leader_index]
            # case 2.1 malicious winner
            if leader_id in malicious_ids:
                malicious_leader_id = leader_id
                invalidate_election = True
            # case 2.2 honest winner
            # the attacker try to invalidate the election by
            # creating a conflcit with one of the malicious no_nodes
            # with the keep of tollerance
            else:
                if self.use_history:
                    for malicious_node in active_malicious_nodes:
                        if malicious_node in self.conflicts:
                            if leader_id in self.conflicts[malicious_node]:
                                malicious_leader_id = malicious_node
                                invalidate_election = True
                        else:
                            self.conflicts[malicious_node] = []
                    if invalidate_election is False:
                        for malicious_node in active_malicious_nodes:
                            if (len(self.conflicts[malicious_node]) <
                                    self.tolerance):
                                self.conflicts[malicious_node].append(
                                    leader_id
                                )
                                malicious_leader_id = malicious_node
                                invalidate_election = True
                                break

                else:
                    malicious_leader_id = active_malicious_nodes[0]
                    invalidate_election = True
        # case 3 more winners
        else:
            no_honest_proposed = 0
            malicious_leader_id = -1
            for index in results:
                # for honest winners
                if register_ids[index] not in malicious_ids:
                    no_honest_proposed = no_honest_proposed + 1
                    leader_id = register_ids[index]
                else:
                    malicious_leader_id = register_ids[index]
            # case 3.1 2 or more honest no_nodes
            # don't do anything
            if no_honest_proposed > 1:
                invalidate_election = False
            # semiliar with case 1 with winner honest
            # case 3.2 one honest winner
            # let the conflict with the propoer malicious node
            elif no_honest_proposed == 1:
                invalidate_election = False
                if self.use_history:
                    for malicious_node in active_malicious_nodes:
                        if malicious_node in self.conflicts:
                            if leader_id in self.conflicts[malicious_node]:
                                malicious_leader_id = malicious_node
                                invalidate_election = True
                        else:
                            self.conflicts[malicious_node] = []
                    if invalidate_election is False:
                        for malicious_node in active_malicious_nodes:
                            if (len(self.conflicts[malicious_node]) <
                                    self.tolerance):
                                self.conflicts[malicious_node].append(
                                    leader_id
                                )
                                malicious_leader_id = malicious_node
                                invalidate_election = True
                                break
                else:
                    malicious_leader_id = active_malicious_nodes[0]
                    invalidate_election = True
            # case 3.2 only malicious winners but multiple chose one
            else:
                malicious_leader_id = active_malicious_nodes[0]
                invalidate_election = True
        for node_index in range(0, len(register_ids)):
            if register_ids[node_index] in malicious_ids:
                modified_data[0, 0, node_index] = 0
                if (invalidate_election and
                        (register_ids[node_index] == malicious_leader_id)):
                    modified_data[0, 0, node_index] = 1
        return modified_data
        # summary
        # CASE 1 -- now inner
        # CASE 2 -- one winner
        # case 2.1 -- malicious node winner
        # Case 2.2 -- honest leader winner
        # case 3 -- multple winners
        # Case 3.1 -- multiple honest winners
        # Case 3.2 -- one honest winner
        # Case 3.3 -- multiple malicious winners
