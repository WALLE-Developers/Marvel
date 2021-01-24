from .abc import MixinMeta

import discord
import random
from asyncio import sleep, TimeoutError

from redbot.core import commands, checks, Config, bank

class Alliance(MixinMeta):
    """A collection of alliance commands built for WALL-E."""

    @commands.command()
    async def myinfoset(self, ctx):
        """Set your MCOC profile."""
        author = ctx.author
        try:
            await ctx.send("Alright {ctx.author.display_name}, I'll send you some DMS.")
            await author.send("The following questions will set your profile. If you would not like to answer a particular question, you can type `skip`.")
            await sleep(1)
            await author.send("What is your ingame name?")
        except discord.Forbidden:
            await ctx.send("I am unable to send you DMs.")
        
        def check(x):
            return x.author == ctx.author and x.channel == ctx.author.dm_channel

        def digit(x):
            return x.author == ctx.author and x.channel == ctx.author.dm_channel and x.content.isdigit() or x.content.lower().startswith("skip")

        for i in range(1):
            
            try:
                user_in_game_name = await self.bot.wait_for("message", timeout=30, check=check)
                if in_game_name.lower().content.startswith("skip"):
                    await ctx.send("Sure. This field has been left unspecified.")
                    continue
            except TimeoutError:
                await ctx.send("You took too long to respond. Please restart the process - no changes have been made.")

            await ctx.send("What is the name of the alliance you belong to? You can specify `none` if you aren't in an alliance. Please specify the name, NOT the tag.")
            try:
                user_alliance_name = await self.bot.wait_for("message", timeout=30, check=check)
                if user_alliance_name.content.lower().startswith("skip"):
                    await ctx.send("Sure. This field has been left unspecified.")
                    continue
                elif user_alliance_name.content.lower().startswith("none"):
                    await ctx.send("Sure. I now know that you are not part of an alliance.")
                    continue
                else:
                    continue
            except TimeoutError:
                await ctx.send("You took too long to respond. Please restart the process - no changes have been made.")

            if user_alliance_name.content.lower().startswith("none"):
                continue
            else:
                await ctx.send(f"What is the tag for your alliance: '{user_alliance_name.content}?")
                try:
                    user_alliance_tag = await self.bot.wait_for("message", timeout=30, check=check)
                    if user_alliance_tag.content.lower().startswith("skip"):
                        await ctx.send("Sure. This field has been left unspecified.")
                        continue
                except TimeoutError:
                    await ctx.send("You took too long to respond. Please restart the process - no changes have been made.")

            await ctx.send("What is your game progression? For example: Cavalier, Throne Breaker, Conqueror etc...")
            try:
                user_progression = await self.bot.wait_for("message", timeout=30, check=check)
                if user_progression.lower().content.startswith("skip"):
                    await ctx.send("Sure. This field has been left unspecified.")
                    continue
            except TimeoutError:
                await ctx.send("You took too long to respond. Please restart the process - no changes have been made.")

            await ctx.send("What is your current prestige?")
            try:
                user_prestige = await self.bot.wait_for("message", timeout=30, check=digit)
                if user_prestige.lower().content.startswith("skip"):
                    await ctx.send("Sure. This field has been left unspecified.")
                    continue
            except TimeoutError:
                await ctx.send("You took too long to respond. Please restart the process - no changes have been made.")

            await ctx.send("How old are you currently? If you would not like to share this information, type `skip`.")
            try:
                user_age = await self.bot.wait_for("message", timeout=30, check=digit)
                if user_age.lower().content.startswith("skip"):
                    await ctx.send("Sure. This field has been left unspecified.")
                    continue
            except TimeoutError:
                await ctx.send("You took too long to respond. Please restart the process - no changes have been made.")

            await ctx.send("What is your gender? If you would not like to share this information, type `skip`.")
            try:
                user_gender = await self.bot.wait_for("message", timeout=30, check=digit)
                if user_gender.lower().content.startswith("skip"):
                    await ctx.send("Sure. This field has been left unspecified.")
                    continue
            except TimeoutError:
                await ctx.send("You took too long to respond. Please restart the process - no changes have been made.")

            await ctx.send("What is your timezone?")
            try:
                user_timezone = await self.bot.wait_for("message", timeout=30, check=digit)
                if user_timezone.lower().content.startswith("skip"):
                    await ctx.send("Sure. This field has been left unspecified.")
                    continue
            except TimeoutError:
                await ctx.send("You took too long to respond. Please restart the process - no changes have been made.")

            await ctx.send("Give yourself a brief description. You could include additional information about your account, or about yourself.")
            try:
                user_description = await self.bot.wait_for("message", timeout=30, check=digit)
                if user_description.lower().content.startswith("skip"):
                    await ctx.send("Sure. This field has been left unspecified.")
                    continue
            except TimeoutError:
                await ctx.send("You took too long to respond. Please restart the process - no changes have been made.")
            await ctx.send("Thanks {ctx.author.name}! All done.")
        
        if not user_in_game_name.content.lower().startswith("skip"):
# This obviously isn't finished yet, lol
# May need to rethink how I do this config also.

 
    @commands.group()
    async def allianceset(self, ctx):
        """Setup for your alliance."""

    @allianceset.group()
    async def info(self, ctx):
        """Sets information for your alliance."""

    @info.command()
    async def quicksetup(self, ctx):
        """
        Set info about your alliance.

        A following Q&A scheme will be held to record your information.
        """
        author = ctx.author

        def check(x):
            return x.author == ctx.author and x.channel == ctx.author.dm_channel

        def bgcheck(x):
            return x.author == ctx.author and x.channel == ctx.author.dm_channel and x.content.startswith(('1', '2', '3'))

        for i in range(1):
            await ctx.send("What is the name of your alliance? Please do not include the tag.")
            try:
                alliance_name = await self.bot.wait_for("message", timeout=20, check=check)
                await self.config.guild(ctx.guild).alliance_name.set(alliance_name)
                return await ctx.send("What is the tag for your alliance?")
            except asyncio.TimeoutError:
                await ctx.send("You took too long to respond. Please restart the process.")
                break
            try:
                alliance_tag = await self.bot.wait_for("message", timeout=20, check=check)
                await self.config.guild(ctx.guild).alliance_tag.set(alliance_tag)
                return await ctx.send("What are the join requirements for your alliance? You could specify prestige, activity etc...")
            except asyncio.TimeoutError:
                await ctx.send("You took too long to respond. Please restart the process.")
                break
            try:
                alliance_requirements = await self.bot.wait_for("message", timeout=20, check=check)
                await self.config.guild(ctx.guild).alliance_requirements.set(alliance_requirements)
                return await ctx.send("How many battlegroups do you run in your alliance?")
            except asyncio.TimeoutError:
                await ctx.send("You took too long to respond. Please restart the process.")
                break
            try:
                alliance_battlegroup_quantity = await self.bot.wait_for("message", timeout=20, check=bgcheck)
                await self.config.guild(ctx.guild).alliance_battlegroup_quantity.set(alliance_battlegroup_quantity)
                return await ctx.send("How many battlegroups do you run in your alliance?")
            except asyncio.TimeoutError:
                await ctx.send("You took too long to respond. Please restart the process.")
                break
            # This isn't finished either
