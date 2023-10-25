# future annotations
from __future__ import annotations
# enumeration
from enum import IntEnum, auto
# typing
import typing
# numpy
import numpy as np
# override decorator
from typing_extensions import override

__all__ = ["CommitteeType", "Committee"]


class CommitteeType(IntEnum):
    r"""The types of committees.

    The class contains the possible types of committees
    to be used in the quantum leader election protocol.
    """

    ALL = auto()
    FIXED = auto()

    # add other committee types
    # use upper case names
    # COMMITTEE_NAME = auto()

    @classmethod
    def _missing_(cls, value: typing.Any) -> CommitteeType:
        if type(value) is str:
            value = value.upper()
            if value in dir(cls):
                return cls[value]
        raise ValueError("%r is not a valid %s" % (value, cls.__name__))

    @staticmethod
    def get_options() -> list[str]:
        r"""
        Return a list of the possible types of commitees in string format.

        Returns:
            committee_types
                return a list of string with the names of the
                types of the committees

        Examples:
            >>> import lep.core
            >>> lep.core.CommitteeType.get_options()
            ['ALL', 'FIXED']
        """
        return list(map(lambda x: x.name, list(CommitteeType)))

    def get_committee(
            self,
            no_nodes: int,
            committee_size: int
    ) -> Committee:
        r"""
        Return a committee of the given type.

        Args:
            no_nodes :
                The number of nodes.
            committee_size :
                The size of the committee.

        Returns:
            committee
                The committee of the given type.

        Raises:
            ValueError : not implemented committee type
        """
        match self:
            case CommitteeType.ALL:
                return CommitteeALL(
                    no_nodes=no_nodes
                )
            case CommitteeType.FIXED:
                return CommitteeFixed(
                    committee_size=committee_size,
                    no_nodes=no_nodes
                )
            case _:
                raise ValueError(
                    "The committee type %s is not implemented" % self.name
                )


