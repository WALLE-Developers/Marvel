import discord
from redbot.core import commands, bank, Config
from redbot.core.utils.chat_formatting import humanize_number

C = ":coin:"

class PayDay(commands.Cog):
    """Get some free currency."""

    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(self, identifier=59365034743, force_registration=True)
        self.config.register_guild(pay=200)

    def cog_unload(self):
        global _old_payday
        if _old_payday:
            try:
                self.bot.remove_command("payday")
            except Exception as error:
                log.info(error)
            self.bot.add_command(_old_payday)

    @commands.command()
    @commands.cooldown(1, 100, commands.BucketType.user)
    async def payday(self, ctx):
        """Get some free currency."""
        pay = await self.config.guild(ctx.guild).pay()
        currency = await bank.get_currency_name(ctx.guild)
        pos = await bank.get_leaderboard_position(ctx.author)
        embed = discord.Embed(title=f"PAYDAY! {C}",
                              description=(
                                  f"Congrats {ctx.author.name}, you just got paid "
                                  f"{pay} {currency}!\nYou are now #{pos} on {ctx.bot.user.name}'s global leaderboard!"
                                  f"\n\nYou previously had {humanize_number(await bank.get_balance(ctx.author))} {currency}, "
                                  f"\nYou can check the leaderboard by using `{ctx.clean_prefix}leaderboard`."
                              ), color=0x94dbd4)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_footer(text=f"💵 | {ctx.bot.user.name} Economy")
        await bank.deposit_credits(ctx.author, pay)
        await ctx.send(embed=embed)

async def setup(bot):
  cog = PayDay(bot)
  global _old_payday
  _old_payday = bot.get_command("payday")
  if _old_payday:
      bot.remove_command(_old_payday.name)
  bot.add_cog(cog)
