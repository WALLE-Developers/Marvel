import discord
import random
from redbot.core import commands

responses = [
    ", according to my calculations, you will be a",
    ", you're gonna be a",
    ", I think you're gonna end up as a"
]

class CEO(commands.Cog):
    """How much of a CEO are you?"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ceo(self, ctx):
        """How much of a CEO are you?"""
        await ctx.send(f"{ctx.author.name}{random.choice(responses)} **{random.randint(1, 100)}% CEO** in your next crystal opening.")
