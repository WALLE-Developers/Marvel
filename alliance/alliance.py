import discord
from redbot.core import commands, checks, Config

TZ = 'PST', 'MST', 'CST', 'EST', 'BST', 'GMT', 'UTC', 'CET', 'MSK', 'GST', 'IST', 'SST', 'CST', 'JST', 'AEDT', 'NZDT', 'pst', 'mst', 'cst', 'est', 'bst', 'gmt', 'utc', 'cet', 'msk', 'gst', 'ist', 'sst', 'cst', 'jst', 'aedt', 'nzdt'

class Alliance(commands.Cog):
  """Alliance commands for MCOC."""
  
  def __init__(self, bot):
    self.bot = bot
    self.config = Config.get_conf(self, 392483748324, force_registration=True)
    self.config.register_guild(timezone=None)
    
  @commands.command()
  async def timezoneset(self, ctx, global_time: str):
    """
    Set your TZ type such as GMT or PST.
    
    Please pick from a valid timezone:
    
    `PST`, `MST`, `CST`, `EST`, `BST`, `GMT`, `UTC`, `CET`, 
    `MSK`, `GST`, `IST`, `SST`, `CST`, `JST`, `AEDT`, or `NZDT`. 
    """
    if global_time.startswith(TZ):
      await self.config.guild(ctx.guild).timezone.set(global_time)
      await ctx.send(f"Done. Your guild's timezone is now `{global_time}`.")
    else:
      await ctx.send(f"That doesn't look like a valid timezone. Please check the list.")
    
    
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
    tz = await self.config.guild(ctx.guild).timezone()
    if tz is None:
      await ctx.send(f"You have not enabled this feature. Please use `{ctx.clean_prefix}timezoneset`.")
    else:
      try:
        if "none" in timezone:
          await ctx.author.edit(nick=ctx.author.name)
          await ctx.send("Your nickname has been reset.")
        elif len(timezone) > 3:
          await ctx.send("That nickname is too long for it to be a timezone.")
        else:
          await ctx.author.edit(nick=f"{ctx.author.name} [{tz.upper()}{timezone}]")
          await ctx.send(f"Done! Your timezone has been added to your nickname as `{ctx.author.name} [{tz.upper()}{timezone}]`.")
      except discord.Forbidden:
        await ctx.send("I have insufficient permissions to change your nickname. Also, I cannot change server owner nicknames.")
