r"""
The Fold-Hamming module for the quantum leader election protocol.
"""
# Hamming code
from __future__ import annotations
# qiskit
import qiskit
# numpy
import numpy as np
# lep base module
import qlep.core
# quantum proof of stake
import qlep.core.qpos
# logging
import logging
# override decorator
from typing_extensions import override

__all__ = ["FoldHammingQLEP", "FoldHammingStateGenerator",
           "FoldHammingLeaderElectionAlgorithm",
           "FoldHammingMaliciousAttacker",
           "FoldHamming"]


class FoldHammingQLEP(qlep.core.QuantumLeaderElectionProtocolwithPoS):
    r"""
    FoldHammingQLEP class for Fold-Hamming codes superposition
    when D=[n/2]
    """

    no_data_bits: int = None
    r"""
    The number of data bits
    """
    fold: int = None
    r"""
    The number of folds
    """
    limit: int = None
    r"""
    The limit given by the how many points connecting to a specific
    data bit can a node control.
    """
    no_election_rounds: int = None
    r"""
    The number of election rounds it is the number of nodes for this
    type of election.
    """
    def __init__(
        self,
        no_nodes: int,
        no_elections: int = 1,
        quantum_data_provider: qlep.core.QuantumDataProvider = None,
        committee: qlep.core.Committee = None,
        stake_vector: np.ndarray = None,
        fold: int = 3,
        limit: int = 2
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
            fold :
                The number of folds in the Fold-Hamming codes superposition.
            limit :
                The maximum number of qubits connection for a node to a given
        Raises:
            ValueError : If the number of nodes is not 2^x-1.
        """
        # call super class QuantumLeaderElectionProtocolwithPoS constructor
        super().__init__(
            election_type=qlep.core.ElectionType.FOLDHAMMING,
            no_nodes=no_nodes,
            no_elections=no_elections,
            quantum_data_provider=quantum_data_provider,
            committee=committee,
            stake_vector=stake_vector
        )
        self.no_data_bits: int = int(np.ceil(np.log2(self.quantum_no_nodes)))
        self.fold: int = fold
        self.no_election_rounds: int = self.fold
        self.limit: int = limit
        if (((2 ** self.no_data_bits - 1) * self.fold) !=
                (self.quantum_no_nodes * self.fold)):
            logging.error("""[FoldHammingQLEP] no_nodes/committee size
                          for hamming must be 2^(n-1) * fold -  %d
                          : %d - %d""", self.quantum_no_nodes,
                          ((2 ** self.no_data_bits - 1) * self.fold),
                          self.no_data_bits)
            raise ValueError("committee size for hamming must be 2^x-1")

    @override
    def _get_election_name(self) -> str:
        return str(self.fold) + "_" + self.election_type.name

    @override
    def _get_stake_quantum_circuits(
        self,
        measure: bool = True,
        stake_vector: np.ndarray = None
    ) -> list[qiskit.QuantumCircuit]:
        return [FoldHammingStateGenerator.get_quantum_circuits(
            no_data_bits=self.no_data_bits,
            stake_vector=stake_vector,
            fold=self.fold,
            limit=self.limit,
            measure=measure
        )]

    @override
    def get_leader_election_algorithm(
            self
    ) -> qlep.core.LeaderElectionAlgorithm:
        return FoldHammingLeaderElectionAlgorithm(
            no_data_bits=self.no_data_bits,
            fold=self.fold,
            limit=self.limit
        )

    @override
    def get_malicious_attacker(self) -> qlep.core.MaliciousAttacker:
        return FoldHammingMaliciousAttacker(
            no_data_bits=self.no_data_bits,
            fold=self.fold,
            limit=self.limit
        )


class FoldHammingStateGenerator:
    r"""
    FoldHammingStateGenerator class for Fold-Hamming codes superposition
    when D=[n/2]
    """
    @staticmethod
    def get_quantum_circuits(
        no_data_bits: int,
        fold: int = 1,
        limit: int = 1,
        stake_vector: np.ndarray = None,
        measure: bool = True
    ) -> qiskit.QuantumCircuit:
        r"""
        Get the quantum circuit for the number of data bits,
        using or not a unitary matrix for the initial data qubits.

        Args:
            no_data_bits :
                The number of data bits.
            stake_vector :
                If True than measure the qubits.
            measure :
                The flag for measuring the quantum circuit.
            fold :
                The number of folds in the Fold-Hamming codes superposition.
            limit :
                The maximum number of qubits connection for a node to a given

        Returns:
            quantum_circuit
                The quantum circuit for the Fold-Hamming state for the given
                number of data bits.
        """
        # the number of nodes
        no_nodes = (2 ** no_data_bits - 1)
        # the number of qubits = the number of no_nodes m ultiply by
        # the number of folds
        no_qubits = no_nodes * fold
        # the index matrix
        index_matrix = FoldHamming.get_index_matrix(
            no_data_bits=no_data_bits,
            fold=fold,
            limit=limit
        )
        # the qubits register
        quantum_registers = qiskit.QuantumRegister(no_qubits, 'q')
        if measure:
            # the calssic registers
            classic_registers = qiskit.ClassicalRegister(no_qubits, 'c')
            # the qunatum circuit
            quantum_circuit = qiskit.QuantumCircuit(
                quantum_registers,
                classic_registers
            )
        else:
            # the qunatum circuit
            quantum_circuit = qiskit.QuantumCircuit(quantum_registers)

        # find the index of the data qubits
        data_indexes = []
        for index in range(0, no_nodes):
            binary_representation = (
                format(index+1, 'b').zfill(no_data_bits)[::-1]
            )
            # if the bit is a parity qubit
            if binary_representation.count('1') == 1:
                data_indexes.append(index)
        # generate superposition of data qubits
        if not (stake_vector is None):
            quantum_circuit.append(
                qlep.core.qpos.get_stake_gate(stake_vector),
                [quantum_registers[index] for index in data_indexes]
            )
        # The use of hadamard gates
        # it use less gates and more stable gates
        else:
            for index in data_indexes:
                quantum_circuit.h(quantum_registers[index])
        quantum_circuit.barrier()
        # generate first segment of hamming code
        for index in range(0, no_nodes):
            binary_representation = (
                format(index+1, 'b').zfill(no_data_bits)[::-1]
            )
            # if the bit is not a quparity bit
            # add the corespondent cx gates with the parity qubits
            if binary_representation.count('1') == 1:
                continue
            else:
                for dataIndex in range(0, no_data_bits):
                    if (binary_representation[dataIndex] == '1'):
                        quantum_circuit.cx(
                            target_qubit=quantum_registers[index],
                            control_qubit=quantum_registers[
                                data_indexes[dataIndex]
                            ]
                        )
        quantum_circuit.barrier()
        # generate the next segments of hamming code by using identity matrix
        for index in range(0, no_nodes):
            for kindex in range(1, fold):
                quantum_circuit.cx(
                    target_qubit=quantum_registers[kindex*no_nodes + index],
                    control_qubit=quantum_registers[
                        index_matrix[kindex, index] - 1
                    ]
                )
        quantum_circuit.barrier()
        if measure:
            quantum_circuit.measure(quantum_registers, classic_registers)
        return quantum_circuit


class FoldHammingLeaderElectionAlgorithm(qlep.core.LeaderElectionAlgorithm):
    r"""
    FoldHammingLeaderElectionAlgorithm class for Fold-Hamming codes
    when D=[n/2]
    """

    no_data_bits: int = None
    r"""
    The number of data bits
    """
    fold_hamming_coder: FoldHamming = None
    r"""
    The FoldHamming object. The coder is used to encode and decode the
    data bits. In this case the coder is used to decode the data bits.
    """
    fold: int = None
    r"""
    The number of folds
    """
    limit: int = None
    r"""
    The limit given by the how many points connecting to a specific
    data bit can a node control.
    """
    def __init__(
        self,
        no_data_bits: int,
        fold: int = 3,
        limit: int = 2
    ) -> None:
        r"""
        Args:
            no_data_bits :
                The number of data bits.
            fold :
                The number of folds.
            limit :
                The limit given by the how many points connecting
                to a specific data bit can a node control.
        """
        super().__init__()
        self.no_data_bits: int = no_data_bits
        self.fold: int = fold
        self.limit: int = limit
        self.fold_hamming_coder: FoldHamming = FoldHamming(
            no_data_bits=self.no_data_bits,
            fold=self.fold,
            limit=self.limit
        )

    @override
    def elect(self, data: np.ndarray) -> int:
        r"""
        Elect the leader from the given data bits.

        Args:
            data :
                The data bits. In this case the codeword bits.
                The shape of the array is (1, no_nodes).

        Returns:
            leader_index
                The index of the leader. If the leader index is -1 than the
                election is invalid.
        """
        bits_array = np.copy(data)
        # make one bitrsting from all the folds
        bits_array.shape = self.fold * len(data[0, 0])
        leader_index = self.fold_hamming_coder.decode(bits_array)
        if (leader_index != -1):
            leader_index = leader_index - 1
        return leader_index


class FoldHammingMaliciousAttacker(qlep.core.MaliciousAttacker):
    r"""
    FoldHammingMaliciousAttacker class for Fold-Hamming codes
    when D=[n/2]
    """

    no_data_bits: int = None
    r"""
    The number of data bits
    """
    fold_hamming_coder: FoldHamming = None
    r"""
    The FoldHamming object. The coder is used to encode and decode the
    data bits. In this case the coder is used to decode the data bits.
    """
    fold: int = None
    r"""
    The number of folds
    """
    limit: int = None
    r"""
    The limit given by the how many points connecting to a specific
    data bit can a node control.
    """
    def __init__(
        self,
        no_data_bits: int,
        fold: int = 3,
        limit: int = 2
    ) -> None:
        r"""
        Args:
            no_data_bits :
                The number of data bits.
            fold :
                The number of folds.
            limit :
                The limit given by the how many points connecting
                to a specific data bit can a node control.
        """
        super().__init__()
        self.no_data_bits: int = no_data_bits
        self.fold: int = fold
        self.limit: int = limit
        self.fold_hamming_coder: FoldHamming = FoldHamming(
            no_data_bits=self.no_data_bits,
            fold=self.fold,
            limit=self.limit
        )

    def attack(
        self,
        register_ids: np.ndarray,
        data: np.ndarray,
        malicious_ids: np.ndarray
    ) -> np.ndarray:
        r"""
        Modify the data bits for the benefit of the malicious attacker.
        Data can be modified only on the positions of the malicious nodes.

        Args:
            register_ids :
                The ids of the nodes.
            data :
                The data bits. In this case the codeword bits received by the
                nodes.
            malicious_ids :
                The ids of the malicious nodes.

        Returns:
            modified_data
                The modified data bits after the attack.
        """
        # get the malicious no_nodes
        malicious_nodes = [x for x in register_ids if x in malicious_ids]
        # if no malicious no_nodes under our control than return the given data
        if not malicious_nodes:
            return data
        # init return data
        modified_data = np.copy(data)

        # decode the current value
        bits_array = np.copy(data)
        bits_array.shape = self.fold * len(register_ids)
        leader_index = self.fold_hamming_coder.decode(bits_array)
        if (leader_index != -1):
            leader_index = leader_index - 1
        # getting the current result on the honest results
        # make the attack
        # if the winner is malicious
        if ((leader_index != -1) and
                (register_ids[leader_index] in malicious_ids)):
            return modified_data
        else:
            # if the leader can be changed
            change_leader: bool = False
            # if the election can become invalid
            invalidate_leader: bool = False
            change_leader_index: int = -1
            invalidate_leader_index: int = -1
            # see the differences from the other encoded values
            differences: np.ndarray = self.fold_hamming_coder.differences(
                bits_array
            )
            min_distance: int = len(register_ids) * self.fold
            # compute the distance
            for index in range(0, len(register_ids)):
                distance = np.count_nonzero(differences[index+1])
                no_controled_positions: int = 0
                # get the no_nodes which can change the values
                changeable_nodes = np.where(differences[index+1] == 1)[0]
                for kindex in range(0, self.fold):
                    # for every fold find how many positions the malicious
                    # nodes control
                    possible_nodes = changeable_nodes[
                        (changeable_nodes >= kindex*len(register_ids)) &
                        (changeable_nodes < (kindex+1)*len(register_ids))
                    ] % len(register_ids)
                    for node_index in possible_nodes:
                        if register_ids[node_index] in malicious_ids:
                            no_controled_positions = no_controled_positions + 1
                distance = distance - no_controled_positions
                # if the node is malicious and the change can be done
                if register_ids[index] in malicious_ids:
                    if ((distance <=
                            self.fold_hamming_coder.correcting_distance) and
                            (distance < min_distance)):
                        change_leader = True
                        change_leader_index = index
                        min_distance = distance
                # if the election can be at least invalidate
                if (distance ==
                        (int(np.floor(
                        self.fold_hamming_coder.correcting_distance)) + 1)):
                    invalidate_leader = True
                    invalidate_leader_index = index
            # if the leader can be changed or invalidated
            if change_leader or invalidate_leader:
                # get the necessary index
                malicious_index: int = -1
                if change_leader:
                    malicious_index = change_leader_index
                else:
                    malicious_index = invalidate_leader_index
                # make the data bits and for it and find out the encoded value
                # no_data_bits = int(np.ceil(np.log2(self.no_nodes)))
                temp: np.ndarray = np.zeros(shape=self.no_data_bits)
                binary_representation = (
                    format(malicious_index+1, 'b')
                    .zfill(self.no_data_bits)[::-1]
                )
                for dataIndex in range(0, self.no_data_bits):
                    if (binary_representation[dataIndex] == '1'):
                        temp[dataIndex] = 1
                    else:
                        temp[dataIndex] = 0
                # the encoded value
                to_send = self.fold_hamming_coder.encode(temp)
                to_send.shape = (self.fold, len(register_ids))
                # modify data for malicious no_nodes
                for node_index in range(0, len(register_ids)):
                    if register_ids[node_index] in malicious_ids:
                        modified_data[0, :, node_index] = (
                            to_send[:, node_index]
                        )
            # attack when it can make the index 0 of decoding == invalid
            # or maybe if nothings work just send zeroes to be close to
            # that value
            else:
                # the encoded value
                temp = np.zeros(shape=self.no_data_bits)
                to_send = self.fold_hamming_coder.encode(temp)
                to_send.shape = (self.fold, len(register_ids))
                # modify data for malicious no_nodes
                for node_index in range(0, len(register_ids)):
                    if register_ids[node_index] in malicious_ids:
                        modified_data[0, :, node_index] = (
                            to_send[:, node_index]
                        )
        return modified_data


class FoldHamming:
    r"""
    FoldHamming class for Fold-Hamming codewords. It can be
    used to encode and decode bit strings.
    """

    no_data_bits: int = None
    r"""
    The number of data bits
    """
    no_bits: int = None
    r"""
    The number of bits of the codewords
    """
    distance: int = None
    r"""
    The minimum distance of the codewords
    """
    correcting_distance: float = None
    r"""
    The number of errors that can be corrected
    """
    encode_matrix: np.ndarray = None
    r"""
    The encode matrix
    """
    decode_matrix: np.ndarray = None
    r"""
    The decode matrix
    """
    fold: int = None
    r"""
    The number of folds
    """
    no_nodes: int = None
    r"""
    The number of nodes
    """
    index_matrix: np.ndarray = None
    r"""
    The index matrix
    """
    def __init__(
            self,
            no_data_bits: int = 3,
            fold: int = 3,
            limit: int = 2) -> None:
        r"""
        Args:
            no_data_bits :
                The number of data bits.
            fold :
                The number of folds.
            limit :
                The limit given by the how many points connecting
                to a specific data bit can a node control.
        """
        # the number of data bits
        self.no_data_bits: int = no_data_bits
        # the number of no_nodes
        self.no_nodes: int = (2 ** self.no_data_bits - 1)
        # the number of folds
        self.fold: int = fold
        # the number of final bits
        self.no_bits: int = self.no_nodes * self.fold
        # the distance
        self.distance: int = self.fold * int(np.floor((self.no_nodes + 1) / 2))
        # correcting distance
        self.correcting_distance: float = (self.distance - 1) / 2
        # we generate de encode matrix similar to normal hamming
        # but for the folds we used a index matrix every extra bit is
        # close connect to one of the first n bits
        self.encode_matrix: np.ndarray = np.zeros(
            shape=(self.no_data_bits, self.no_bits),
            dtype=int
        )
        # decide the first n bits similar to hamming
        for index in range(0, self.no_nodes):
            binary_representation = (
                format(index+1, 'b').zfill(self.no_data_bits)[::-1]
            )
            for data_index in range(0, self.no_data_bits):
                if (binary_representation[data_index] == '1'):
                    self.encode_matrix[data_index, index] = 1
        # rest of the encode matrix
        # take the index matrix to know the connections between the bits
        self.index_matrix = FoldHamming.get_index_matrix(
            no_data_bits=no_data_bits,
            fold=self.fold,
            limit=limit
        )
        # for every fold
        for kindex in range(1, self.fold):
            # for every node
            for index in range(0, self.no_nodes):
                # for every given data bit
                for data_index in range(0, self.no_data_bits):
                    # the results value is given by the connected bit
                    # from the first fold. the index matrix use value
                    # from 1 to n inclusive, by subtracting 1 we go in
                    # the 0 to n-1 domain
                    self.encode_matrix[
                        data_index,
                        kindex*self.no_nodes+index
                    ] = self.encode_matrix[
                        data_index,
                        self.index_matrix[kindex, index]-1
                    ]
        # the decode matrix is made similar to hamming decode matrix
        # we take all the possible value and encode them to generate a row
        # in the decode matrix
        self.decode_matrix: np.ndarray = np.zeros(
            shape=(self.no_nodes+1, self.no_bits),
            dtype=int
        )
        temp: np.ndarray = np.zeros(shape=self.no_data_bits)
        for index in range(0, self.no_nodes+1):
            binary_representation = (
                format(index, 'b').zfill(self.no_data_bits)[::-1]
            )
            for data_index in range(0, self.no_data_bits):
                if (binary_representation[data_index] == '1'):
                    temp[data_index] = 1
                else:
                    temp[data_index] = 0
            self.decode_matrix[index] = self.encode(temp)

    @staticmethod
    def get_index_matrix(
            no_data_bits: int = 3,
            fold: int = 3,
            limit: int = 2) -> np.ndarray:
        r"""
        Get the index matrix for the given number of data bits, fold and
        limit.

        Args:
            no_data_bits :
                The number of data bits.
            fold :
                The number of folds.
            limit :
                The limit given by the how many points connecting to
                a specific data bit can a node control.

        Returns:
            index_matrix
                The index matrix. The shape of the array is (fold, no_nodes).
                The value on the (i, j) position represent the index in the
                hamming codeword of the j-th node for the i-th fold.
        """
        no_nodes: int = (2 ** no_data_bits - 1)
        matrix: np.ndarray = np.zeros(shape=(fold, no_nodes), dtype=int)
        # we return some hand-computed matrix depending on the value
        if (no_data_bits == 3 and fold == 3 and limit == 2):
            matrix = np.array([
                [1, 2, 3, 4, 5, 6, 7],
                [5, 6, 7, 1, 2, 3, 4],
                [6, 5, 4, 7, 3, 1, 2]])
        if (no_data_bits == 4 and fold == 3 and limit == 2):
            matrix = np.array([
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                [15, 4, 5, 3, 10, 11, 8, 14, 13, 12, 7, 2, 9, 6, 1],
                [8, 9, 10, 14, 3, 13, 11, 5, 6, 7, 4, 15, 2, 1, 12]
                ])
        if (no_data_bits == 4 and fold == 5 and limit == 3):
            matrix = np.array([
                [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
                [15, 4, 5, 3, 10, 11, 8, 14, 13, 12, 7, 2, 9, 6, 1],
                [8, 9, 10, 14, 3, 13, 11, 5, 6, 7, 4, 15, 2, 1, 12],
                [6, 15, 12, 9, 14, 5, 4, 3, 2, 1, 8, 11, 7, 13, 10],
                [12, 11, 8, 6, 13, 10, 15, 4, 3, 2, 1, 5, 14, 9, 7]
                ])
        return matrix

    def encode(self, data: np.ndarray) -> np.ndarray:
        r"""
        Encode the given data bits. It multiply data bits vector with the
        encode matrix in Z_{2}.

        Args:
            data :
                The data bits.

        Returns:
            encoded_data
                The encoded data bits.
        """
        return np.matmul(data, self.encode_matrix) % 2

    def differences(self, bits_array: np.ndarray) -> np.ndarray:
        r"""
        Compute the differences between the given bitstring and all the
        possible encoded values (use xor for this).

        Args:
            bits_array :
                The bitstring.

        Returns:
            differences :
                The differences between the given bitstring and all the
                possible encoded values. The shape of the array is
                (no_nodes+1, no_bits).
        """
        differences: np.ndarray = np.zeros(
            shape=(self.no_nodes+1, self.no_bits),
            dtype=int
        )
        for index in range(0, self.no_nodes+1):
            differences[index] = np.bitwise_xor(
                bits_array,
                self.decode_matrix[index]
            )
        return differences

    def decode(self, bits_array: np.ndarray) -> int:
        r"""
        To the decode a bitstring we find the closest encode value possible
        the distance is given by the number of differences between the two
        strings.

        Args:
            bits_array :
                The bitstring.

        Returns:
            index/data
                The index of the closest encode value possible or -1 if the
                distance is greater than the correcting distance for very
                possible encoded value.
        """
        distances: np.ndarray = np.zeros(shape=self.no_nodes+1, dtype=int)
        differences: np.ndarray = self.differences(bits_array=bits_array)
        for index in range(0, self.no_nodes+1):
            distances[index] = np.count_nonzero(differences[index])
        minIndex: int = np.argmin(distances)
        if (distances[minIndex] <= self.correcting_distance):
            return minIndex
        else:
            return -1
