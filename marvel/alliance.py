import discord
import random
from redbot.core import commands, checks, Config, bank

class Alliance(MixinMeta):
    """A collection of alliance commands built for WALL-E."""
    
    @commands.group()
    async def allianceset(self, ctx):
        """Setup for your alliance."""
            
    @allianceset.command()
    @commands.has_permissions(manage_roles=True)
    async def officer(self, ctx, role: discord.Role):
        """Set your officer role."""
        await self.config.guild(ctx.guild).officerrole.set(role.id)
        await ctx.send(f"Done. {role.mention} will now be considered as an alliance officer role.")
