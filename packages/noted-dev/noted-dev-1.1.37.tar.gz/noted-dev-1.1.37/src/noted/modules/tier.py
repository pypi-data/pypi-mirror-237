# © Copyright 2022 CERN. This software is distributed under the terms of
# the GNU General Public Licence version 3 (GPL Version 3), copied verbatim
# in the file "LICENCE.txt". In applying this licence, CERN does not waive
# the privileges and immunities granted to it by virtue of its status as an
# Intergovernmental Organization or submit itself to any jurisdiction.

from enum import Enum

class Tier(Enum):
    """Class for tier attributes."""
    _Tier0 = '0'
    _Tier1 = '1'
    _Tier2 = '2'
    _Tier3 = '3'
