"""
For init file
set_config
"""

import os
import sys

# add path
sys.path.append(os.path.dirname(__file__))


import __common
from klemmen import Klemmen


set_config = __common.set_config


class Bench:
    """Test bench class, used for implementing the operations of different test benches."""

    def __init__(
        self,
        did: str = "upper",
    ) -> None:
        self.did = did
        self.device = "Bench"

    def kl_event(self):
        """Function kl event to contrl kl15 and kl30."""
        return Klemmen(self.did, self.device)
