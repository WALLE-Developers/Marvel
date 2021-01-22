from abc import ABC
from typing import Dict

from redbot.core import Config
from redbot.core.bot import Red

class MixinMeta(ABC):

    def __init__(self, *_args):
        self.settings: Config
        self.bot: Red
        self.sanitize: Dict[str, bool]
