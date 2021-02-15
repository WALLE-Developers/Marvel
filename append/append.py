import discord
from discord.abc import Messageable

from redbot.core import commands, Config
from redbot.core.commands import Context
from redbot.core.bot import Red
from functools import wraps

real_send = Messageable.send
CONFIG = Config.get_conf(None, 348964231348679, True, "Append")
CONFIG.register_global(toggle=False, double=True)

E = "<:wallelove:800005867838767124>"

@wraps(real_send)
async def send(
    self,
    content=None,
    *,
    tts=False,
    embed=None,
    file=None,
    files=None,
    delete_after=None,
    nonce=None,
    allowed_mentions=None,
) -> discord.Message:
    content = str(content) if content is not None else None
    if content:
        if len(content) > 1995:
            await real_send(self, E)
            if await CONFIG.double():
                content = f"{E}, {content}"
            if content.endswith((".", "!", "?")):
                content += f" {E}"
            elif content.endswith((" ", "\n", "```")):
                content += E
            else:
                content += f", {E}"
    else:
        content = E
    return await real_send(
        self,
        content=content,
        tts=tts,
        embed=embed,
        file=file,
        files=files,
        delete_after=delete_after,
        nonce=nonce,
        allowed_mentions=allowed_mentions,
    )


class Append(commands.Cog):
    __author__ = ["jack1142 (Jackenmen#6607)", "Jojo#7791"]

    def __init__(self, bot: Red):
        self.bot = bot

    def cog_unload(self):
        setattr(Messageable, "send", real_send)

    async def initalize(self):
        toggle = await CONFIG.toggle()
        if toggle:
            setattr(Messageable, "send", send)

    @commands.group(invoke_without_command=True)
    @commands.is_owner()
    async def appendtoggle(self, ctx, toggle: bool):
        """Toggle append because why not?"""
        if toggle:
            setattr(Messageable, "send", send)
        else:
            setattr(Messageable, "send", real_send)
        await ctx.tick()
        await CONFIG.toggle.set(toggle)

    @appendtoggle.command()
    async def double(self, ctx, toggle: bool):
        """Double"""
        await CONFIG.double.set(toggle)
        await ctx.tick()

    @commands.command()
    async def appendtoggle(self, ctx):
        """Credits for Jack because without SmileySend I wouldn't have this"""
        description = (
            "Thanks to Jack over at Red"
            " for giving me the tools to make this!"
            "\nYou can check Jack's smileysend out at their [repo](https://github.com/jack1142/WeirdUnsupportedCogsOfJack)"
        )
        embed = discord.Embed(
            title="Canadian Send Credits!",
            description=description,
            colour=await ctx.embed_colour(),
        )
        await ctx.send(embed=embed)
