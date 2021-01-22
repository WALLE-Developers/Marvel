from .abc import MixinMeta

import discord
from redbot.core import commands, checks, Config

TZ = (
    'PST', 'MST', 'CST', 'EST', 'BST', 'GMT', 'UTC', 
    'CET', 'MSK', 'GST', 'IST', 'SST', 'CST', 'JST', 
    'AEDT', 'NZDT', 'pst', 'mst', 'cst', 'est', 'bst', 
    'gmt', 'utc', 'cet', 'msk', 'gst', 'ist', 
    'sst', 'cst', 'jst', 'aedt', 'nzdt'
)

class TZ(MixinMeta):
    pass
  
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
        elif global_time.startswith(str(TZ)):
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
        if member.nick is None:
            member.nick = member.name
        off = await self.config.guild(ctx.guild).officerrole()
        officer = discord.utils.get(ctx.guild.roles, id=off)
        tzon = await self.config.user(member).tzon()
        if officer not in ctx.author.roles:
            return await ctx.send("You are not an alliance officer, you cannot use this command.")
        tz = await self.config.guild(ctx.guild).timezone()
        if tz is None:
            await ctx.send(f"You have not enabled this feature. Please get an officer to use `{ctx.clean_prefix}timezoneset`.")
        else:
            try:
                if "none" in timezone:
                    await member.edit(nick=member.name)
                    await self.config.user(member).tzon.set(False)
                    await ctx.send(f"{member.name}'s nickname has been reset.")
                elif len(timezone) > 4:
                    await ctx.send("That nickname is too long for it to be a timezone.")
                elif tzon is False:
                    await member.edit(nick=f"{member.nick} [{tz.upper()}{timezone}]")
                    await self.config.user(member).tzon.set(True)
                    await ctx.send(f"Done! The timezone `{tz.upper()}{timezone}` has been added to {member.name}'s nickname.")
                else:
                    await ctx.send(f"{member.name} already has their timezone set, as `{member.nick}`.")
            except discord.Forbidden:
                await ctx.send(f"I have insufficient permissions to change {member.name}'s nickname. Also, I cannot change server owner nicknames.")
