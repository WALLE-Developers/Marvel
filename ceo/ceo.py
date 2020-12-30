import discord
import random
from redbot.core import commands

class CEO(commands.Cog):
    """How much of a CEO are you?"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ceo(self, ctx):
        """How much of a CEO are you?"""
        await ctx.send(f"{ctx.author.name}, you're gonna be a **{random.randint(1, 100)}% CEO** in your next crystal opening.")
