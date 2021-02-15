from .append import Append


async def setup(bot):
    c = Append(bot)
    bot.add_cog(c)
    await c.initalize()