class Committee():
    r"""
    The super class for the committee implementation.
    """

    committee_type: CommitteeType = None
    r"""
    type of committee
    """
    committee_size: int = None
    r"""
    size of the committee
    """
    no_nodes: int = None
    r"""
    number of nodes
    """
    no_committees: int = None
    r"""
    number of committees
    """
    no_committee_rounds: int = 1
    r"""
    The number of committee rounds in the quantum leader election
    protocol.
    """

    def __init__(
            self,
            committee_type: CommitteeType,
            committee_size: int,
            no_nodes: int
    ) -> None:
        r"""
        Initialize the committee.

        Args:
            committee_type :
                The type of the committee.
            committee_size :
                The size of the committee.
            no_nodes :
                The number of nodes.

        Raises:
            ValueError : incompatible parameters
        """
        self.committee_type: CommitteeType = committee_type
        self.committee_size: int = committee_size
        self.no_nodes: int = no_nodes
        self.no_committees: int = int(
            np.floor(
                (no_nodes-1) /
                (committee_size-1)
            )
        )
        self.no_committee_rounds: int = int(
            np.floor(
                np.log2(self.no_nodes) /
                np.log2(self.committee_size)
            )
        )
        if self.committee_size ** self.no_committee_rounds != self.no_nodes:
            raise ValueError(
                """The number of nodes %d is not compatible with the committee
                size %d""" % (
                    self.no_nodes,
                    self.committee_size
                )
            )

    def get_initial_committees(
            self,
            register_ids: np.ndarray,
    ) -> np.ndarray:
        r"""
        First round of committees.

        Args:
            register_ids :
                The ids of the nodes.

        Returns:
            committees
                The committees. shape = (x, committee_size)
        """
        committees = np.copy(register_ids)
        committees.shape = (
            int(self.no_nodes/self.committee_size),
            self.committee_size
        )
        return committees

    def get_initial_stake_committees(
            self,
            register_ids: np.ndarray,
            stake_vector: np.ndarray,
    ) -> np.ndarray:
        r"""
        First round of committees.

        Args:
            register_ids :
                The ids of the nodes.
            stake_vector :
                The stake of the nodes.

        Returns:
            [committees, stakes]
                The committees with stakes.
                shape = (x, 2, committee_size)
        """
        committees = np.copy(register_ids)
        committees.shape = (
            int(self.no_nodes/self.committee_size),
            self.committee_size
        )
        stakes = np.copy(stake_vector)
        stakes.shape = (
            int(self.no_nodes/self.committee_size),
            self.committee_size
        )
        return np.array([np.array([committees[index], stakes[index]])
                         for index in range(len(committees))]
                        )

    def update_committees(
            self,
            committees: np.ndarray,
            committees_winners: np.ndarray,
    ) -> np.ndarray:
        r"""
        Update committees.

        Args:
            committees :
                The committees.
            committees_winners :
                The winners of the committees. A 1D array with the
                ids of the winning nodes from the previous elections
                of the prevous committees.

        Returns:
            committees
                The new committees. shape = (x, committee_size)

        Raises:
            ValueError :
                Numbber of winners is not compatible with the committee size.
        """
        if len(committees_winners) == 1:
            return committees
        if len(committees_winners) % self.committee_size != 0:
            raise ValueError(
                """The number of winners %d is not compatible with the
                committee size %d""" % (
                    len(committees_winners),
                    self.committee_size
                )
            )
        # create the new commitees
        committees_winners.shape = (
            int(len(committees_winners)/self.committee_size),
            self.committee_size
        )
        # add the new created committees
        committees = np.vstack(
            (committees, committees_winners)
        )
        return committees

    def update_stake_committees(
            self,
            committees: np.ndarray,
            committees_winners: list[tuple[int, float]],
    ) -> np.ndarray:
        r"""
        Update committees.

        Args:
            committees :
                The committees.
            committees_winners :
                The winners of the committees. A 1D array with the
                ids of the winning nodes from the previous elections
                of the prevous committees.

        Returns:
            committees
                The new committees. shape = (x, committee_size)

        Raises:
            ValueError :
                Numbber of winners is not compatible with the committee size.
        """
        if len(committees_winners) == 1:
            return committees
        if len(committees_winners) % self.committee_size != 0:
            raise ValueError(
                """The number of winners %d is not compatible with the
                committee size %d""" % (
                    len(committees_winners),
                    self.committee_size
                )
            )
        new_committees = np.array(
            [winner[0] for winner in committees_winners]
        )
        new_stakes = np.array(
            [winner[1] for winner in committees_winners]
        )
        # create the new commitees
        new_committees.shape = (
            int(len(committees_winners)/self.committee_size),
            self.committee_size
        )
        new_stakes.shape = (
            int(len(committees_winners)/self.committee_size),
            self.committee_size
        )
        committees_winners = (
            np.array(
                [np.array([new_committees[index], new_stakes[index]])
                 for index in range(len(new_committees))]
            )
        )
        # add the new created committees
        committees = np.vstack(
            (committees, committees_winners)
        )
        return committees

    def get_name(self) -> str:
        r"""
        Return the name for the committee.

        Returns:
            committee_name
                The name for the committee.
        """
        committee_name: str = "_%s_%d" % (
            self.committee_type.name,
            self.committee_size
        )
        return committee_name

    def get_latex_name(self) -> str:
        r"""
        Return the latex name for the committee.

        Returns:
            latex_name
                The latex name for the committee.
        """
        latex_name = (
            self.committee_type.name +
            r' ' +
            str(self.committee_size)
        )
        return latex_name


class CommitteeALL(Committee):
    r"""
    The committee implementation for the type ALL of committee.
    """
    def __init__(
            self,
            no_nodes: int
    ) -> None:
        r"""
        Initialize the committee of type ALL.

        Args:
            committee_size :
                The size of the committee.
            no_nodes :
                The number of nodes.
        """
        super().__init__(
            committee_type=CommitteeType.ALL,
            committee_size=no_nodes,
            no_nodes=no_nodes
        )

    @override
    def get_latex_name(self) -> str:
        return r''


class CommitteeFixed(Committee):
    r"""
    The committee implementation for the type FIXED of committee.
    """
    def __init__(
            self,
            committee_size: int,
            no_nodes: int
    ) -> None:
        r"""
        Initialize the committee of type FIXED.

        Args:
            committee_size :
                The size of the committee.
            no_nodes :
                The number of nodes.
        """
        super().__init__(
            committee_type=CommitteeType.FIXED,
            committee_size=committee_size,
            no_nodes=no_nodes
        )

    @override
    def get_latex_name(self) -> str:
        return r'-CF(%d)' % self.committee_size
