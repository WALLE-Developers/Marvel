import typing

from abc import ABC
from redbot.core import commands, Config
from redbot.core.bot import Red

from .alliance import Alliance
from .tz import TZ
from .ceo import CEO
from .mjolnir import Mjolnir

IDENTIFIER = 3249832743924

class CompositeMetaClass(
    type(commands.Cog),
    type(ABC)
):
    pass
    
class Marvel(
    Alliance,
    CEO, 
    TZ,
    Mjolnir,
    commands.Cog,
    metaclass=CompositeMetaClass
):
    """Marvel commands built for WALL-E."""
    
    def __init__(self, bot: Red):
        self.bot = bot
        self.config = Config.get_conf(
            self, 
            IDENTIFIER, 
            force_registration=True
        )
        self.config.register_guild(
            timezone=None
        )
        self.config.register_member(
            tzon=False
        )
        self.config.register_user(
            lifted=0
        )

def setup(bot):
    bot.add_cog(Marvel(bot))
