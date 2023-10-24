"""
The base calsses and functions for core module of the
quantum leader election protocol module (lep).
"""
# future annotations
from __future__ import annotations
# numpy
import numpy as np
# logging
import logging
# typing
import typing
# for quantum computing code
import qiskit
# override decorator
from typing_extensions import override
# matplotlib
import matplotlib.pyplot as plt
# directory creation
import pathlib
# for testing qleps from files
import qlep


from qlep.core.electiontypes import ElectionType as ElectionType
from qlep.core.committeetypes import CommitteeType as CommitteeType
from qlep.core.committeetypes import Committee as Committee
from qlep.core.wcftypes import WCFElectionType as WCFElectionType
from qlep.core.providers import QuantumDataProvider as QuantumDataProvider


__all__ = ["MaliciousAttacker", "LeaderElectionAlgorithm",
           "QuantumLeaderElectionProtocol",
           "QuantumLeaderElectionProtocolwithPoS",
           "WeackCoinFlippingQLEP"
           ]


class MaliciousAttacker():
    r"""The malicious attacker for a quantum leader election protocol.

    The superclass for the malicious attacker for a quantum leader election
    protocol it is used to modify the data of the malicious nodes for the
    benefit of the attacker. Its internal state is reseted when the number
    of malicious nodes changes.
    """

    def attack(
        self,
        register_ids: np.ndarray,
        data: np.ndarray,
        malicious_ids: np.ndarray
    ) -> np.ndarray:
        r"""
        Return the data array after the attack of the malicious nodes.

        It use the position of the malicious nodes from malicious_ids
        in the register_ids to change the value of the data array in
        a way that is beneficial for the attacker.

        Args:
            register_ids :
                The ids of the nodes register in the quantum leader election.
                register_ids.shape = (no_nodes)
            data :
                The data array containing unchanged results of the nodes.
                data.shape = (no_quantum_circuits, no_rounds, no_nodes)
            malicious_ids :
                The ids of the malicious nodes. malicious_ids is a 1D array.

        Returns:
            malicious_data
                The data array after the attack of the malicious nodes.
                malicious_data.shape = (no_quantum_circuits, no_rounds,
                no_nodes)

        Note:
            Every quantum leader election protocol must define the attacker in
            the perfect informational model.
        """
        return data

    def reset(self) -> None:
        r"""
        Reset the malicious attacker to its initial state.
        """
        pass


class LeaderElectionAlgorithm():
    r"""The leader election algorithm for a quantum leader election protocol.

    The superclass for the leader election algorithm for a quantum leader
    election protocol. It defines the interface for the leader election
    algorithm.
    """

    def elect(
        self,
        data: np.ndarray
    ) -> int:
        r"""
        Return the leader index fo the election given the data array.

        It use the data array to determine the leader index of the election.
        The data can be the results of the nodes over multiple rounds of the
        election. The data array is a 2D array with the shape (no_rounds,
        no_nodes).

        Args:
            data :
                The data array containing the results of the nodes in the
                election. The data array is a 3D array with the shape
                (no_quantum_circuits, no_rounds, no_nodes).

        Returns:
            leader_index
                The index of the leader given the data array between 0 and
                no_nodes-1. It returns -1 if the election is invalid.
        """
        return -1


