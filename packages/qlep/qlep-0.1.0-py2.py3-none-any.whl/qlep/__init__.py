"""
Contains the core of lep: base, qlep, qpos, etc.

base contains the base classes for lep

basic contains the basic quantum leader election protocol

ecc contains the error correcting codes quantum leader election protocol

wcf contains the weak coin flipping quantum leader election protocol

"""
# future annotations
from __future__ import annotations
from qlep.draw import draw_election_CDF
from qlep.draw import draw_election_fair_boxplot
from qlep.draw import draw_stake_election_CDF
from qlep.draw import draw_malicious_CDF
from qlep.draw import get_filtered_qleps_with_data
from qlep.func import generate_qlep
from qlep.func import qlep_from_dict

__author__ = "Stefan-Dan Ciocirlan (sdcioc)"
__copyright__ = "Copyright 2023, Singapore Blockchain Innovation Programme"
__credits__ = ["Dumitrel Loghin"]
__license__ = "EUPL-1.2"
__version__ = "0.1.0"
__maintainer__ = "Stefan-Dan Ciocirlan"
__email__ = "stefan_dan@xn--ciocrlan-o2a.ro"
__status__ = "Production"

__all__ = ["core", "basic", "ecc", "wcf"]

__all__ += [
    'generate_qlep',
    'qlep_from_dict',
    'draw_election_CDF',
    'draw_election_fair_boxplot',
    'draw_stake_election_CDF',
    'draw_malicious_CDF',
    'get_filtered_qleps_with_data'
]
