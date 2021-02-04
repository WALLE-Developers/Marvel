from .abc import MixinMeta
import discord
from redbot.core import commands, checks, Config

TZ_LIST = (
    'PST', 'MST', 'CST', 'EST', 'BST', 'GMT', 'UTC', 'CET',
    'MSK', 'GST', 'IST', 'SST', 'CST', 'JST', 'AEDT', 'NZDT',
    'pst', 'mst', 'cst', 'est', 'bst', 'gmt', 'utc', 'cet', 
    'msk', 'gst', 'ist', 'sst', 'cst', 'jst', 'aedt', 'nzdt'
)

class TZ(MixinMeta):
    pass
  
    @commands.command()
    @commands.mod()
    async def timezoneset(self, ctx, global_time: str):
        """
        Set your TZ type such as GMT or PST.

        Please pick from a valid timezone:

        `PST`, `MST`, `CST`, `EST`, `BST`, `GMT`, `UTC`, `CET`, 
        `MSK`, `GST`, `IST`, `SST`, `CST`, `JST`, `AEDT`, or `NZDT`. 
        """
        if global_time.lower().startswith(tuple(TZ_LIST)):
            await self.config.guild(ctx.guild).timezone.set(global_time)
            await ctx.send(f"Done. Your guild's timezone is now `{global_time}`.")
        else:
            await ctx.send(f"That doesn't look like a valid timezone. Please check the list.")


    @commands.command()
    @commands.mod()
    async def timezone(self, ctx, member: discord.Member, timezone: str):
        """
        Set the timezone on one's nickname.
        
        Example Usage:
        `[p]timezone @kreusada +1`
        `[p]timezone 719988449867989142 -4`
        
        Reset a user's nickname:
        `[p]timezone @kreusada none`
        """
        if member.nick is None:
            member.nick = member.name
        tz = await self.config.guild(ctx.guild).timezone()
        tzon = await self.config.member(member).tzon()
        if tz is None:
            await ctx.send(f"You have not enabled this feature. Please get an officer to use `{ctx.clean_prefix}timezoneset`.")
        else:
            try:
                if "none" in timezone:
                    await member.edit(nick=member.name)
                    await self.config.member(member).tzon.set(False)
                    await ctx.send(f"{member.name}'s nickname has been reset.")
                elif len(timezone) > 4:
                    await ctx.send("That nickname is too long for it to be a timezone.")
                elif tzon is False:
                    await member.edit(nick=f"{member.nick} [{tz.upper()}{timezone}]")
                    await self.config.member(member).tzon.set(True)
                    await ctx.send(f"Done! The timezone `{tz.upper()}{timezone}` has been added to {member.name}'s nickname.")
                else:
                    await ctx.send(f"{member.name}'s nickname already has a timezone: `{member.nick}`. Use {ctx.clean_prefix}timezone {member.name} none` to reset it.")
            except discord.Forbidden:
                await ctx.send(f"I have insufficient permissions to change {member.name}'s nickname. Also, I cannot change server owner nicknames.")