class QuantumLeaderElectionProtocol():
    r"""The quantum leader election protocol super class.

    The superclass for the quantum leader election protocol. It defines the
    interface for the quantum leader election protocol. It contains the basic
    attributes and methods for the quantum leader election protocol.

    Note:
        Every quantum leader election protocol must define the quantum circuit,
        the malicious attacker and the leader election algorithm. The protocol
        transmit only 1 qubit per node per round. The protocols are in the
        .. math:: \mathcal{R}(n, r, 1)
        where n is the number of nodes, r is the number of rounds and 1
        represent the number of bits of information send by every node
        per round.
    """

    election_type: ElectionType = None
    r"""
    The type of election in the quantum leader
    election protocol.
    """
    no_nodes: int = None
    r"""
    The number of nodes in the quantum leader election protocol.
    """
    no_elections: int = None
    r"""
    The number of elections in the quantum leader
    election protocol.
    """
    quantum_data_provider: QuantumDataProvider = None
    r"""
    The provider of quantum data for the experiments.
    """
    committee: Committee = None
    r"""
    The committe of the eleciton
    """
    quantum_no_nodes: int = no_nodes
    r"""
    The number of nodes in the quantum leader election circuit.
    """
    quantum_no_elections: int = no_elections
    r"""
    The number of elections in the quantum leader election circuit.
    """
    no_election_rounds: int = 1
    r"""
    The number of rounds in the quantum leader election circuit.
    """

    def __init__(
                self,
                election_type: ElectionType,
                no_nodes: int = 7,
                no_elections: int = 1,
                quantum_data_provider: QuantumDataProvider = None,
                committee: Committee = None,
    ) -> None:
        r"""The constructor of the quantum leader election protocol class.

        Takes the initial parameters and save the values as the attributes
        of the class. It also computes the number of nodes and elections
        for the quantum leader election circuit.

        Args:
            election_type :
                The type of election in the quantum leader election protocol.
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
        """
        self.election_type: ElectionType = election_type
        self.no_nodes: int = no_nodes
        self.no_elections: int = no_elections
        self.quantum_data_provider = quantum_data_provider
        self.no_election_rounds: int = 1

        if committee is None:
            self.committee = CommitteeType.ALL.get_committee(
                committee_size=no_nodes,
                no_nodes=no_nodes
            )
        else:
            self.committee = committee
        self.quantum_no_nodes: int = self.committee.committee_size

        # Depending on the committee type we compute the number of nodes and
        # elections for the quantum leader election circuit. We also compute
        # the number of committees the quantum leader election protocol has.
        # For the committee type ALL, the number of nodes and elections for
        # the quantum leader election circuit is the same as the number of
        # nodes and elections for the quantum leader election protocol.
        # For the committee type FIXED, the number of nodes for the quantum
        # leader election circuit is the same as the committee size. The number
        # of elections for the quantum leader election circuit is the number
        # of elections for the quantum leader election protocol multiplied by
        # the number of committees. The number of committees is the number of
        # nodes minus 1 divided by the committee size minus 1. The number of
        # committee rounds is the log base committee size of the number of
        # nodes.
        self.quantum_no_elections: int = (
            no_elections *
            self.committee.no_committees
        )

    def get_quantum_circuits(
            self,
            measure: bool = True
    ) -> list[qiskit.QuantumCircuit]:
        r"""
        Return the quantum circuit of the quantum leader election protocol.

        It returns the quantum circuit of the quantum leader election protocol.
        The quantum circuit is a qiskit.QuantumCircuit object. It can contains
        the measurement operation or not depending on the measure parameter.

        Args:
            measure :
                If the quantum circuit contains the measurement operations.
                When False, the quantum circuit is used for drawing.
                When True, the quantum circuit is used for running
                experiments on QPUs and simulators.

        Returns:
            quantum_circuits
                The quantum circuit of the quantum leader election protocol.

        """
        return None

    def get_malicious_attacker(self) -> MaliciousAttacker:
        r"""
        Return the malicious attacker of the quantum leader election protocol.

        It returns the malicious attacker of the quantum leader election
        protocol. The malicious attacker is a MaliciousAttacker object.
        Its role is to modify the data of the malicious nodes for the benefit
        of the attacker. It is used in the perfect informational model.

        Returns:
            malicious_attacker
                The malicious attacker of the quantum leader election protocol.

        """
        return None

    def get_leader_election_algorithm(self) -> LeaderElectionAlgorithm:
        r"""
        Return the leader election algorithm of the quantum leader election
        protocol.

        It returns the leader election algorithm of the quantum leader election
        protocol. The leader election algorithm is a LeaderElectionAlgorithm
        object. Its role is to determine the leader index of the election
        given the data array.

        Returns:
            leader_election_algorithm
                The leader election algorithm of the quantum leader election
                protocol.
        """
        return None

    def _get_election_name(self) -> str:
        r"""
        Return the name of the election type of the quantum
        leader election protocol.

        Returns:
            election_name
                The name of the election type of the quantum leader election
                protocol.
        """
        return self.election_type.name

    def get_latex_name(self) -> str:
        r"""
        Return the name of the quantum leader election protocol in latex
        format.

        Returns:
            latex_name
                The name of the quantum leader election protocol in
                latex format.
        """
        latex_name: str = (
            r'$\mathcal{R}_{QLE}^{' +
            r'\textrm{' +
            self._get_election_name() +
            r'}}(' +
            str(self.no_nodes) +
            r')' +
            self.committee.get_latex_name() +
            r'$ ' +
            self.quantum_data_provider.get_latex_name()
        )
        return latex_name

    def _get_quantum_name(self) -> str:
        r"""
        Return the name of the quantum related files.

        Returns:
            q_file_name
                The name of the quantum related files.

        Note:
            The quantum related files are the files related to the quantum
            leader election circuit experiments.
        """
        q_file_name: str = (
            self._get_election_name() +
            "_" +
            str(self.quantum_no_nodes) +
            "_" +
            self.quantum_data_provider.get_name() +
            "_" +
            str(self.quantum_no_elections)
        )
        return q_file_name

    def _get_simulation_name(self) -> str:
        r"""
        Return the name of the simulation name.

        Returns:
            simulation_name
                The name of the simulation.
        """
        simulation_name: str = (
            self._get_election_name() +
            "_" +
            str(self.no_nodes) +
            "_" +
            self.quantum_data_provider.get_name() +
            "_" +
            str(self.no_elections) +
            self.committee.get_name()
        )
        return simulation_name

    def get_quantum_job_file_name(
            self,
            quantum_job_directory: str = "jobs"
    ) -> str:
        r"""
        Return the name of the quantum job file.

        Args:
            quantum_job_directory :
                The name of the quantum job directory.

        Returns:
            quantum_job_file_name
                The name of the quantum job file.

        Note:
            The quantum job file is the file with the job details
            sended to the provider.
        """
        quantum_job_file_name: str = (
            quantum_job_directory +
            "/" +
            self._get_quantum_name() +
            ".npz"
        )
        return quantum_job_file_name

    def get_quantum_data_file_name(
            self,
            quantum_directory: str = "quantum"
    ) -> str:
        r"""
        Return the name of the quantum data file.

        Args:
            quantum_directory :
                The name of the quantum data directory.

        Returns:
            quantum_data_file_name
                The name of the quantum experiment file.

        Note:
            The quantum data file is the file with the
            results of the quantum leader election circuit experiments.
        """
        quantum_data_file_name: str = (
            quantum_directory +
            "/" +
            self._get_quantum_name() +
            ".npz"
        )
        return quantum_data_file_name

    def get_simulate_file_name(
            self,
            simulate_directory: str = "simulate"
    ) -> str:
        r"""
        Return the name of the simulation experiment file.

        Args:
            simulate_directory :
                The name of the simulation experiment directory.

        Returns:
            simulate_experiment_file_name
                The name of the simulation experiment file.

        Note:
            The simulation experiment file is the file with the results
            of the simulation experiments.
        """
        simulate_experiment_file_name: str = (
            simulate_directory +
            "/" +
            self._get_simulation_name() +
            ".npz"
        )
        return simulate_experiment_file_name

    def get_experiment_information(self) -> dict[str, typing.Any]:
        r"""
        Return the experiment info dictionary.

        It a good use to save the experiment information to a file.

        Returns:
            experiment_information
                The experiment info dictionary. It contains details about the
                quantum leader election protocol. The keys of the dictionary
                are: no_nodes, no_elections, election_type,
                quantum_data_provider, committee.
        """
        experiment_information: dict[str, typing.Any] = {
            "no_nodes": self.no_nodes,
            "no_elections": self.no_elections,
            "election_type": self.election_type,
            "quantum_data_provider": self.quantum_data_provider,
            "committee": self.committee
        }
        return experiment_information

    def compatible_QLEP(self, target: QuantumLeaderElectionProtocol) -> bool:
        r"""
        Return True if the target quantum leader election protocol is
        compatible with the current quantum leader election protocol.

        It checks if the target quantum leader election protocol is compatible
        with the current quantum leader election protocol. The target quantum
        leader election protocol is compatible with the current quantum leader
        election protocol if the election type is the same, the number of
        quantum nodes is the same, and the number of quantum elections is
        less or equal.

        Args:
            target :
                The target quantum leader election protocol.

        Returns:
            compatible
                True if the target quantum leader election protocol is
                compatible with the current quantum leader election protocol.
        """
        compatible: bool = True
        compatible = compatible & (self.election_type == target.election_type)
        compatible = compatible & (self.quantum_no_nodes ==
                                   target.quantum_no_nodes)
        compatible = compatible & (self.quantum_no_elections <=
                                   target.quantum_no_elections)
        return compatible

    # # # # # # # # # # # # #
    # GENERATE QUANTUM DATA #
    # # # # # # # # # # # # #

    def send_quantum_job(
            self,
            quantum_job_file_name: str = None
    ) -> (str, qiskit.providers.JobV1):
        r"""
        Send the quantum job to the provider.

        Args:
            quantum_job_file_name :
                The name of the quantum job file.
        """
        if quantum_job_file_name is None:
            quantum_job_file_name = self.get_quantum_job_file_name()
        job = self.quantum_data_provider.send_job(
            quantum_circuits=self.get_quantum_circuits(),
            shots=self.quantum_no_elections
        )
        pathlib.Path(quantum_job_file_name).parent.mkdir(
            parents=True,
            exist_ok=True
        )
        np.savez(
            file=quantum_job_file_name,
            experiment_information=self.get_experiment_information(),
            job_id=job.job_id()
        )
        return (quantum_job_file_name, job)

    def _shape_quantum_data(
            self,
            data: list[np.ndarray]
    ) -> np.ndarray:
        r"""
        Return the data array with the shape (quantum_no_elections,
        no_election_rounds, quantum_no_nodes).

        It reshape the data array from the shape (quantum_no_elections *
        no_election_rounds, quantum_no_nodes) to the shape
        (1, quantum_no_elections, no_election_rounds, quantum_no_nodes).

        Args:
            data :
                The data array containing the results of quantum experiments.
                data.shape = (quantum_no_elections * no_election_rounds,
                quantum_no_nodes)

        Returns:
            data
                The data array with the shape (1, quantum_no_elections,
                no_election_rounds, quantum_no_nodes)

        Note:
            The data array is a 2D array with the shape (quantum_no_elections *
            no_election_rounds, quantum_no_nodes). The data array is reshaped
            to a 4D array with the shape (quantum_no_elections,
            no_election_rounds, quantum_no_nodes).
        """
        no_quantum_circuits = len(data)
        for index in range(no_quantum_circuits):
            data[index].shape = (
                self.quantum_no_elections,
                self.no_election_rounds,
                self.quantum_no_nodes
            )
        quantum_data: np.ndarray = np.concatenate(data, axis=1)
        quantum_data.shape = (
            self.quantum_no_elections,
            no_quantum_circuits,
            self.no_election_rounds,
            self.quantum_no_nodes
        )
        return quantum_data

    def get_quantum_job_data(
            self,
            quantum_job_file_name: str = None,
            quantum_data_file_name: str = None,
            job: qiskit.providers.JobV1 = None
    ) -> str:
        r"""
        Get the quantum job data from the provider.

        Args:
            quantum_job_file_name :
                The name of the quantum job file.
            quantum_data_file_name :
                The name of the quantum data file.

        Raises:
            ValueError : quantum job file not compatible
        """
        if quantum_job_file_name is None:
            quantum_job_file_name = self.get_quantum_job_file_name()
        if quantum_data_file_name is None:
            quantum_data_file_name = self.get_quantum_data_file_name()

        # load the job
        np_data = np.load(quantum_job_file_name, allow_pickle=True)
        job_id = np_data["job_id"].item()
        experiment_information = np_data["experiment_information"].item()
        # verify if the qleps are compatible
        simulate_file_qlep: QuantumLeaderElectionProtocol = (
            qlep.qlep_from_dict(experiment_information=experiment_information)
        )
        compatible = self.compatible_QLEP(target=simulate_file_qlep)
        if not compatible:
            raise ValueError("quantum job file not compatible")

        # get the quantum data
        quantum_data = self.quantum_data_provider.get_job_result(
            job=job,
            job_id=job_id
        )
        # shape the results
        quantum_data = self._shape_quantum_data(data=quantum_data)
        # save the quantum data
        pathlib.Path(quantum_data_file_name).parent.mkdir(
            parents=True,
            exist_ok=True
        )
        np.savez(
            file=quantum_data_file_name,
            experiment_information=self.get_experiment_information(),
            quantum_data=quantum_data
        )
        return quantum_data_file_name

    def generate_quantum_data(
            self,
            quantum_job_file_name: str = None,
            quantum_data_file_name: str = None
    ) -> str:
        r"""
        Generate the quantum data from the provider.

        Args:
            quantum_job_file_name :
                The name of the quantum job file.
            quantum_data_file_name :
                The name of the quantum data file.
        """
        if quantum_job_file_name is None:
            quantum_job_file_name = self.get_quantum_job_file_name()
        if quantum_data_file_name is None:
            quantum_data_file_name = self.get_quantum_data_file_name()
        (_, job) = self.send_quantum_job(
            quantum_job_file_name=quantum_job_file_name
        )
        self.get_quantum_job_data(
            quantum_job_file_name=quantum_job_file_name,
            quantum_data_file_name=quantum_data_file_name,
            job=job
        )
        return quantum_data_file_name

    # # # # # # # # # # # # #
    # SIMULATE ELECTIONS    #
    # # # # # # # # # # # # #

    def _generate_malicious_ids(
            self,
            no_malicious_nodes: int,
            registers_ids: np.ndarray,
    ) -> np.ndarray:
        r"""
        Return the malicious ids.

        It returns the malicious ids. The malicious ids are the ids of the
        malicious nodes. The malicious nodes are the first no_malicious_nodes
        nodes.

        Args:
            no_malicious_nodes :
                The number of malicious nodes.
            registers_ids :
                The ids of the nodes.
        """
        malicious_ids: np.ndarray = np.arange(
            start=0,
            stop=no_malicious_nodes,
            step=1,
            dtype=int
        )
        return registers_ids[malicious_ids]

    def _generate_register_ids(
            self,
            ids: np.ndarray,
            shuffle: bool = True,
            register_seed: int = 0
    ) -> np.ndarray:
        r"""
        Return the register ids.

        It returns the register ids. The register ids are the ids of the nodes
        in the order for the elections.

        Args:
            ids :
                The ids of the nodes.
            shuffle :
                If the ids are shuffled before every election.
            register_seed :
                The seed used for the random number generator.

        Returns:
            register_ids
                The register ids. The register ids are the ids of the nodes
                in the order for the elections.
        """
        # setup the random seeed
        rs = np.random.RandomState(
            np.random.MT19937(
                np.random.SeedSequence(register_seed)
            )
        )
        shuffle_ids = np.copy(ids)
        # setup the order of the ids for every election
        register_ids = np.zeros(
            shape=(self.no_elections, self.no_nodes),
            dtype=int
        )
        for election_index in range(0, self.no_elections):
            if shuffle:
                rs.shuffle(shuffle_ids)
            register_ids[election_index] = np.copy(shuffle_ids)

        return register_ids

    def _sanitize_election_data(
            self,
            data: np.ndarray,
            register_ids: np.ndarray
    ) -> np.ndarray:
        r"""
        Return the sanitized election data.

        It returns the sanitized election data. The sanitized election data
        is the election data with 0s for the invalid ids.

        Args:
            data :
                The election data.
            register_ids :
                The ids of the nodes.

        Returns:
            sanitized_data
                The sanitized election data. The sanitized election data
                is the election data with 0s for the invalid ids.
        """
        # if the commitee ids are invalid try to
        # make zero the values
        sanitized_data: np.ndarray = np.copy(data)
        (no_quantum_circuits, no_election_rounds, no_nodes) = data.shape
        for node_index in range(0, no_nodes):
            if register_ids[node_index] == -1:
                sanitized_data[:, :, node_index] = 0
        return sanitized_data

    def _simulate_committees_election(
            self,
            register_ids: np.ndarray,
            malicious_ids: np.ndarray,
            quantum_data: np.ndarray,
            attacker: MaliciousAttacker,
            algorithm: LeaderElectionAlgorithm,
    ) -> int:
        r"""
        Simulate an election through committees.

        Args:
            register_ids :
                The ids of the nodes.
            malicious_ids :
                The ids of the malicious nodes.
            quantum_data :
                The quantum data.
            attacker :
                The malicious attacker.
            algorithm :
                The leader election algorithm.

        Returns:
            leader_id
                The leader id.
        """
        # the initial committees
        committees: np.ndarray = self.committee.get_initial_committees(
            register_ids=register_ids
        )
        committee_index: int = 0
        # go through every committee
        while committee_index < self.committee.no_committees:
            # starts a committee round
            committees_winners: list[int] = []
            # go through every commitee of that round
            while committee_index < len(committees):
                sanitized_data: np.ndarray = self._sanitize_election_data(
                    data=quantum_data[committee_index],
                    register_ids=committees[committee_index]
                )
                # attack the valid data
                malicious_data: np.ndarray = attacker.attack(
                    register_ids=committees[committee_index],
                    data=sanitized_data,
                    malicious_ids=malicious_ids
                )
                # elect the leader
                leader_index: int = algorithm.elect(
                    data=malicious_data
                )
                # if the leader index is invalid
                if ((leader_index < 0) or
                        (leader_index >= self.committee.committee_size)):
                    committees_winners.append(-1)
                else:
                    committees_winners.append(
                        committees[committee_index, leader_index]
                    )
                # go to the next committee
                committee_index += 1
            # update the committees
            committees = self.committee.update_committees(
                committees=committees,
                committees_winners=np.array(committees_winners)
            )
        leader_id: int = committees_winners[0]

        return leader_id

    def simulate_elections(
            self,
            quantum_data_file_name: str = None,
            simulate_file_name: str = None,
            shuffle: bool = True,
            register_seed: int = 0
    ) -> None:
        r"""
        Simulate the quantum leader election protocol.

        It simulates the quantum leader election protocol and saves the
        results to a file.

        Args:
            quantum_data_file_name :
                The file where the quantum experiment results are stored.
            simulate_file_name :
                The file where the simulation results will be stored.
            shuffle :
                If the ids are shuffled before every election.
            register_seed :
                The seed used for the random number generator.

        Raises:
            ValueError : If the quantum file is not compatible.
        """
        # load the simulation file
        if quantum_data_file_name is None:
            quantum_data_file_name = self.get_quantum_data_file_name()
        npdata = np.load(quantum_data_file_name, allow_pickle=True)
        # get the experiment information
        experiment_information = npdata["experiment_information"].item()
        # get the quantum elections results
        quantum_data = npdata["quantum_data"]
        # verify if the qleps are compatible
        quantum_file_qlep: QuantumLeaderElectionProtocol = (
            qlep.qlep_from_dict(experiment_information=experiment_information)
        )
        compatible = self.compatible_QLEP(target=quantum_file_qlep)
        if not compatible:
            raise ValueError("quantum file not compatible")

        # get the election algorithm
        election_algorithm: LeaderElectionAlgorithm = (
            self.get_leader_election_algorithm()
        )

        # every node has an id from 0 to no_nodes
        ids = np.arange(start=0, stop=self.no_nodes, step=1, dtype=int)
        # setup the order of the ids for every election
        register_ids = self._generate_register_ids(
            ids=ids,
            shuffle=shuffle,
            register_seed=register_seed
        )
        # the maximum number of malicious nodes
        max_no_malicious_nodes: int = int(np.floor(self.no_nodes/2.0))
        # -2 uninitialiased
        # -1 invalid
        # 0 to (no_nodes - 1) valid IDs
        leaders_ids: np.ndarray = -2 * np.ones(
            shape=(max_no_malicious_nodes+1, self.no_elections),
            dtype=int
        )
        elections_malicious_ids: list[np.ndarray] = []
        fair_indexes = -2 * np.ones(shape=self.no_elections, dtype=int)
        for no_malicious_nodes in range(0, max_no_malicious_nodes + 1):
            attacker: MaliciousAttacker = self.get_malicious_attacker()
            malicious_ids: np.ndarray = self._generate_malicious_ids(
                no_malicious_nodes=no_malicious_nodes,
                registers_ids=ids
            )
            elections_malicious_ids.append(malicious_ids)
            logging.info("[QLEP][Simulation] %s - %d/%d " % (
                self._get_election_name(), no_malicious_nodes,
                max_no_malicious_nodes
            ))
            for election_index in range(0, self.no_elections):
                leader_id: int = self._simulate_committees_election(
                    register_ids=register_ids[election_index],
                    malicious_ids=malicious_ids,
                    quantum_data=quantum_data[
                        (election_index *
                         self.committee.no_committees):
                        ((election_index+1) *
                         self.committee.no_committees)
                    ],
                    attacker=attacker,
                    algorithm=election_algorithm
                )
                # compute the fair index
                if no_malicious_nodes == 0:
                    found = np.where(register_ids[election_index] == leader_id)
                    if len(found) > 0 and len(found[0]) > 0:
                        fair_indexes[election_index] = found[0][0]
                    else:
                        fair_indexes[election_index] = -1
                leaders_ids[no_malicious_nodes, election_index] = leader_id
        # save the results
        # if the file does not exists create it
        if simulate_file_name is None:
            simulate_file_name = self.get_simulate_file_name()
        # create the directory if does not exists
        pathlib.Path(simulate_file_name).parent.mkdir(
            parents=True,
            exist_ok=True
        )
        # make the array savable for different version of numpy
        elections_malicious_ids = np.array(
            elections_malicious_ids,
            dtype=object
        )
        np.savez(
            file=simulate_file_name,
            leaders_ids=leaders_ids,
            register_ids=register_ids,
            fair_indexes=fair_indexes,
            quantum_data=quantum_data,
            elections_malicious_ids=elections_malicious_ids,
            experiment_information=self.get_experiment_information()
        )

    # # # # # # # # # # # # #
    # DRAW AND ANALYSE      #
    # # # # # # # # # # # # #

    def analyse_simulate_results(
            self,
            simulate_file_name: str = None
    ) -> dict[str, typing.Any]:
        r"""
        Return the analyse of the simulation experiments results.

        It loads the simulation file and analyse the results of the
        simulation experiments. It returns a dictionary with the following
        keys: winning_percentages, invalid_elections_percentages,
        fairvalue_PRA, fairvalue_PRV, max_bias, max_abs_bias,
        malicious_win_percentage, max_no_malicious_nodes,
        index_winning_percentage.

        Args:
            simulate_file_name :
                The name of the simulation experiment file.

        Returns:
            analyse_results
                The analyse of the simulation experiments results. It is a
                dictionary with the following keys: winning_percentages,
                invalid_elections_percentages, fairvalue_PRA, fairvalue_PRV,
                max_bias, max_abs_bias, malicious_win_percentage,
                max_no_malicious_nodes, index_winning_percentage.
        """
        # load the simulation file
        if simulate_file_name is None:
            simulate_file_name = self.get_simulate_file_name()
        npdata = np.load(simulate_file_name, allow_pickle=True)
        # get the experiment information
        experiment_information = npdata["experiment_information"].item()
        # verify if the qleps are compatible
        simulate_file_qlep: QuantumLeaderElectionProtocol = (
            qlep.qlep_from_dict(experiment_information=experiment_information)
        )
        compatible = self.compatible_QLEP(target=simulate_file_qlep)
        if not compatible:
            raise ValueError("simulation file not compatible")
        # get the quantum leader election results
        leaders_ids = npdata["leaders_ids"]
        # get the quantum leader no_elections results for
        # no malicious users
        fair_indexes = npdata["fair_indexes"]
        # malciious ids
        elections_malicious_ids = npdata["elections_malicious_ids"]
        # find the maximum malicious
        max_no_malicious_nodes: int = int(np.floor(self.no_nodes/2.0))
        max_no_malicious_nodes = len(leaders_ids) - 1
        # fair value
        fairvalue_PRA = 1.0/self.no_nodes
        # compute the winning percentage
        # the fair value with invalid elections
        winning_percentages = np.zeros(
            shape=(max_no_malicious_nodes+1, self.no_nodes),
            dtype=float
        )
        no_invalid_elections = np.zeros(
            shape=max_no_malicious_nodes+1,
            dtype=int
        )
        invalid_elections_percentages = np.zeros(
            shape=max_no_malicious_nodes+1,
            dtype=float
        )
        # get how many times every node has won
        # if the election are invalid how many of them are
        for no_malicious_nodes in range(0, max_no_malicious_nodes + 1):
            unique, count = np.unique(
                leaders_ids[no_malicious_nodes],
                return_counts=True
            )
            for jindex in range(0, len(unique)):
                if unique[jindex] == -1 or unique[jindex] >= self.no_nodes:
                    no_invalid_elections[no_malicious_nodes] += (
                        count[jindex]
                    )
                else:
                    winning_percentages[no_malicious_nodes][unique[jindex]] = (
                        count[jindex] / self.no_elections
                    )
        unique, count = np.unique(fair_indexes, return_counts=True)
        index_winning_percentage = np.zeros(shape=self.no_nodes, dtype=float)
        for jindex in range(0, len(unique)):
            if not (unique[jindex] == -1 or unique[jindex] >= self.no_nodes):
                index_winning_percentage[unique[jindex]] = (
                    count[jindex] / self.no_elections
                )
        # find out the total malicious winning percentage
        malicious_win_percentage = np.zeros(
                shape=max_no_malicious_nodes+1,
                dtype=float
        )

        for no_malicious_nodes in range(0, max_no_malicious_nodes + 1):
            malicious_ids = elections_malicious_ids[no_malicious_nodes]
            malicious_win_percentage[no_malicious_nodes] = (
                np.sum(
                    [winning_percentages[no_malicious_nodes][malicious_node]
                     for malicious_node in malicious_ids]
                )
            )
        # compute invaide elections percentage
        invalid_elections_percentages = (
            no_invalid_elections / self.no_elections
        )
        # the fair value without invalid elections
        fairvalue_PRV = (
            fairvalue_PRA *
            (self.no_elections-no_invalid_elections) /
            self.no_elections
        )
        # compute the the maximum bias for winning
        # if all bias than use np.abs before np.max
        max_bias = np.max(
            winning_percentages - fairvalue_PRA,
            axis=1
        )
        max_abs_bias = np.max(
            np.abs(winning_percentages - fairvalue_PRA),
            axis=1
        )

        return dict(
            winning_percentages=winning_percentages,
            invalid_elections_percentages=invalid_elections_percentages,
            fairvalue_PRA=fairvalue_PRA,
            fairvalue_PRV=fairvalue_PRV,
            max_bias=max_bias,
            max_abs_bias=max_abs_bias,
            malicious_win_percentage=malicious_win_percentage,
            max_no_malicious_nodes=max_no_malicious_nodes,
            index_winning_percentage=index_winning_percentage
        )

    def draw_quantum_circuits(
            self,
            draw_directory: str = "draw"
    ) -> None:
        r"""
        Draw the quantum circuit of the quantum leader election protocol.

        It draws the quantum circuit of the quantum leader election protocol
        and saves it to a file.

        Args:
            draw_directory :
                The name of the draw directory.

        Note:
            The quantum circuit is saved to a file with the name
            quantum_circuit.pdf.
        """
        # get the quantum circuits
        quantum_circuits: list[qiskit.QuantumCircuit] = (
            self.get_quantum_circuits(measure=False)
        )
        # the raget basis for drawing
        # target_basis_gates = ['rx', 'ry', 'rz', 'h', 'cx', 'cz', 'x']
        # target_basis_gates = ['rx', 'ry', 'rz', 'h', 'cx', 'cz']
        # target_basis_gates = ['x', 'h', 'cx', 'F']
        # target_basis_gates = ['rx', 'ry', 'rz', 'h', 'cx', 'x']
        # the drawing style
        style = {
            'name': 'bw'
        }
        # create the directory
        pathlib.Path(draw_directory).mkdir(parents=True, exist_ok=True)
        # go through qunatum circuits and draw them
        for circuit_index in range(0, len(quantum_circuits)):
            # draw the quantum circuit
            qiskit.transpile(
                quantum_circuits[circuit_index],
                # basis_gates=target_basis_gates,
                optimization_level=0
            ).draw(
                    output='latex',
                    filename=(
                        draw_directory +
                        "/" +
                        self._get_quantum_name() +
                        "_circuit_" +
                        str(circuit_index) +
                        ".pdf"
                    ),
                    fold=-1,
                    plot_barriers=False,
                    initial_state=True,
                    scale=1,
                    with_layout=False,
                    justify='left',
                    style=style
            )

    def draw_boxplot(
            self,
            simulate_file_name: str = None,
            draw_directory: str = None
    ) -> None:
        r"""
        Draw the boxplot of the election results when the number of malicious
        nodes increase.

        Args:
            simulate_file_name :
                The file where the simulation results are stored.
            draw_directory :
                The directory where the figures will be stored.

        Raises:
            ValueError : If the simulation file is not compatible.
        """
        # setup latex and font size
        plt.rcParams['text.usetex'] = True
        plt.rcParams.update({'font.size': 22})
        # malicious winning percentage figure
        figure_boxplot, ax_boxplot = plt.subplots(figsize=(15, 15))

        # initial axis setup
        my_xlabel = r'Number of malicious nodes $ f = | \mathcal{M} | $'
        my_ylabel = r'\% of elections'

        analyse_results = self.analyse_simulate_results(
            simulate_file_name=simulate_file_name
        )

        max_no_malicious_nodes = analyse_results["max_no_malicious_nodes"]
        winning_percentages = analyse_results["winning_percentages"]
        fairvalue_PRA = analyse_results["fairvalue_PRA"]
        fairvalue_PRV = analyse_results["fairvalue_PRV"]
        max_bias = analyse_results["max_bias"]
        invalid_elections_percentages = (
            analyse_results["invalid_elections_percentages"]
        )

        # setup x axis
        ax_boxplot.set_xlabel(my_xlabel)
        ax_boxplot.set_xticklabels(range(0, max_no_malicious_nodes + 1))
        # draw the box plots
        ax_boxplot.boxplot(
            [winning_percentages[no_malicious_nodes]
             for no_malicious_nodes in range(0, max_no_malicious_nodes + 1)
             ],
            showfliers=False)
        # draw the fair PR line
        fairline_PRA = ax_boxplot.hlines(
            y=fairvalue_PRA,
            xmin=0.5,
            xmax=max_no_malicious_nodes+1+0.5,
            label=r'Fair $ Pr[L^{G}=P_{i}] $',
            linestyles='dashed',
            colors='blue',
            alpha=0.6,
            lw=2
        )

        # create deviation for no_nodes to be plot
        xdeviation = np.linspace(start=-0.25, stop=0.25, num=self.no_nodes)
        # setup the the y axis
        max_y_value = np.max([0.4, np.max(winning_percentages)])
        ax_boxplot.set_ylim(top=max_y_value)
        my_yticks = np.linspace(start=0, stop=max_y_value, num=11)
        # setup y axis labels
        ax_boxplot.set_ylabel(my_ylabel)
        ax_boxplot.set_yticks(my_yticks)
        ax_boxplot.grid(linestyle='--', axis='y')

        # plot the no_nodes values and the maximum positive bias
        for no_malicious_nodes in range(0, max_no_malicious_nodes + 1):
            if (no_malicious_nodes > 0):
                malicious_nodes_x = (
                    (no_malicious_nodes+1) *
                    np.ones(shape=no_malicious_nodes, dtype=int) +
                    xdeviation[0:no_malicious_nodes]
                )
                malicious_nodes_y = (
                    winning_percentages[no_malicious_nodes][
                        0:no_malicious_nodes]
                )
                malicous_nodes = ax_boxplot.scatter(
                    x=malicious_nodes_x,
                    y=malicious_nodes_y,
                    marker='v',
                    color='red',
                    alpha=0.7,
                    label=r'Malicious Node $ P_{i} \in \mathcal{M} $'
                )
            honest_nodes_x = (
                (no_malicious_nodes+1) *
                np.ones(
                    shape=self.no_nodes-no_malicious_nodes,
                    dtype=int
                ) +
                xdeviation[no_malicious_nodes:]
            )
            honest_nodes_y = (
                winning_percentages[no_malicious_nodes][
                    no_malicious_nodes:]
            )
            honest_nodes = ax_boxplot.scatter(
                x=honest_nodes_x,
                y=honest_nodes_y,
                marker='P',
                color='green',
                alpha=0.7,
                label=r'Honest Node $ P_{i} \in \mathcal{H} $'
            )
            bias_nodes = ax_boxplot.scatter(
                x=no_malicious_nodes+1,
                y=max_bias[no_malicious_nodes],
                marker='x',
                color='orange',
                alpha=1,
                label=r'$ MAX(\varepsilon_{i}) $'
            )
            invalid_election_nodes = ax_boxplot.scatter(
                x=no_malicious_nodes+1,
                y=invalid_elections_percentages[no_malicious_nodes],
                marker='o',
                color='red',
                alpha=1,
                label=r'$  Pr[L^{G}=\emptyset] $'
            )
            # draw the fair PRV line
            fairlines_PRV = ax_boxplot.hlines(
                y=fairvalue_PRV[no_malicious_nodes],
                xmin=no_malicious_nodes+1-0.25,
                xmax=no_malicious_nodes+1+0.25,
                label=r'Fair $ Pr^{V}[L^{G}=P_{i}] $',
                linestyles='dotted',
                colors='red',
                alpha=0.6,
                lw=4
            )

        # add legend
        ax_boxplot.legend(
            handles=[malicous_nodes, honest_nodes, bias_nodes,
                     fairline_PRA, fairlines_PRV, invalid_election_nodes],
            loc="upper left",
            prop={'size': 24}
        )
        # create the directory
        pathlib.Path(draw_directory).mkdir(parents=True, exist_ok=True)
        figure_boxplot.savefig(
            draw_directory +
            "/" +
            self._get_simulation_name() +
            "_boxplot.pdf",
            format='pdf',
            dpi=1200,
            bbox_inches='tight'
        )
        # close the figure to save space
        plt.close(figure_boxplot)

    def _get_marker_fill_style(self) -> str:
        r"""
        Return the marker fill style depending on the provider.

        Returns:
            marker_fill_style
                The marker fill style depending on the provider.
        """
        return self.quantum_data_provider.provider.get_marker_fill_style()

    def _get_marker_style(self) -> str:
        r"""
        Return the marker style depending on the election type.

        Returns:
            marker_style
                The marker style depending on the election type.
        """
        return self.election_type.get_marker_style()

    def _get_marker_size(self) -> int:
        r"""
        Return the marker size depending on the committee size.

        Returns:
            marker_size
        """
        min_marker_size: int = 18
        max_marker_size: int = 28
        markerSize: int = int(
            np.ceil(
                min_marker_size +
                (max_marker_size-min_marker_size) *
                (self.committee.committee_size - 7) /
                float(128 - 7)
            )
        )
        return markerSize

    def _get_line_style(self) -> str:
        r"""
        Return the line style depending on the backend.
        - : for teoretical
        -- : for simulation
        : : for QPU

        Returns:
            line_style
                The line style depending on the backend.
        """
        return self.quantum_data_provider.get_line_style()

    def _get_line_width(self) -> float:
        r"""
        Return the line width depending on the nuber of nodes.

        Returns:
            line_width
                The line width depending on the nodes.
        """
        min_line_width: float = 2
        max_line_width: float = 4
        line_width: float = (
            min_line_width +
            (max_line_width - min_line_width) *
            (self.no_nodes - 7) /
            float(256 - 7)
        )
        return line_width

    def get_plot_style(self) -> dict[str, typing.Any]:
        r"""
        Return the marker style of the QLEP.
        marker depends on election type
        fillstyle depends on provider
        linestyle depends on backend
        markersize depends on committee size
        lw depends on number of nodes

        Returns:
            marker_style
                The marker style of the QLEP. It is a dictionary with the
                following keys: marker, fillstyle, linestyle, lw,
                markerfacecolor, markeredgecolor, markerfacecoloralt,
                markersize, label.
        """
        plot_style = dict(
            marker=self._get_marker_style(),
            fillstyle=self._get_marker_fill_style(),
            linestyle=self._get_line_style(),
            markersize=self._get_marker_size(),
            linewidth=self._get_line_width(),
            # color='darkgrey',
            markerfacecolor='black',
            markerfacecoloralt='white',
            markeredgecolor='black',
            label=self.get_latex_name()
        )
        return plot_style


