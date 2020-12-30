import discord
from redbot.core import commands, checks, Config

class Alliance(commands.Cog):
  """Alliance commands for MCOC."""
  
  def __init__(self, bot):
    self.bot = bot
    
  @commands.command()
  async def timezone(self, ctx, timezone: str):
    """
    Set the timezone on your nickname.

    Example Usage:
    `[p]timezone +1`
    `[p]timezone -4`

    Reset your nickname:
    `[p]timezone none`
    """
    try:
      if "none" in timezone:
        await ctx.author.edit(nick=ctx.author.name)
        await ctx.send("Your nickname has been reset.")
      elif len(timezone) > 3:
        await ctx.send("That nickname is too long for it to be a timezone.")
      else:
        await ctx.author.edit(nick=f"{ctx.author.name} [GMT {timezone}]")
        await ctx.send(f"Done! Your timezone has been added to your nickname as `{ctx.author.name} [GMT {timezone}]`.")
    except discord.Forbidden:
      await ctx.send("I have insufficient permissions to change your nickname. Also, I cannot change server owner nicknames.")
