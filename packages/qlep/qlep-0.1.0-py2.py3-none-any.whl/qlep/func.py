
# future annotations
from __future__ import annotations
import numpy as np
import logging
import typing

# lep
import qlep.core
import qlep.basic
import qlep.ecc


def generate_qlep(
    no_nodes: int = 15,
    no_elections: int = 100,
    election_type: qlep.core.ElectionType = None,
    provider: qlep.core.Provider = qlep.core.Provider.AER,
    backend_name: str = "aer_simulator",
    committee_type: qlep.core.CommitteeType = None,
    committee_size: int = None,
    **kwargs
) -> qlep.core.QuantumLeaderElectionProtocol:
    r"""
    Returns a Quantum Leader Election Protocol for
    the given parameters.

    Args:
        no_nodes :
            The number of nodes in the network.
        no_elections :
            The number of elections to be simulated.
        election_type :
            The type of the election.
        provider :
            The provider for the quantum backend.
        backend_name :
            The quantum backend name.
        committee_type :
            The type of the committee.
        committee_size :
            The size of the committee.
        **kwargs :
            The keyword arguments specific to every type
            of election.

    Returns:
        qlep
            The Quantum Leader Election Protocol.

    Raises:
        ValueError : bad parameters
    """
    use_stake: bool = False
    if "use_stake" in kwargs.keys():
        use_stake = kwargs["use_stake"]
    stake_vector: np.ndarray = None
    if "stake_vector" in kwargs.keys():
        stake_vector = kwargs["stake_vector"]

    quantum_data_provider: qlep.core.QuantumDataProvider = (
        qlep.core.QuantumDataProvider(
            provider=provider,
            backend_name=backend_name
        )
    )
    committee: qlep.core.Committee = (
        committee_type.get_committee(
            no_nodes=no_nodes,
            committee_size=committee_size
        )
    )
    if stake_vector is None:
        if use_stake:
            no_data_bits = int(np.ceil(np.log2(no_nodes)))
            size = 2**no_data_bits
            if size == (no_nodes + 1):
                # vector is the sqrt probability of the superposition
                # all have equal changes except all 0 binary string
                vector = np.ones(shape=size, dtype='f') / np.sqrt(size-1)
                # for all 0 binary string
                vector[0] = 0
                stake_vector = vector
            else:
                # vector is the sqrt probability of the superposition
                # all have equal changes
                vector = np.ones(shape=size, dtype='f') / np.sqrt(size)
                stake_vector = vector
    match (election_type):
        case qlep.core.ElectionType.WSTATE:
            use_history: bool = False
            tolerance: int = None
            if "use_history" in kwargs.keys():
                use_history = kwargs["use_history"]
            if "tolerance" in kwargs.keys():
                tolerance = kwargs["tolerance"]
            return qlep.basic.WStateQLEP(
                no_nodes=no_nodes,
                no_elections=no_elections,
                quantum_data_provider=quantum_data_provider,
                committee=committee,
                use_history=use_history,
                tolerance=tolerance
            )
        case qlep.core.ElectionType.GHZSTATE:
            fewer_qubits: bool = True
            if "fewer_qubits" in kwargs.keys():
                fewer_qubits = kwargs["fewer_qubits"]
                logging.info(f"[QLEPGenerator] fewer_qubits: {fewer_qubits}")
            logging.info(f"[QLEPGenerator] fewer_qubits: {fewer_qubits}")
            return qlep.basic.GHZStateQLEP(
                no_nodes=no_nodes,
                no_elections=no_elections,
                quantum_data_provider=quantum_data_provider,
                committee=committee,
                stake_vector=stake_vector,
                fewer_qubits=fewer_qubits
            )
        case qlep.core.ElectionType.HAMMING:
            return qlep.ecc.HammingQLEP(
                no_nodes=no_nodes,
                no_elections=no_elections,
                quantum_data_provider=quantum_data_provider,
                committee=committee,
                stake_vector=stake_vector
            )
        case qlep.core.ElectionType.FOLDHAMMING:
            fold: int = 3
            limit: int = 2
            if "fold" in kwargs.keys():
                fold = kwargs["fold"]
            if fold == 3:
                limit = 2
            elif fold == 5:
                limit = 3
            else:
                logging.error("[QLEPGenerator] Bad fold value")
                raise ValueError("Bad fold value")
            return qlep.ecc.FoldHammingQLEP(
                no_nodes=no_nodes,
                no_elections=no_elections,
                quantum_data_provider=quantum_data_provider,
                committee=committee,
                stake_vector=stake_vector,
                fold=fold,
                limit=limit
            )
        case qlep.core.ElectionType.WALSH:
            return qlep.ecc.WalshQLEP(
                no_nodes=no_nodes,
                no_elections=no_elections,
                quantum_data_provider=quantum_data_provider,
                committee=committee,
                stake_vector=stake_vector
            )
        case qlep.core.ElectionType.FOLDWALSH:
            fold: int = 2
            limit: int = 1
            if "fold" in kwargs.keys():
                fold = kwargs["fold"]
            if fold == 2:
                limit = 1
            else:
                logging.error("[QLEPGenerator] Bad fold value")
                raise ValueError("Bad fold value")
            return qlep.ecc.FoldWalshQLEP(
                no_nodes=no_nodes,
                no_elections=no_elections,
                quantum_data_provider=quantum_data_provider,
                committee=committee,
                stake_vector=stake_vector,
                fold=fold,
                limit=limit
            )
        case qlep.core.ElectionType.WCF:
            # wcf_type: lep.core.WCFElectionType = None
            # if "wcf_type" in kwargs.keys():
            #     wcf_type = kwargs["wcf_type"]
            return None
        case qlep.core.ElectionType.DUMMY:
            return qlep.basic.DummyQLEP(
                no_nodes=no_nodes,
                no_elections=no_elections,
                quantum_data_provider=quantum_data_provider,
                committee=committee
            )
        case _:
            logging.error("[QLEPGenerator] Bad election type")
            raise ValueError("Bad election type")


def qlep_from_dict(
    experiment_information: dict[str, typing.Any]
) -> qlep.core.QuantumLeaderElectionProtocol:
    r"""
    Generates a Quantum Leader Election Protocol from the experiment
    information.

    Args:
        experiment_information :
            The experiment information dictionary.

    Returns:
        qlep
            The Quantum Leader Election Protocol.
    """
    no_nodes = experiment_information.pop('no_nodes', None)
    no_elections = experiment_information.pop('no_elections', None)
    election_type = experiment_information.pop('election_type', None)
    quantum_data_provider = experiment_information.pop(
        'quantum_data_provider',
        None
    )
    if quantum_data_provider is not None:
        provider = quantum_data_provider.provider
        backend_name = quantum_data_provider.backend_name
    else:
        provider = qlep.core.Provider.AER
        backend_name = 'aer_simulator'
    committee = experiment_information.pop('committee', None)
    if committee is not None:
        committee_type = committee.committee_type
        committee_size = committee.committee_size
    else:
        committee_type = None
        committee_size = None
    return generate_qlep(
        no_nodes=no_nodes,
        no_elections=no_elections,
        election_type=election_type,
        provider=provider,
        backend_name=backend_name,
        committee_type=committee_type,
        committee_size=committee_size,
        **experiment_information
    )