class QuantumLeaderElectionProtocolwithPoS(QuantumLeaderElectionProtocol):
    r"""
    The quantum leader election protocol with proof of stake.

    The quantum leader election protocol with proof of stake. It is a
    subclass of the quantum leader election protocol. It contains the
    attributes and methods for the quantum leader election protocol with
    proof of stake.
    """

    use_stake: bool = False
    r"""
    If the quantum leader election protocol uses proof of stake.
    """
    stake_vector: np.ndarray = None
    r"""
    The stake vector of the nodes in the
    quantum leader election protocol. The stake vector is a 1D array with the
    shape (no_nodes).
    """

    def __init__(
            self,
            election_type: ElectionType,
            no_nodes: int = 7,
            no_elections: int = 1,
            quantum_data_provider: QuantumDataProvider = None,
            committee: Committee = None,
            stake_vector: np.ndarray = None
    ) -> None:
        r"""
        The constructor of the quantum leader election protocol with proof of
        stake class.

        Takes the same parameters as QuantumLeaderElectionProtocol class and
        adds the stake vector parameter. It also verifies if the stake vector
        is valid. It initializes the use_stake attribute with True,
        only if the stake vector is valid.

        Args:
            election_type :
                The type of election in the quantum leader election protocol.
            no_nodes :
                The number of nodes in the quantum leader election protocol.
            no_elections :
                The number of elections in the quantum leader election
                protocol.
            quantum_data_provider :
                The quantum data provider of the quantum leader election
            committee :
                The committee of the quantum leader election protocol.
            stake_vector :
                The stake vector of the nodes in the quantum leader election
                protocol. The stake vector is a 1D array with the shape
                (no_nodes).

        Raises:
            ValueError : If the stake vector is not valid.
        """
        # call super class QuantumLeaderElectionProtocol constructor
        super().__init__(
            election_type=election_type,
            no_nodes=no_nodes,
            no_elections=no_elections,
            quantum_data_provider=quantum_data_provider,
            committee=committee)
        # verify if the stake vector is valid
        self.stake_vector: np.ndarray = stake_vector
        self.use_stake: bool = False
        if self.stake_vector is None:
            self.use_stake = False
        else:
            self.use_stake = True
            if self.stake_vector.shape != (no_nodes,):
                logging.error("""[QuantumLeaderElectionProtocolwithPoS]
                              wrong stake vector shape""")
                raise ValueError("stake vector shape does not match nodes")

    @override
    def get_latex_name(self) -> str:
        # add PoS to the latex name if use_stake is True
        return super().get_latex_name() + (r" PoS" if self.use_stake else "")

    @override
    def _get_quantum_name(self) -> str:
        # add PoS to the quantum related files if use_stake is True
        return (
            super()._get_quantum_name() +
            (r"_PoS" if self.use_stake else "")
        )

    @override
    def _get_simulation_name(self) -> str:
        # add PoS to the simulation related files if use_stake is True
        return (
            super()._get_simulation_name() +
            (r"_PoS" if self.use_stake else "")
        )

    @override
    def get_experiment_information(self) -> dict[str, typing.Any]:
        # add use_stake and stake_vector to the experiment info dictionary
        experiment_information: dict[str, typing.Any] = (
            super().get_experiment_information()
        )
        experiment_information["use_stake"] = self.use_stake
        experiment_information["stake_vector"] = self.stake_vector
        return experiment_information

    @override
    def compatible_QLEP(self, target: QuantumLeaderElectionProtocol) -> bool:
        r"""
        Return True if the target quantum leader election protocol is
        compatible with the current quantum leader election protocol.

        It checks if the target quantum leader election protocol is compatible
        with the current quantum leader election protocol. The target quantum
        leader election protocol is compatible with the current quantum leader
        election protocol if the election type is the same, the number of
        quantum nodes is the same, the number of quantum elections is
        less or equal, and the use_stake is the same. If the use_stake is
        True, the stake_vector must be the same.

        Args:
            target: The target quantum leader election protocol.

        Returns:
            compatible
                True if the target quantum leader election protocol is
                compatible with the current quantum leader election protocol.
        """
        compatible: bool = super().compatible_QLEP(target)
        if self.use_stake:
            if isinstance(target, QuantumLeaderElectionProtocolwithPoS):
                compatible = (
                    compatible and
                    np.all(
                        self.stake_vector == target.stake_vector
                    )
                )
            else:
                compatible = False
        return compatible

    def _get_stake_quantum_circuits(
        self,
        measure: bool = True,
        stake_vector: np.ndarray = None
    ) -> list[qiskit.QuantumCircuit]:
        raise NotImplementedError

    @override
    def get_quantum_circuits(
        self,
        measure: bool = True
    ) -> list[qiskit.QuantumCircuit]:
        return self._get_stake_quantum_circuits(
            measure=measure,
            stake_vector=self.stake_vector
        )

    @override
    def generate_quantum_data(
            self,
            quantum_job_file_name: str = None,
            quantum_data_file_name: str = None
    ) -> str:
        r"""
        Generate the quantum data from the provider.

        Args:
            quantum_job_file_name :
                The name of the quantum job file.
            quantum_data_file_name :
                The name of the quantum data file.
        """
        if self.use_stake:
            if quantum_data_file_name is None:
                quantum_data_file_name = self.get_quantum_data_file_name()
            # save the quantum data
            pathlib.Path(quantum_data_file_name).parent.mkdir(
                parents=True,
                exist_ok=True
            )
            np.savez(
                file=quantum_data_file_name,
                experiment_information=self.get_experiment_information(),
                quantum_data=None
            )
            return quantum_data_file_name
        else:
            return super().generate_quantum_data(
                quantum_job_file_name=quantum_job_file_name,
                quantum_data_file_name=quantum_data_file_name
            )
    # # # # # # # # # # # # #
    # SIMULATE ELECTIONS    #
    # # # # # # # # # # # # #

    def _sanitize_stake_data(
            self,
            register_ids: np.ndarray
    ) -> np.ndarray:
        r"""
        Return the sanitized stake data.

        Args:
            register_ids :
                The ids of the nodes.

        Returns:
            sanitized_stake_data
                The sanitized stake data. The sanitized stake data
                is the stake data with 0s for the invalid ids.
        """
        # if the commitee ids are invalid try to
        # make zero the values
        sanitized_stake_data: np.ndarray = np.array(
            [self.stake_vector[rid] if rid >= 0 else 0
             for rid in register_ids]
        )
        if np.all(sanitized_stake_data == 0):
            sanitized_stake_data = np.ones(shape=register_ids.shape, dtype='f')
        if np.linalg.norm(sanitized_stake_data) < 0.00001:
            print("A crapat")
            print(register_ids)
            print(sanitized_stake_data)
            print(sanitized_stake_data == 0)
            print(np.all(sanitized_stake_data == 0))
            raise ValueError("0 division")
            # stake committee
            # a = ids
            # b = stake
            # a.shape(n_com, c_size)
            # b.shape(n_com, c_size)
            # d = np.concatenate([a,b], axis=1)
            # d.shape(n_com, 2, c_size)
        return sanitized_stake_data

    def _shape_stake_quantum_data(
            self,
            data: list[np.ndarray]
    ) -> np.ndarray:
        r"""
        Return the data array with the shape (1,
        no_election_rounds, quantum_no_nodes).

        It reshape the data array from the shape (1 *
        no_election_rounds, quantum_no_nodes) to the shape
        (1, 1, no_election_rounds, quantum_no_nodes).

        Args:
            data :
                The data array containing the results of quantum experiments.
                data.shape = (1 * no_election_rounds,
                quantum_no_nodes)

        Returns:
            data
                The data array with the shape (1, 1,
                no_election_rounds, quantum_no_nodes)

        Note:
            The data array is a 2D array with the shape (1 *
            no_election_rounds, quantum_no_nodes). The data array is reshaped
            to a 4D array with the shape (1,
            no_election_rounds, quantum_no_nodes).
        """
        no_quantum_circuits = len(data)
        for index in range(no_quantum_circuits):
            data[index].shape = (
                1,
                self.no_election_rounds,
                self.quantum_no_nodes
            )
        quantum_data: np.ndarray = np.concatenate(data, axis=1)
        quantum_data.shape = (
            1,
            no_quantum_circuits,
            self.no_election_rounds,
            self.quantum_no_nodes
        )
        return quantum_data

    def _simulate_stake_committees_election(
            self,
            register_ids: np.ndarray,
            stake_vector: np.ndarray,
            malicious_ids: np.ndarray,
            attacker: MaliciousAttacker,
            algorithm: LeaderElectionAlgorithm,
    ) -> int:
        r"""
        Simulate an election through committees.

        Args:
            register_ids :
                The ids of the nodes.
            malicious_ids :
                The ids of the malicious nodes.
            attacker :
                The malicious attacker.
            algorithm :
                The leader election algorithm.

        Returns:
            leader_id
                The leader id.
        """
        # the initial committees
        committees: np.ndarray = self.committee.get_initial_stake_committees(
            register_ids=register_ids,
            stake_vector=stake_vector
        )
        committee_index: int = 0
        # go through every committee
        while committee_index < self.committee.no_committees:
            # starts a committee round
            committees_winners: list[tuple[int, float]] = []
            # go through every commitee of that round
            while committee_index < len(committees):
                committee_circuits = self._get_stake_quantum_circuits(
                    stake_vector=committees[committee_index][1]
                )
                quantum_data_list = self.quantum_data_provider.run_stake(
                    quantum_circuits=committee_circuits
                )
                quantum_data = self._shape_stake_quantum_data(
                    data=quantum_data_list
                )
                sanitized_data: np.ndarray = self._sanitize_election_data(
                    data=quantum_data[0],
                    register_ids=committees[committee_index][0]
                )
                # attack the valid data
                malicious_data: np.ndarray = attacker.attack(
                    register_ids=committees[committee_index][0],
                    data=sanitized_data,
                    malicious_ids=malicious_ids
                )
                # elect the leader
                leader_index: int = algorithm.elect(
                    data=malicious_data
                )
                # compute the new leader stake
                leader_stake: float = np.sum(
                    committees[committee_index][1]
                )
                # if the leader index is invalid
                if ((leader_index < 0) or
                        (leader_index >= self.committee.committee_size)):
                    committees_winners.append((-1, leader_stake))
                else:
                    committees_winners.append(
                        (committees[committee_index, 0, leader_index],
                         leader_stake)
                    )
                # go to the next committee
                committee_index += 1
            # update the committees
            committees = self.committee.update_stake_committees(
                committees=committees,
                committees_winners=committees_winners
            )
        leader_id: int = committees_winners[0][0]

        return leader_id

    @override
    def simulate_elections(
            self,
            quantum_data_file_name: str = None,
            simulate_file_name: str = None,
            shuffle: bool = True,
            register_seed: int = 0
    ) -> None:
        r"""
        Simulate the quantum leader election protocol.

        It simulates the quantum leader election protocol and saves the
        results to a file.

        Args:
            quantum_data_file_name :
                The file where the quantum experiment results are stored.
            simulate_file_name :
                The file where the simulation results will be stored.
            shuffle :
                If the ids are shuffled before every election.
            register_seed :
                The seed used for the random number generator.

        Raises:
            ValueError : If the quantum file is not compatible.
        """
        if self.use_stake is False:
            super().simulate_elections(
                quantum_data_file_name=quantum_data_file_name,
                simulate_file_name=simulate_file_name,
                shuffle=shuffle,
                register_seed=register_seed
            )
            return None

        # get the election algorithm
        election_algorithm: LeaderElectionAlgorithm = (
            self.get_leader_election_algorithm()
        )

        # every node has an id from 0 to no_nodes
        ids = np.arange(start=0, stop=self.no_nodes, step=1, dtype=int)
        # setup the order of the ids for every election
        register_ids = self._generate_register_ids(
            ids=ids,
            shuffle=shuffle,
            register_seed=register_seed
        )
        # the maximum number of malicious nodes
        max_no_malicious_nodes: int = int(np.floor(self.no_nodes/2.0))
        # for POS is a TODO: the malicious nodes
        max_no_malicious_nodes = 0
        # -2 uninitialiased
        # -1 invalid
        # 0 to (no_nodes - 1) valid IDs
        leaders_ids: np.ndarray = -2 * np.ones(
            shape=(max_no_malicious_nodes+1, self.no_elections),
            dtype=int
        )
        elections_malicious_ids: list[np.ndarray] = []
        fair_indexes = -2 * np.ones(shape=self.no_elections, dtype=int)
        for no_malicious_nodes in range(0, max_no_malicious_nodes + 1):
            attacker: MaliciousAttacker = self.get_malicious_attacker()
            malicious_ids: np.ndarray = self._generate_malicious_ids(
                no_malicious_nodes=no_malicious_nodes,
                registers_ids=ids
            )
            elections_malicious_ids.append(malicious_ids)
            logging.info("[QLEP][Simulation] %s - %d/%d " % (
                self._get_election_name(), no_malicious_nodes,
                max_no_malicious_nodes
            ))
            for election_index in range(0, self.no_elections):
                logging.info("[QLEP][Simulation] %s - %d/%d - %d/%d " % (
                    self._get_election_name(), no_malicious_nodes,
                    max_no_malicious_nodes, election_index,
                    self.no_elections
                ))
                leader_id: int = self._simulate_stake_committees_election(
                    register_ids=register_ids[election_index],
                    stake_vector=np.array(
                        [self.stake_vector[id]
                         for id in register_ids[election_index]]
                    ),
                    malicious_ids=malicious_ids,
                    attacker=attacker,
                    algorithm=election_algorithm
                )
                # compute the fair index
                if no_malicious_nodes == 0:
                    found = np.where(register_ids[election_index] == leader_id)
                    if len(found) > 0 and len(found[0]) > 0:
                        fair_indexes[election_index] = found[0][0]
                    else:
                        fair_indexes[election_index] = -1
                leaders_ids[no_malicious_nodes, election_index] = leader_id
        # save the results
        # if the file does not exists create it
        if simulate_file_name is None:
            simulate_file_name = self.get_simulate_file_name()
        # create the directory if does not exists
        pathlib.Path(simulate_file_name).parent.mkdir(
            parents=True,
            exist_ok=True
        )
        np.savez(
            file=simulate_file_name,
            leaders_ids=leaders_ids,
            register_ids=register_ids,
            fair_indexes=fair_indexes,
            quantum_data=None,
            elections_malicious_ids=elections_malicious_ids,
            experiment_information=self.get_experiment_information()
        )

    # # # # # # # # # # # # #
    # DRAW AND ANALYSE      #
    # # # # # # # # # # # # #

    @override
    def analyse_simulate_results(
            self,
            simulate_file_name: str = None
    ) -> dict[str, typing.Any]:
        analyse_results = super().analyse_simulate_results(
            simulate_file_name=simulate_file_name
        )
        if self.use_stake:
            if simulate_file_name is None:
                simulate_file_name = self.get_simulate_file_name()
            npdata = np.load(simulate_file_name, allow_pickle=True)
            analyse_results["stake_vector"] =\
                npdata["experiment_information"].item()["stake_vector"]
        return analyse_results

    def get_d_stake_cdf_file_name(self) -> str:
        r"""
        """
        return self._get_simulation_name() + "_stake_cdf.pdf"

    def draw_stake_barplot(
        self,
        simulate_file_name: str = None,
        draw_directory: str = None
    ) -> None:
        r"""
        Draw the boxplot of the election results when the number of malicious
        nodes increase.

        Args:
            simulate_file_name :
                The file where the simulation results are stored.
            draw_directory :
                The directory where the figures will be stored.

        Raises:
            ValueError : If the simulation file is not compatible.
        """
        # setup latex and font size
        plt.rcParams['text.usetex'] = True
        plt.rcParams.update({'font.size': 22})
        # malicious winning percentage figure
        figure_barplot, ax_barplot = plt.subplots(figsize=(15, 10))

        # initial axis setup
        my_xlabel = r'Nodes $ P_{i} $'
        my_ylabel = r'\% of total stake/elections'

        analyse_results = self.analyse_simulate_results(
            simulate_file_name=simulate_file_name
        )

        winning_percentages = analyse_results["winning_percentages"]
        no_nodes = len(winning_percentages[0])

        # the stake vector
        stake_vector = analyse_results["stake_vector"]
        total_stake = np.sum(stake_vector)
        stake_vector = stake_vector/total_stake

        xticks = np.arange(no_nodes)
        xticklabels = [r'$ P_{%d} $' % i
                       if (i in [0, no_nodes-1, int(no_nodes/2)])
                       else ""
                       for i in xticks]
        width = 0.25

        # setup x axis
        ax_barplot.set_xlabel(my_xlabel)
        ax_barplot.set_xticks(
            xticks + width,
            xticklabels,
        )
        #    fontsize=10
        # ax_barplot.set_xticks(xticks + width)
        # setup y axis
        ax_barplot.set_ylabel(my_ylabel)
        max_y_value = np.round(
            np.max(
                [np.max(winning_percentages[0]), np.max(stake_vector)]
            ),
            decimals=2
        ) + 0.01
        ax_barplot.set_ylim(top=max_y_value)
        my_yticks = np.linspace(start=0, stop=max_y_value, num=11)
        # setup y axis labels
        ax_barplot.set_yticks(my_yticks)
        ax_barplot.grid(linestyle='--', axis='y')

        stake_bars = ax_barplot.bar(
            x=xticks+width/2,
            height=stake_vector,
            width=width,
            label=r'Stake',
            edgecolor='black',
            hatch="/",
            color='white'
        )
        winning_bars = ax_barplot.bar(
            x=xticks+width+width/2,
            height=winning_percentages[0],
            width=width,
            label=r'Won elections',
            edgecolor='black',
            hatch="--",
            color='white'
        )

        # add legend
        ax_barplot.legend(
            handles=[stake_bars, winning_bars],
            loc="upper left",
            prop={'size': 24}
        )
        # create the directory
        pathlib.Path(draw_directory).mkdir(parents=True, exist_ok=True)
        figure_barplot.savefig(
            draw_directory +
            "/" +
            self._get_simulation_name() +
            "_stake_barplot.pdf",
            format='pdf',
            dpi=1200,
            bbox_inches='tight'
        )
        # close the figure to save space
        plt.close(figure_barplot)

    def draw_stake_plot(
        self,
        simulate_file_name: str = None,
        draw_directory: str = None
    ) -> None:
        r"""
        Draw the boxplot of the election results when the number of malicious
        nodes increase.

        Args:
            simulate_file_name :
                The file where the simulation results are stored.
            draw_directory :
                The directory where the figures will be stored.

        Raises:
            ValueError : If the simulation file is not compatible.
        """
        # setup latex and font size
        plt.rcParams['text.usetex'] = True
        plt.rcParams.update({'font.size': 22})
        # malicious winning percentage figure
        figure_plot, ax_plot = plt.subplots(figsize=(15, 10))

        # initial axis setup
        my_xlabel = r'Nodes $ P_{i} $ order by stake'
        my_ylabel = r'Share of total stake/elections'

        analyse_results = self.analyse_simulate_results(
            simulate_file_name=simulate_file_name
        )

        winning_percentages = analyse_results["winning_percentages"]
        no_nodes = len(winning_percentages[0])

        # the stake vector
        stake_vector = analyse_results["stake_vector"]
        total_stake = np.sum(stake_vector)
        stake_vector = stake_vector/total_stake

        zipped_list = list(zip(stake_vector, winning_percentages[0]))
        zipped_list.sort(key=lambda x: x[0])

        nodes = np.arange(no_nodes)
        xticks = [0, int(no_nodes/4), int(no_nodes/2),
                  int(no_nodes*3/4), no_nodes-1]
        xticklabels = [r'$ P_{s_{%d}} $' % i
                       for i in xticks]

        # setup x axis
        ax_plot.set_xlabel(my_xlabel)
        ax_plot.set_xticks(xticks, xticklabels)
        # setup y axis
        ax_plot.set_ylabel(my_ylabel)
        max_y_value = np.round(
            np.max(
                [np.max(winning_percentages[0]), np.max(stake_vector)]
            ),
            decimals=2
        ) + 0.01
        ax_plot.set_ylim(top=max_y_value)
        my_yticks = np.linspace(start=0, stop=max_y_value, num=11)
        # setup y axis labels
        ax_plot.set_yticks(my_yticks)
        ax_plot.grid(linestyle='--', axis='y')

        stake_line = ax_plot.plot(
            nodes,
            [z[0] for z in zipped_list],
            label=r'Stake',
            color='black',
            linestyle=':'
        )
        winning_line = ax_plot.plot(
            nodes,
            [z[1] for z in zipped_list],
            label=r'Won elections',
            color='black',
            linestyle='--'
        )

        # add legend
        ax_plot.legend(
            handles=[stake_line[0], winning_line[0]],
            loc="upper left",
            prop={'size': 24}
        )
        # create the directory
        pathlib.Path(draw_directory).mkdir(parents=True, exist_ok=True)
        figure_plot.savefig(
            draw_directory +
            "/" +
            self._get_simulation_name() +
            "_stake_plot.pdf",
            format='pdf',
            dpi=1200,
            bbox_inches='tight'
        )
        # close the figure to save space
        plt.close(figure_plot)

    def draw_stake_cdf(
        self,
        simulate_file_name: str = None,
        draw_directory: str = None
    ) -> None:
        r"""
        Draw the boxplot of the election results when the number of malicious
        nodes increase.

        Args:
            simulate_file_name :
                The file where the simulation results are stored.
            draw_directory :
                The directory where the figures will be stored.

        Raises:
            ValueError : If the simulation file is not compatible.
        """
        # setup latex and font size
        plt.rcParams['text.usetex'] = True
        plt.rcParams.update({'font.size': 22})
        # malicious winning percentage figure
        figure_plot, ax_plot = plt.subplots(figsize=(15, 15))

        # initial axis setup
        my_xlabel = r'Share of stake'
        my_ylabel = r'Share of elections/nodes'

        analyse_results = self.analyse_simulate_results(
            simulate_file_name=simulate_file_name
        )

        winning_percentages = analyse_results["winning_percentages"]
        no_nodes = len(winning_percentages[0])

        # the stake vector
        stake_vector = analyse_results["stake_vector"]
        total_stake = np.sum(stake_vector)
        stake_vector = stake_vector/total_stake

        zipped_list = list(zip(stake_vector, winning_percentages[0]))
        zipped_list.sort(key=lambda x: x[0])

        stake_cdf = [
            np.sum(
                [z[0] for z in zipped_list[0:(index+1)]]
            )
            for index in range(no_nodes)
        ]
        win_cdf = [
            np.sum(
                [z[1] for z in zipped_list[0:(index+1)]]
            )
            for index in range(no_nodes)
        ]

        my_yticks = np.linspace(start=0, stop=1, num=11)
        my_xticks = np.linspace(start=0, stop=1, num=11)
        # setup x axis
        ax_plot.set_xlabel(my_xlabel)
        ax_plot.set_xticks(my_xticks)
        # setup y axis
        ax_plot.set_ylabel(my_ylabel)
        ax_plot.set_yticks(my_yticks)
        ax_plot.set_ylim(bottom=-0.1, top=1)
        ax_plot.grid(linestyle='--', axis='both')

        cdf_line = ax_plot.plot(
            stake_cdf,
            win_cdf,
            label=self.get_latex_name(),
        )
        fair_line = ax_plot.plot(
            stake_cdf,
            stake_cdf,
            label=r'Stake Fair Line',
        )
        nodes_line = ax_plot.plot(
            stake_cdf,
            (np.arange(no_nodes)+1)/no_nodes,
            label=r'Share of Nodes',
        )

        # add legend
        ax_plot.legend(
            handles=[cdf_line[0], fair_line[0], nodes_line[0]],
            loc="upper left",
            prop={'size': 24}
        )
        # create the directory
        pathlib.Path(draw_directory).mkdir(parents=True, exist_ok=True)
        figure_plot.savefig(
            draw_directory +
            "/" +
            self._get_simulation_name() +
            "_stake_cdf.pdf",
            format='pdf',
            dpi=1200,
            bbox_inches='tight'
        )
        # close the figure to save space
        plt.close(figure_plot)


