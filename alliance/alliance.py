import discord
from redbot.core import commands, checks, Config

TZ = 'PST', 'MST', 'CST', 'EST', 'BST', 'GMT', 'UTC', 'CET', 'MSK', 'GST', 'IST', 'SST', 'CST', 'JST', 'AEDT', 'NZDT', 'pst', 'mst', 'cst', 'est', 'bst', 'gmt', 'utc', 'cet', 'msk', 'gst', 'ist', 'sst', 'cst', 'jst', 'aedt', 'nzdt'

class Alliance(commands.Cog):
  """Alliance commands for MCOC."""
  
  def __init__(self, bot):
    self.bot = bot
    self.config = Config.get_conf(self, 392483748324, force_registration=True)
    self.config.register_guild(timezone=None, officerrole=None)
    
  @commands.group()
  async def allianceset(self, ctx):
    """Setup for your alliance."""
    
  @commands.command()
  @commands.is_owner()
  async def allianceconfigdel(self, ctx):
    await self.config.guild(ctx.guild).timezone.set(None)
    await self.config.guild(ctx.guild).officerrole.set(None)
    await ctx.message.add_reaction("✅")
    
  @allianceset.command()
  @commands.has_permissions(manage_roles=True)
  async def officer(self, ctx, role: discord.Role):
    """Set your officer role."""
    await self.config.guild(ctx.guild).officerrole.set(role.id)
    await ctx.send(f"Done. {role.mention} will now be considered as an alliance officer role.")
    
  @commands.command()
  async def timezoneset(self, ctx, global_time: str):
    """
    Set your TZ type such as GMT or PST.
    
    Please pick from a valid timezone:
    
    `PST`, `MST`, `CST`, `EST`, `BST`, `GMT`, `UTC`, `CET`, 
    `MSK`, `GST`, `IST`, `SST`, `CST`, `JST`, `AEDT`, or `NZDT`. 
    """
    off = await self.config.guild(ctx.guild).officerrole()
    officer = discord.utils.get(ctx.guild.roles, id=off)
    if off is None:
      await ctx.send("Your alliance does not have an alliance officer role set up.")
    elif officer not in ctx.author.roles:
      return await ctx.send("You are not an alliance officer, you cannot use this command.")
    elif global_time.startswith(TZ):
      await self.config.guild(ctx.guild).timezone.set(global_time)
      await ctx.send(f"Done. Your guild's timezone is now `{global_time}`.")
    else:
      await ctx.send(f"That doesn't look like a valid timezone. Please check the list.")
    
    
  @commands.command()
  async def timezone(self, ctx, member: discord.Member, timezone: str):
    """
    Set the timezone on one's nickname.

    Example Usage:
    `[p]timezone @kreusada +1`
    `[p]timezone 719988449867989142 -4`

    Reset a user's nickname:
    `[p]timezone @kreusada none`
    """
    off = await self.config.guild(ctx.guild).officerrole()
    officer = discord.utils.get(ctx.guild.roles, id=off)
    if officer not in ctx.author.roles:
      return await ctx.send("You are not an alliance officer, you cannot use this command.")
    tz = await self.config.guild(ctx.guild).timezone()
    if tz is None:
      await ctx.send(f"You have not enabled this feature. Please get an officer to use `{ctx.clean_prefix}timezoneset`.")
    else:
      try:
        if "none" in timezone:
          await member.edit(nick=member.name)
          await ctx.send(f"{member.name}'s nickname has been reset.")
        elif len(timezone) > 3:
          await ctx.send("That nickname is too long for it to be a timezone.")
        else:
          await member.edit(nick=f"{member.name} [{tz.upper()}{timezone}]")
          await ctx.send(f"Done! The timezone `{tz.upper()}{timezone}` has been added to {member.name}'s nickname as `{member.name} [{tz.upper()}{timezone}]`.")
      except discord.Forbidden:
        await ctx.send("I have insufficient permissions to change your nickname. Also, I cannot change server owner nicknames.")
