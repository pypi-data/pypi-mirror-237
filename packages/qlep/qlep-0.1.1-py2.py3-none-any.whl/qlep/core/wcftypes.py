# future annotations
from __future__ import annotations
# enumeration
from enum import IntEnum, auto
# typing
import typing

__all__ = ["WCFElectionType"]


class WCFElectionType(IntEnum):
    r"""The types of weak coin flipping election.

    The class contains the possible types of weak coin
    flipping election to be used in the quantum leader
    election protocol.
    """

    BOZZIO2020 = auto()
    MOCHON2004 = auto()

    # add other wcf election types
    # use upper case names
    # WCF_ELECTION_NAME = auto()

    @classmethod
    def _missing_(cls, value: typing.Any) -> WCFElectionType:
        if type(value) is str:
            value = value.upper()
            if value in dir(cls):
                return cls[value]
        raise ValueError("%r is not a valid %s" % (value, cls.__name__))

    @staticmethod
    def get_options() -> list[str]:
        r"""
        Return a list of the possible types of wcf election in string format.

        Goes thorugh all the possible values of the WCFElectionType and creates
        a list of the names of the values by mapping the name attribute of
        the WCFElectionType.

        Returns:
            wcf_election_types
                Return a list of string with the names of the
                types of the wcf election

        Examples:
            >>> import lep.base
            >>> lep.base.WCFElectionType.get_options()
            ['BOZZIO2020', 'MOCHON2004']
        """
        return list(map(lambda x: x.name, list(WCFElectionType)))
