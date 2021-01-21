from abc import ABC

from redbot.core import commands, checks, Config

from .alliance import Alliance

class CompositeMetaClass(type(commands.Cog), type(ABC)):
    """
    This allows the metaclass used for proper type detection to
    coexist with discord.py's metaclass
    This is from
    https://github.com/Cog-Creators/Red-DiscordBot/blob/V3/develop/redbot/cogs/mod/mod.py#L23
    """

    pass
    
class Marvel(Alliance, commands.Cog, metaclass=CompositeMetaClass):
  """Marvel commands built for WALL-E."""
  
  
