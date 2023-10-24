r"""
The module with the GHZ state quantum leader election protocol
"""
# logging
import logging
# lep base
import qlep.core
# numpy
import numpy as np
# qiskit
import qiskit
# quantum proof of stake
import qlep.core.qpos
# typing
import typing
# override decorator
from typing_extensions import override


class GHZStateQLEP(qlep.core.QuantumLeaderElectionProtocolwithPoS):
    r"""
    The GHZStateQLEP class implements the Quantum Leader Election Protocol
    using the GHZ state
    """
    fewer_qubits: bool = False
    r"""
    If True than the number of qubits used is reduced to the minimum
    required for the number of nodes, but it is not possible to use
    the stake vector.
    """
    def __init__(
                self,
                no_nodes: int,
                no_elections: int = 1,
                quantum_data_provider: qlep.core.QuantumDataProvider = None,
                committee: qlep.core.Committee = None,
                stake_vector: np.ndarray = None,
                fewer_qubits: bool = False
    ) -> None:
        r"""
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
            stake_vector :
                The stake vector for the quantum leader election protocol.
            fewer_qubits :
                If True than the number of qubits used is reduced to the
                minimum required for the number of nodes, but it is not
                possible to use the stake vector.

        Raises:
            ValueError : fewer_qubits is True and use_stake is True
        """
        # call super class QuantumLeaderElectionProtocolwithPoS constructor
        super().__init__(
            election_type=qlep.core.ElectionType.GHZSTATE,
            no_nodes=no_nodes,
            no_elections=no_elections,
            quantum_data_provider=quantum_data_provider,
            committee=committee,
            stake_vector=stake_vector
        )
        # compute the number of election rounds
        # log2(no_nodes) = no_election_rounds
        self.no_election_rounds: int = int(
            np.ceil(np.log2(self.quantum_no_nodes)))
        self.fewer_qubits: bool = fewer_qubits
        # if fewer qubits than the number of elections
        # must be multiply by the number of election rounds
        # every experiment it gives one bit out of
        # log2(no_nodes) bits.
        if self.fewer_qubits:
            if self.use_stake:
                logging.error("""[GHZStateQLEP] use of stake vector
                              is not supported with fewer qubits
                              mode""")
                raise ValueError("use_stake and fewer_qubits")
            self.quantum_no_elections: int =\
                self.no_election_rounds * self.quantum_no_elections

    @override
    def _shape_quantum_data(
            self,
            data: list[np.ndarray]
    ) -> np.ndarray:
        r"""
        Reshape the data array to the correct shape

        Args:
            data :
                The data array. It is a 2D array with the shape
                (quantum_no_elections * no_election_rounds,
                quantum_no_nodes). In the case of fewer_qubits
                is True the quantum_no_elections is divided by
                no_election_rounds.

        Returns:
            data
                The data array. It is a 3D array with the shape
                (quantum_no_elections, no_election_rounds,
                quantum_no_nodes) if fewer_qubits is False.
                Otherwise quantum_no_elections is divided by
                no_election_rounds.
        """
        if self.fewer_qubits:
            no_quantum_circuits = len(data)
            real_no_elections: int = int(
                np.floor(
                    self.quantum_no_elections /
                    self.no_election_rounds
                )
            )
            for index in range(no_quantum_circuits):
                data[index].shape = (
                    real_no_elections,
                    self.no_election_rounds,
                    self.quantum_no_nodes
                )
            quantum_data: np.ndarray = np.concatenate(data, axis=1)
            quantum_data.shape = (
                real_no_elections,
                no_quantum_circuits,
                self.no_election_rounds,
                self.quantum_no_nodes
            )
            return quantum_data
        else:
            return super()._shape_quantum_data(data)

    @override
    def get_experiment_information(self) -> dict[str, typing.Any]:
        r"""
        Get the experiment info. It calls the super class method and
        adds the fewer_qubits attribute.

        Returns:
            experimentInfo
                The experiment information dictionary.
        """
        experimentInfo = super().get_experiment_information()
        experimentInfo['fewer_qubits'] = self.fewer_qubits
        return experimentInfo

    @override
    def _get_stake_quantum_circuits(
            self,
            measure: bool = True,
            stake_vector: np.ndarray = None
    ) -> list[qiskit.QuantumCircuit]:
        return [GHZStateGenerator.get_quantum_circuits(
            no_nodes=self.quantum_no_nodes,
            stake_vector=stake_vector,
            fewer_qubits=self.fewer_qubits,
            measure=measure
        )]

    @override
    def get_leader_election_algorithm(
            self
    ) -> qlep.core.LeaderElectionAlgorithm:
        return GHZLeaderElectionAlgorithm()

    @override
    def get_malicious_attacker(self) -> qlep.core.MaliciousAttacker:
        return GHZMaliciousAttacker()


