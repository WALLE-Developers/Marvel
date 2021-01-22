from .abc import MixinMeta

import discord
from redbot.core import commands, checks, Config

from random import choice as c, randint as r
from asyncio import sleep, TimeoutError

match_starting = "Please wait for the fight to commence."

default_combattents = {
    "Baron Zemo": "https://d13ezvd6yrslxm.cloudfront.net/wp/wp-content/images/civil-war-baron-zemo-header-700x300.png", 
    "Captain America": "https://www.denofgeek.com/wp-content/uploads/2019/03/captain-america-first-avenger-main.jpg?fit=1200%2C675",
    "Green Goblin": "https://img.cinemablend.com/filter:scale/quill/0/5/9/b/e/d/059bedcdd489d8e7a7e585cfabd274c4a407149a.jpg?mw=600",
    "Proxima Midnight": "https://img.cinemablend.com/filter:scale/quill/2/e/8/f/9/3/2e8f939f8e9d71b59e5c9d10c36db7b7f6f8706f.png?mw=600",
    "Luke Cage": "https://www.telegraph.co.uk/content/dam/on-demand/2016/09/30/luke-cage-generic_trans_NvBQzQNjv4BqqVzuuqpFlyLIwiB6NTmJwU8R8p1QYM5LJTq3yzG3ShE.jpg"
}

class Marvel(MixinMeta):
    """
    A collection of commands for Marvel.
    
    This file is not focused on Marvel Contest of Champions.
    """

    @commands.command()
    async def combat(self, ctx, member: discord.Member = None):
        for i in range(1):
            if member is None:
                for name, url in default_combattents.items():
                    contestant = c(name)
                    title = f"{ctx.author.name} contests against {contestant}!"
                    e = discord.Embed(title=title, description=match_starting, color=0xeeba4a)
                    e.set_image(url=url)
                    e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                    await ctx.send(embed=e)
                    await sleep(10)
                    await ctx.send(f"The battle has commenced: **{ctx.author.name}** VS **{contestant}**! :zap:")
                    def check(x):
                        return x.author == ctx.author and x.channel == ctx.channel and x.content.lower().startswith('hit')            
                    for i in range(1):
                        while True:
                            damage1 = r(250, 2500)
                            damage2 = r(250, 2500)
                            await ctx.send(f"{contestant} hits you for {damage1}, {ctx.author.name}.")
                            my_health_points = await self.config.member(ctx.author).myhealth()
                            their_health_points = await self.config.member(ctx.author).myhealth()
                            my_health_points =- damage1                        
                            my_health_points = await self.config.member(ctx.author).myhealth.set(my_health_points)
                            if their_health_points > 0:
                                await ctx.send(f"**{contestant} has won the round!**")
                                break
                            else:
                                pass
                            try:
                                hit = await self.bot.wait_for("message", timeout=20, check=check)
                                await ctx.send(f"You hit {contestant} for {damage2}, {ctx.author.name}.")
                                hit -= damage2
                                my_health_points = await self.config.member(ctx.author).theirhealth.set(hit)
                                if my_health_points > 0:
                                    await ctx.send(f"**{contestant} has won the round!**")
                                    break
                                else:
                                    pass
                            except TimeoutError:
                                continue
                    await self.config.member(ctx.author).myhealth.clear()
                    await self.config.member(ctx.author).theirhealth.clear()
            else:
                title = f"{ctx.author.name} contests against {member.name}!"
                e = discord.Embed(title=title, description=match_starting, color=0xeeba4a)
                e.set_author(name=ctx.author, icon_url=ctx.author.avatar_url)
                await ctx.send(embed=e)
                await sleep(10)
                await ctx.send(f"The battle has commenced: **{ctx.author.name}** VS **{member.name}**! :zap:")
                def p1(x):
                    return x.author == ctx.author and x.channel == ctx.channel and x.content.lower().startswith('hit')
                def p2(x):
                    return x.author == member and x.channel == ctx.channel and x.content.lower().startswith('hit')            
                for i in range(1):
                    while True:
                        damage1 = r(250, 2500)
                        damage2 = r(250, 2500)
                        try:
                            await ctx.send(f"{ctx.author.name}, it's your turn. Type `hit` to deal damage to {member.name}.")
                            p1 = await self.bot.wait_for("message", timeout=20, check=p1)
                            currenthealth = await self.config.member(member).currenthealth()
                            removed = -damage1
                            await self.config.member(member).currenthealth.set(removed)
                            await ctx.send(f"You hit {member.name} for {damage1}!")
                        except TimeoutError:
                            continue
                        try:
                            await ctx.send(f"{member.name}, it's your turn. Type `hit` to deal damage to {ctx.author.name}.")
                            p2 = await self.bot.wait_for("message", timeout=20, check=p2)
                            currenthealth = await self.config.member(ctx.author).currenthealth()
                            removed = -damage2
                            await self.config.member(ctx.author).currenthealth.set(removed)
                            await ctx.send(f"You hit {ctx.author.name} for {damage2}!")
                        except TimeoutError:
                            continue
                await self.config.member(ctx.author).currenthealth.clear()
                await self.config.member(member).currenthealth.clear()