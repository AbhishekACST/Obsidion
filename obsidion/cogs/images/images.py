import discord
from discord.ext import commands

from obsidion.utils.utils import usernameToUUID

import logging

log = logging.getLogger(__name__)


class images(commands.Cog):
    def __init__(self, bot):
        self.session = bot.http_session
        self.bot = bot

    @commands.command(aliases=["ach", "advancement"])
    async def achievement(
        self, ctx: commands.Context, block_name: str, title: str, text: str
    ):
        """Create your very own custom Minecraft achievements."""
        await ctx.channel.trigger_typing()
        embed = discord.Embed(color=0x00FF00)
        embed.set_image(
            url=f"https://api.bowie-co.nz/api/v1/images/advancement?item={block_name}&title={title}&text={text}"
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def sign(
        self,
        ctx: commands.Context,
        line1: str,
        line2: str = "%20",
        line3: str = "%20",
        line4: str = "%20",
    ):
        """Create your very own custom Minecraft Signs."""
        await ctx.channel.trigger_typing()
        embed = discord.Embed(color=0x00FF00)
        embed.set_image(
            url=f"https://api.bowie-co.nz/api/v1/images/sign?line1={line1}&line2={line2}&line3={line3}&line4={line4}"
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def avatar(self, ctx: commands.Context, username: str):
        """Renders a Minecraft players face."""
        await ctx.channel.trigger_typing()
        uuid = await usernameToUUID(username, ctx.bot.http_session)
        if uuid:
            embed = discord.Embed(
                description=f"Here is: `{username}`'s Face! \n **[DOWNLOAD](https://visage.surgeplay.com/face/512/{uuid})**",
                color=0x00FF00,
            )
            embed.set_image(url=f"https://visage.surgeplay.com/face/512/{uuid}")

            await ctx.send(embed=embed)
        else:
            await ctx.send(
                f"{ctx.message.author.mention}, :x: The user: `{username}` does not exist!"
            )

    @commands.command()
    async def skull(self, ctx: commands.Context, username: str = None):
        """Renders a Minecraft players skull."""
        await ctx.channel.trigger_typing()
        uuid = await usernameToUUID(username, ctx.bot.http_session)
        if uuid:
            embed = discord.Embed(
                description=f"Here is: `{username}`'s Skull! \n **[DOWNLOAD](https://visage.surgeplay.com/head/512/{uuid})**",
                color=0x00FF00,
            )
            embed.set_image(url=f"https://visage.surgeplay.com/head/512/{uuid}")

            await ctx.send(embed=embed)
        else:
            await ctx.send(
                f"{ctx.message.author.mention}, :x: The user: `{username}` does not exist!"
            )

    @commands.command()
    async def skin(self, ctx: commands.Context, username: str):
        """Renders a Minecraft players skin."""
        await ctx.channel.trigger_typing()
        uuid = await usernameToUUID(username, ctx.bot.http_session)
        if uuid:
            embed = discord.Embed(
                description=f"Here is: `{username}`'s Skin! \n **[DOWNLOAD](https://visage.surgeplay.com/full/512/{uuid})**",
                color=0x00FF00,
            )
            embed.set_image(url=f"https://visage.surgeplay.com/full/512/{uuid}")

            await ctx.send(embed=embed)
        else:
            await ctx.send(
                f"{ctx.message.author.mention}, :x: The user: `{username}` does not exist!"
            )

    @commands.command()
    async def render(self, ctx: commands.Context, render_type: str, username: str):
        """Renders a Minecraft players skin in 6 different ways. You can choose from these 6 render types: face, front, frontfull, head, bust & skin."""
        await ctx.channel.trigger_typing()
        renders = ["face", "front", "frontfull", "head", "bust", "skin"]
        if render_type in renders:
            uuid = await usernameToUUID(username, ctx.bot.http_session)
            if uuid:
                embed = discord.Embed(
                    description=f"Here is: `{username}`'s {render_type}! \n **[DOWNLOAD](https://visage.surgeplay.com/{type_}/512/{uuid})**",
                    color=0x00FF00,
                )
                embed.set_image(
                    url=f"https://visage.surgeplay.com/{render_type}/512/{uuid}"
                )

                await ctx.send(embed=embed)
            else:
                await ctx.send(
                    f"{ctx.message.author.mention}, :x: The user: `{username}` does not exist!"
                )
        else:
            await ctx.send(
                f"{ctx.message.author.mention}, Please supply a render type. Your options are:\n `face`, `front`, `frontfull`, `head`, `bust`, `skin` \n Type: ?render <render type> <username>"
            )