class GHZStateGenerator:
    r"""
    The GHZStateGenerator class implements the generation of the
    Greenberger-Horne-Zeilinger state state
    """
    @staticmethod
    def get_one_qubit_GHZ(
        no_nodes: int,
        measure: bool = True
    ) -> qiskit.QuantumCircuit:
        r"""
        Get the quantum circuit for the GHZ state with one qubit as data bit
        for the given number of nodes. It is used for the fewer_qubits mode.
        The data qubit goes through an Hadamard gate and than it is used
        as control qubit for the CNOT gates to all the other qubits. In
        this case it use a cascade of CNOT gates from the first qubit to
        the last qubit.

        Args:
            no_nodes :
                The number of nodes in the quantum leader election protocol.
            measure :
                If True than measure the qubits. Default value is True.

        Returns:
            quantum_circuit :
                The quantum circuit for the GHZ state with one qubit
                as data bit for the given number of nodes.
        """
        quantum_registers = qiskit.QuantumRegister(no_nodes, 'q')
        if measure:
            classic_registers = qiskit.ClassicalRegister(no_nodes, 'c')
            quantum_circuit = qiskit.QuantumCircuit(quantum_registers,
                                                    classic_registers)
        else:
            quantum_circuit = qiskit.QuantumCircuit(quantum_registers)
        quantum_circuit.h(quantum_registers[0])
        for index in range(0, no_nodes-1):
            quantum_circuit.cx(control_qubit=quantum_registers[index],
                               target_qubit=quantum_registers[index+1])
        quantum_circuit.barrier()
        if measure:
            quantum_circuit.measure(quantum_registers, classic_registers)
        return quantum_circuit

    @staticmethod
    def get_quantum_circuits(
        no_nodes: int,
        stake_vector: np.ndarray = None,
        fewer_qubits: bool = False,
        measure: bool = True
    ) -> qiskit.QuantumCircuit:
        r"""
        Get the quantum circuit for the GHZ state for the given number of
        nodes.

        The data qubits go through an Hadamard gate and than it is
        used as control qubits for the CNOT gates cascade. It has two modes:
        fewer_qubits = True: the number of qubits used is reduced to the
        minimum required for the number of nodes, but it is not possible to
        use the stake vector. And it generates the data qubits separately.
        fewer_qubits = False: the number of qubits used is equal to the
        number of nodes multiplied by the number of election rounds
        (log2(no_nodes)). And it generates the data qubits together
        with Hadamard gates or the from the stake vector.

        Args:
            no_nodes :
                The number of nodes in the quantum leader election protocol.
            stake_vector :
                The stake vector for the quantum leader election protocol.
            fewer_qubits :
                If True than the number of qubits used is reduced to the
                minimum required for the number of nodes, but it is not
                possible to use the stake vector.
            measure :
                If True than measure the qubits.

        Returns:
            quantum_circuit :
                The quantum circuit for the GHZ state for the given number of
                nodes.
        """
        if fewer_qubits:
            return GHZStateGenerator.get_one_qubit_GHZ(
                no_nodes=no_nodes,
                measure=measure
            )
        else:
            no_data_qubits = int(np.ceil(np.log2(no_nodes)))
            no_election_rounds = no_data_qubits
            no_qubits = no_data_qubits * no_nodes
            quantum_registers = qiskit.QuantumRegister(no_qubits, 'q')
            if measure:
                classic_registers = qiskit.ClassicalRegister(no_qubits, 'c')
                quantum_circuit = qiskit.QuantumCircuit(quantum_registers,
                                                        classic_registers)
            else:
                quantum_circuit = qiskit.QuantumCircuit(quantum_registers)

            # extract the indexes for the data qubits
            data_indexes = [x * no_nodes for x in range(0, no_data_qubits)]

            # if stake vector is given than use it
            if not (stake_vector is None):
                quantum_circuit.append(
                    qlep.core.qpos.get_stake_gate(stake_vector),
                    [quantum_registers[index] for index in data_indexes])
            # The use of hadamard gates -> this generates also the |00...00>
            # superposition it use less gates and more stable gates
            else:
                for index in data_indexes:
                    quantum_circuit.h(quantum_registers[index])
            quantum_circuit.barrier()

            for rounds_index in range(0, no_election_rounds):
                for index in range(0, no_nodes - 1):
                    quantum_circuit.cx(
                        control_qubit=quantum_registers[
                            rounds_index*no_nodes+index],
                        target_qubit=quantum_registers[
                            rounds_index*no_nodes+index+1]
                    )
            quantum_circuit.barrier()
            if measure:
                quantum_circuit.measure(quantum_registers, classic_registers)
            return quantum_circuit


