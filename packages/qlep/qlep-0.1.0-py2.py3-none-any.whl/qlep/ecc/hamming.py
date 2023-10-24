r"""
.. _hamming:

The hamming module implements the Hamming codes when D=[n/2].
"""
# Hamming code
from __future__ import annotations
# qiskit module
import qiskit
# numpy module
import numpy as np
# lep base module
import qlep.core
# quantum proof of stake
import qlep.core.qpos
# logging
import logging
# override decorator
from typing_extensions import override

__all__ = ["HammingQLEP", "HammingStateGenerator", "HammingMaxD",
           "HammingLeaderElectionAlgorithm", "HammingMaliciousAttacker"]


class HammingQLEP(qlep.core.QuantumLeaderElectionProtocolwithPoS):
    r"""
    HammingQLEP class for Hamming codes superposition when D=[n/2]
    """

    no_data_bits: int = None
    r"""
    The number of data bits
    """

    def __init__(
        self,
        no_nodes: int,
        no_elections: int = 1,
        quantum_data_provider: qlep.core.QuantumDataProvider = None,
        committee: qlep.core.Committee = None,
        stake_vector: np.ndarray = None
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

        Raises:
            ValueError : If the number of nodes is not 2^x-1.
        """
        # call super class QuantumLeaderElectionProtocolwithPoS constructor
        super().__init__(
            election_type=qlep.core.ElectionType.HAMMING,
            no_nodes=no_nodes,
            no_elections=no_elections,
            quantum_data_provider=quantum_data_provider,
            committee=committee,
            stake_vector=stake_vector
        )
        self.no_data_bits: int = int(np.ceil(np.log2(self.quantum_no_nodes)))
        # verify the relation between quantum_no_nodes and no_data_bits
        if (2 ** self.no_data_bits) != (self.quantum_no_nodes + 1):
            logging.error("""[HammingQLEP] no_nodes/committee size
                          for hamming must be 2^n-1""")
            raise ValueError("committee size for hamming must be 2^x-1")

    @override
    def _get_stake_quantum_circuits(
            self,
            measure: bool = True,
            stake_vector: np.ndarray = None
    ) -> list[qiskit.QuantumCircuit]:
        return [HammingStateGenerator.get_quantum_circuits(
                    no_data_bits=self.no_data_bits,
                    stake_vector=stake_vector,
                    measure=measure
                )]

    @override
    def get_leader_election_algorithm(
            self
    ) -> qlep.core.LeaderElectionAlgorithm:
        return HammingLeaderElectionAlgorithm(no_data_bits=self.no_data_bits)

    @override
    def get_malicious_attacker(self) -> qlep.core.MaliciousAttacker:
        return HammingMaliciousAttacker(no_data_bits=self.no_data_bits)


class HammingStateGenerator:
    r"""
    HammingStateGenerator class for Hamming codes superposition when D=[n/2]
    """

    @staticmethod
    def get_quantum_circuits(
        no_data_bits: int,
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

        Returns:
            quantum_circuit
                The quantum circuit for the Hamming state for the given
                number of data bits.
        """
        # the number of qubits
        no_qubits = 2 ** no_data_bits - 1
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

        # extract the indexes for the data qubits
        data_indexes = []
        for index in range(0, no_qubits):
            binary_representation = (
                format(index+1, 'b') .zfill(no_data_bits)[::-1]
            )
            # if the bit is a parity qubit
            if binary_representation.count('1') == 1:
                data_indexes.append(index)

        # generate the superposition of the data qubits
        # if stake vector is given than use it
        if not (stake_vector is None):
            quantum_circuit.append(
                qlep.core.qpos.get_stake_gate(stake_vector),
                [quantum_registers[index] for index in data_indexes]
            )
        # The use of hadamard gates -> this generates also the |00...00>
        # it use less gates and more stable gates
        else:
            for index in data_indexes:
                quantum_circuit.h(quantum_registers[index])
        quantum_circuit.barrier()

        # create the connection between data qubits and parity qubits
        # using CNOT gates
        for index in range(0, no_qubits):
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
        if measure:
            quantum_circuit.measure(quantum_registers, classic_registers)
        return quantum_circuit


class HammingLeaderElectionAlgorithm(qlep.core.LeaderElectionAlgorithm):
    r"""
    HammingLeaderElectionAlgorithm class for Hamming codes when D=[n/2]
    """
    no_data_bits: int = None
    r"""
    The number of data bits
    """
    hamming_coder: HammingMaxD = None
    r"""
    The Hamming coder used for encoding and decoding.
    """
    def __init__(
        self,
        no_data_bits: int
    ) -> None:
        r"""
        Args:
            no_data_bits :
                The number of data bits.
        """
        super().__init__()
        self.no_data_bits: int = no_data_bits
        self.hamming_coder: HammingMaxD = HammingMaxD(
            no_data_bits=self.no_data_bits
        )

    @override
    def elect(self, data: np.ndarray) -> int:
        r"""
        Elect the leader from the given data bits.

        Args:
            data :
                The data bits. In this case the codeword bits. The shape of the
                array is (1, no_nodes).

        Returns:
            leader_index
                The index of the leader. If the leader index is -1 than the
                election is invalid. From the value of the index 1 is
                subtracted because the indexes of the nodes are from 0 to
                no_nodes - 1.
        """
        # decode the current value
        bits_array = np.copy(data)
        # onlty one round
        bits_array.shape = len(data[0, 0])
        leader_index = self.hamming_coder.decode(bits_array)
        if (leader_index != -1):
            leader_index = leader_index - 1
        return leader_index


class HammingMaliciousAttacker(qlep.core.MaliciousAttacker):
    r"""
    HammingMaliciousAttacker class for Hamming codes when D=[n/2]
    """
    no_data_bits: int = None
    r"""
    The number of data bits
    """
    hamming_coder: HammingMaxD = None
    r"""
    The Hamming coder used for encoding and decoding.
    """
    def __init__(
            self,
            no_data_bits: int
    ) -> None:
        r"""
        Args:
            no_data_bits :
                The number of data bits.
        """
        super().__init__()
        self.no_data_bits: int = no_data_bits
        self.hamming_coder: HammingMaxD = HammingMaxD(
            no_data_bits=self.no_data_bits
        )

    @override
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
        # get the malicious nodes
        malicious_nodes = [x for x in register_ids if x in malicious_ids]
        # if no malicious nodes under our control than return the given data
        if not malicious_nodes:
            return data
        # init return data
        modified_data = np.copy(data)

        # decode the current value
        bits_array = np.copy(data)
        # only one round
        bits_array.shape = len(register_ids)
        leader_index: int = self.hamming_coder.decode(bits_array)
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
            differences = self.hamming_coder.differences(bits_array)
            min_distance = len(register_ids)
            # compute the distance
            for index in range(0, len(register_ids)):
                distance = np.count_nonzero(differences[index+1])
                no_controled_nodes = 0
                # the no_nodes where the value can be changed to get the
                # proposed encoded value
                changeable_nodes = np.where(differences[index+1] == 1)[0]
                # how many no_nodes are controlled by the malicious attacker
                for node_index in changeable_nodes:
                    if register_ids[node_index] in malicious_ids:
                        no_controled_nodes = no_controled_nodes + 1
                # the new computed distance
                distance = distance - no_controled_nodes
                # if the node is malicious and the change can be done
                if register_ids[index] in malicious_ids:
                    if ((distance <= self.hamming_coder.correcting_distance)
                            and (distance < min_distance)):
                        change_leader = True
                        change_leader_index = index
                        min_distance = distance
                # if the election can be at least invalidate
                if (distance ==
                        (int(np.floor(self.hamming_coder.correcting_distance))
                         + 1)):
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
                temp = np.zeros(shape=self.no_data_bits)
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
                to_send = self.hamming_coder.encode(temp)
                # modify data for malicious no_nodes
                for node_index in range(0, len(register_ids)):
                    if register_ids[node_index] in malicious_ids:
                        modified_data[0, :, node_index] = to_send[node_index]
            # attack when it can make the index 0 of decoding == invalid
            # or maybe if nothings work just send zeroes to be
            # close to that value
            else:
                # the encoded value
                temp = np.zeros(shape=self.no_data_bits)
                to_send = self.hamming_coder.encode(temp)
                # modify data for malicious no_nodes
                for node_index in range(0, len(register_ids)):
                    if register_ids[node_index] in malicious_ids:
                        modified_data[0, :, node_index] = to_send[node_index]

        return modified_data


class HammingMaxD:
    r"""
    HammingMaxD class for Hamming codes when D=[n/2]. It can be used to encode
    and decode bit strings.

    The encode matrix is a k x n matrix where k is the number of data bits
    and n is the number of bits of the codewords. The decode matrix is a
    (n+1) x n matrix where n is the number of bits of the codewords. The
    encode matrix is used to encode the data bits. The decode matrix is
    used to decode the bitstring. The decode matrix contains all the
    possible encoded values for the data bits. The decode matrix is generated
    using the encode matrix. The encode matrix is generated using the binary
    representation of the index of the column. The decode matrix is generated
    using the binary representation of the index of the row.
    The codes are inspried by [1]_.

    References:
        .. [1] Hamming, Richard W. "Error detecting and error correcting codes." The Bell system technical journal 29.2 (1950): 147-160.
    """

    no_data_bits: int = None
    r"""
    The number of data bits
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
    def __init__(self, no_data_bits: int = 3) -> None:
        r"""
        Args:
            no_data_bits :
                The number of data bits.
        """
        # number of data bits m - data bits
        self.no_data_bits: int = no_data_bits
        # the necessary bits needed to archive D=[n/2] -- n = total bits
        self.no_bits: int = 2 ** self.no_data_bits - 1
        # compute distance between codewords
        self.distance: int = int(np.floor((self.no_bits + 1) / 2))
        # how many errors can it correct
        self.correcting_distance: float = (self.distance - 1) / 2
        # encode matrix
        # every column represent a bit in the final string
        # every row is a data bit
        # a bit is the value of xor of all data bits that have
        # the value 1 on its column
        # input value = 1 x m vector
        # encode matrix = m * n matrix
        # econde value = input value x encode matrix = 1 x n vector
        # the operations are done modulo 2 in Z_{2}
        self.encode_matrix: np.ndarray = np.zeros(
            shape=(self.no_data_bits, self.no_bits),
            dtype=int
        )
        for index in range(0, self.no_bits):
            binary_representation = (
                format(index+1, 'b').zfill(self.no_data_bits)[::-1]
            )
            for data_index in range(0, self.no_data_bits):
                if (binary_representation[data_index] == '1'):
                    self.encode_matrix[data_index, index] = 1
        # decode matrix
        # for every possible data bits we create a decode matrix which
        # contains all the encoded values possible values for
        # data bits = 2^{data bits}
        # we geenrate the vector by looking on the binary representation of
        # the value end than we used the encode matrix to encode the value
        # and store it in the dcode matrix
        self.decode_matrix: np.ndarray = np.zeros(
            shape=(self.no_bits+1, self.no_bits),
            dtype=int
        )
        temp: np.ndarray = np.zeros(shape=self.no_data_bits)
        for index in range(0, self.no_bits+1):
            binary_representation = (
                format(index, 'b').zfill(self.no_data_bits)[::-1]
            )
            for data_index in range(0, self.no_data_bits):
                if (binary_representation[data_index] == '1'):
                    temp[data_index] = 1
                else:
                    temp[data_index] = 0
            self.decode_matrix[index] = self.encode(temp)

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
            differences
                The differences between the given bitstring and all the
                possible encoded values. The shape of the array is
                (no_bits+1, no_bits).
        """
        differences: np.ndarray = np.zeros(
            shape=(self.no_bits+1, self.no_bits),
            dtype=int
        )
        for index in range(0, self.no_bits+1):
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
            index
                The index of the closest encode value possible or -1 if the
                distance is greater than the correcting distance for very
                possible encoded value.
        """
        distances: np.ndarray = np.zeros(shape=self.no_bits+1, dtype=int)
        differences: np.ndarray = self.differences(bits_array=bits_array)
        for index in range(0, self.no_bits+1):
            distances[index] = np.count_nonzero(differences[index])
        # the index of the minimum distance
        minIndex: int = np.argmin(distances)
        if (distances[minIndex] <= self.correcting_distance):
            return minIndex
        else:
            return -1
