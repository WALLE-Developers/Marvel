import discord; import random; from redbot.core import commands, checks, Config, bank, modlog
from redbot.core.utils.chat_formatting import bold as b; 
class SupportServer(commands.Cog):
  def __init__(self, bot): self.bot = bot; self.config = Config.get_conf(self, 3029848234, force_registration=True)
  @commands.group()
  async def assign(self, ctx):'Assign a support server role.';pass
  @assign.command(aliases=["contrib"])
  async def contributor(self, ctx, member: discord.Member):'Assign contributor.'
