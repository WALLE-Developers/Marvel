import typing

from abc import ABC
from redbot.core import commands, Config
from redbot.core.bot import Red

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
            timezone=None,
            alliance_name=None,
            alliance_tag=None,
            alliance_requirements=None,
            alliance_battlegroup_quantity=None,

        )
        self.config.register_member(
            tzon=False
        )
        self.config.register_user(
            lifted=0,
            user_in_game_name=None,
            user_alliance_name=None,
            
        )

    async def red_delete_data_for_user(
        self,
        requester: Literal["discord", "owner", "user", "user_strict"],
        user_id: int
    ) -> None:
        await self.config.user_from_id(user_id).clear()

def setup(bot):
    bot.add_cog(Marvel(bot))
