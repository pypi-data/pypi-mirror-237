# future annotations
from __future__ import annotations
# enumeration
from enum import IntEnum, auto
# typing
import typing
# matplolib for maker/line style
from matplotlib.lines import Line2D

__all__ = ["ElectionType"]


class ElectionType(IntEnum):
    r"""The types of election.

    The class contains the possible types of election to be
    used in the quantum leader election protocol.
    """

    WSTATE = auto()
    GHZSTATE = auto()
    HAMMING = auto()
    FOLDHAMMING = auto()
    WCF = auto()
    WALSH = auto()
    FOLDWALSH = auto()
    # add other election types
    # use upper case names
    # ELECTION_NAME = auto()
    DUMMY = auto()
    NEWPROTOCOL = auto()

    @classmethod
    def _missing_(cls, value: typing.Any) -> ElectionType:
        if type(value) is str:
            value = value.upper()
            if value in dir(cls):
                return cls[value]
        raise ValueError("%r is not a valid %s" % (value, cls.__name__))

    @staticmethod
    def get_options() -> list[str]:
        r"""
        Return a list of the possible types of election in string format.

        Goes thorugh all the possible values of the ElectionType and creates
        a list of the names of the values by mapping the name attribute of
        the ElectionType.

        Returns:
            election_types
                Return a list of string with the names of the types of
                the election

        Examples:
            >>> import lep.base
            >>> lep.base.ElectionType.get_options()
            ['WSTATE', 'GHZSTATE', 'HAMMING', 'FOLDHAMMING',
            'WCF', 'WALSH', 'FOLDWALSH']
        """
        return list(map(lambda x: x.name, list(ElectionType)))

    def get_marker_style(self) -> str:
        r"""
        Return the marker style depending on the election type.

        Returns:
            marker_style
                The marker style depending on the election type.
        """
        styles: list[str] = Line2D.filled_markers
        election_types: list[str] = list(ElectionType)
        marker_dict = dict(zip(election_types, styles))
        return marker_dict[self]
