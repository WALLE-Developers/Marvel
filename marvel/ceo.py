from .abc import MixinMeta

import discord
import random
from redbot.core import commands, bank

responses = [
    ", according to my calculations, you will be a",
    ", you're gonna be a",
    ", I think you're gonna end up as a"
]

class CEO(MixinMeta):
    pass

    @commands.command()
    @commands.cooldown(1, 300, commands.BucketType.user)
    async def ceo(self, ctx):
        """How much of a marvel CEO are you?"""
        ceo = random.randint(1, 100)
        currency = await bank.get_currency_name(ctx.guild)
        if ceo == 42:
            await ctx.send(f"**42%**, nice {ctx.author.name}!! I added 42,000 {currency} to your bank account.")
            await bank.deposit_credits(ctx.author, 42000)
        elif ceo == 69:
            await ctx.send(f"**69%**, oooo yeahh. I added 69,000 {currency} to your bank account, {ctx.author.name}.")
            await bank.deposit_credits(ctx.author, 69000)
        elif ceo == 100:
            await ctx.send(f"**100%** wooooow {ctx.author.name} I added 100,000 {currency} to your bank account.")
            await bank.deposit_credits(ctx.author, 100000)
        else:
            await ctx.send(f"{ctx.author.name}{random.choice(responses)} **{ceo}% CEO** in your next crystal opening.")
