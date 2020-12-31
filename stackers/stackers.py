from redbot.core import commands, Config
import discord

class Stackers(commands.Cog):
    """How much WALL-E Trash can we stack?"""

    def __init__(self, bot):
        self.bot = bot
        self.emojis = self.bot.loop.create_task(self.init())
        self.config = Config.get_conf(self, 95873453487, force_registration=True)
        self.config.register_user(
            stack=0
        )
        self.config.register_guild(
            stack=0
        )
        self.config.register_global(
            stack=0
        )

    def cog_unload(self):
        if self.emojis:
            self.emojis.cancel()

    async def init(self):
        await self.bot.wait_until_ready()
        self.walle = {
            "walle": discord.utils.get(self.bot.emojis, id=794141784577802250),
            "trash": discord.utils.get(self.bot.emojis, id=791308063935168522)
        }

    @commands.command()
    async def stack(self, ctx):
        """Stack WALL-E Trash!"""
        stackglob = await self.config.stack()
        stackuser = await self.config.user(ctx.author).stack()
        stackguild = await self.config.guild(ctx.guild).stack()
        stackglob += 1
        stackuser += 1
        stackguild += 1
        await self.config.stack.set(stackglob)
        await self.config.user(ctx.author).stack.set(stackuser)
        await self.config.guild(ctx.guild).stack.set(stackguild)
        await ctx.send(
            f"{ctx.author.name} contributes towards the trash stack. {self.walle['walle']}"
            f"\nYou can see the StackStats by using `{ctx.clean_prefix}stackstats`."
            )

    @commands.command()
    async def stackstats(self, ctx):
        """Review the stackstats."""
        glob = await self.config.stack()
        user = await self.config.user(ctx.author).stack()
        guild = await self.config.guild(ctx.guild).stack()
        embed = discord.Embed(title=f"{ctx.bot.user.name} StackStats {self.walle['trash']}", color=0xf56060)
        embed.add_field(name="Global Stacks", value=glob, inline=False)
        embed.add_field(name="Guild Stacks", value=guild, inline=False)
        embed.add_field(name="Your contributions", value=user, inline=False)
        embed.set_footer(text="♻️ | Stackers")
        await ctx.send(embed=embed)

    @commands.command()
    @commands.is_owner()
    async def stackdebug(self, ctx):
        """Reset all config for stackers."""
        await self.config.clear_all()
        await ctx.message.add_reaction("✅")