class GHZLeaderElectionAlgorithm(qlep.core.LeaderElectionAlgorithm):
    r"""
    The GHZLeaderElectionAlgorithm class implements the leader election
    algorithm for the GHZ state
    """
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def local_node_elect(bits: np.ndarray) -> int:
        r"""
        Compute the GHZ local leader from the bits array
        given as input for a node.

        Args:
            bits :
                The bits array. It is a 1D array with the shape
                (no_election_rounds,). It contains the bits
                for the node.

        Returns:
            leader_index :
                The leader index. The intger value of the bits
                binary array.
        """
        # sum(2^[0:no_election_rounds] * bits)
        # the integer value of the bits binary array
        return np.sum(
            np.power(
                2 * np.ones(shape=len(bits), dtype=int),
                np.arange(len(bits))
            ) *
            bits
        )

    def elect(self, data: np.ndarray) -> int:
        (no_quantum_circuits, no_election_rounds, no_nodes) = data.shape
        # transform data to leaders
        leader_indexes: np.ndarray = np.array(
            [GHZLeaderElectionAlgorithm.local_node_elect(
                data[0, :, node_index]
            )
             for node_index in range(0, no_nodes)]
        )
        # take all the unique values registed by the no_nodes and their counts
        unique, counts = np.unique(leader_indexes, return_counts=True)
        index = np.argmax(counts)
        no_nodes = len(leader_indexes)
        # if the maximum ecounter is more than half of the no_nodes
        # than it is the new leader
        valid_leader = counts[index] > (no_nodes / 2)
        if (valid_leader):
            return unique[index]
        else:
            return -1


class GHZMaliciousAttacker(qlep.core.MaliciousAttacker):
    r"""
    The GHZMaliciousAttacker class implements the malicious attacker
    for the GHZ state.
    """
    def __init__(self) -> None:
        super().__init__()

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
        # compute the ranking for the honest nodes
        honest_leader_indexes = np.array(
            [GHZLeaderElectionAlgorithm.local_node_elect(data[0, :, index])
             for index in range(0, len(register_ids))
             if register_ids[index] not in malicious_ids]
        )

        # Find the most voted malicious node by honest nodes and than
        # make all the malicious nodes vote for it

        # compute the current best candidates for election
        unique, counts = np.unique(honest_leader_indexes, return_counts=True)
        # sort elements by the counts number
        count_sort_ind = np.argsort(-counts)
        unique = unique[count_sort_ind]
        # search for a malicious node inside already proposed laders
        found_malicious_node: bool = False
        malicious_index: int = -1
        for index in range(0, len(unique)):
            # do not take in account invalid values
            if ((unique[index] != -1) and
                    (unique[index] < len(register_ids))):
                # The first possible leader node that is malicious
                if register_ids[unique[index]] in malicious_ids:
                    found_malicious_node = True
                    malicious_index = unique[index]
                    break
        # if not malicious node found than send the
        # result of the first malicious
        if not found_malicious_node:
            maliciousLeaderID = malicious_nodes[0]
            found = np.where(register_ids == maliciousLeaderID)
            malicious_index = found[0][0]
        # create data to send
        tmp = malicious_index
        to_send = np.zeros(shape=len(data[0]), dtype=int)
        for kindex in range(0, len(data[0])):
            to_send[kindex] = tmp % 2
            tmp = tmp / 2
        # modify data for malicious no_nodes
        for node_index in range(0, len(register_ids)):
            if register_ids[node_index] in malicious_ids:
                modified_data[0, :, node_index] = np.copy(to_send)
        return modified_data