class WeackCoinFlippingQLEP(QuantumLeaderElectionProtocolwithPoS):
    r"""
    The weak coin flipping quantum leader election protocol with proof
    of stake.

    The weak coin flipping quantum leader election protocol with proof of
    stake. It is a subclass of the quantum leader election protocol with
    proof of stake. It contains the attributes and methods for the weak coin
    flipping quantum leader election protocol.
    """

    wcf_type: WCFElectionType = None
    r"""
    The type of weak coin flipping election
    """
    def __init__(
            self,
            no_nodes: int = 7,
            no_elections: int = 1,
            quantum_data_provider: QuantumDataProvider = None,
            committee_size: int = None,
            stake_vector: np.ndarray = None,
            wcf_type: WCFElectionType = None
    ) -> None:
        # call super class QuantumLeaderElectionProtocolwithPoS constructor
        super().__init__(
            election_type=ElectionType.WCF,
            no_nodes=no_nodes,
            no_elections=no_elections,
            quantum_data_provider=quantum_data_provider,
            committee=CommitteeType.FIXED.get_committee(
                no_nodes=no_nodes,
                committee_size=committee_size
            ),
            stake_vector=stake_vector)
        self.wcf_type: WCFElectionType = wcf_type

    @override
    def _get_election_name(self) -> str:
        return super()._get_election_name() + "_" + self.wcf_type.name
