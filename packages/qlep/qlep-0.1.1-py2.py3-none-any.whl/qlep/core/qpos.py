"""
The qpos submodule of lep.core contains the Quantum Proof of Stake
"""
import qiskit
import numpy as np

__all__ = ["get_stake_matrix", "get_stake_gate"]


def get_stake_matrix(stake_vector: np.ndarray) -> np.ndarray:
    r"""
    Generates a unitary matrix from the stake vector

    Args:
        stake_vector :
            The stake vector

    Returns:
        matrix
            The unitary matrix for the stake vector

    Note:
        The unitary matrix is generated using the Householder transformation
    """
    size = len(stake_vector)
    # vector is with stake
    vector = stake_vector
    # e1 = (1 0 0 ... 0)
    e1 = np.zeros(size)
    e1[0] = 1
    # w = v/|v| - e1
    w = vector/np.linalg.norm(vector) - e1
    # HO = I - 2 x (w x w)/<w,w>
    matrix = np.identity(size) - 2*((np.outer(w, w))/(np.inner(w, w)))
    return matrix


def get_stake_gate(
        stake_vector: np.ndarray
) -> qiskit.extensions.UnitaryGate:
    r"""
    Generates a quantum gate from the stake vector

    Args:
        stake_vector :
            The stake vector

    Returns:
        qiskit.extensions.UnitaryGate
            The quantum gate for the stake vector
    """
    stakeOperator = qiskit.extensions.UnitaryGate(
        get_stake_matrix(stake_vector)
        )
    return stakeOperator
