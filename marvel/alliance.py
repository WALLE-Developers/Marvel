from .abc import MixinMeta

import discord
import random
from redbot.core import commands, checks, Config, bank

class Alliance(MixinMeta):
    """A collection of alliance commands built for WALL-E."""
    
#    @commands.group()
#    async def allianceset(self, ctx):
#        """Setup for your alliance."""