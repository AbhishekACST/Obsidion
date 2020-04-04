import discord
from discord.ext import commands
import aiohttp
import datetime
import asyncio
from utils.utils import get_uuid, get

class servers(commands.Cog, name="Servers"):

    def __init__(self, bot):
        self.session = bot.session
        self.bot = bot
        self.hypixel = bot.hypixel_api
        self.update = datetime.datetime.now()

        self.bg_task = bot.loop.create_task(self.my_background_task())

    async def my_background_task(self):
        await self.bot.wait_until_ready()
        print("start")
        while not self.bot.is_closed():
            for server, value in self.bot.pool["serverTracking"].items():
                print(server, value)
                data = await get(self.session, f"https://api.mcsrvstat.us/2/{value['server']}")
                print("yay")
                channel = self.bot.get_channel(int(value["channel"]))
                print("channel")
                print(data)
                if data["online"]:
                    name = f"{value['server'].split('.')[0].title()}: {data['players']['now']:,} / {data['players']['max']:,}"
                    await channel.edit(name=name)
                else:
                    print("offline")
                    await channel.edit(name="SERVER IS OFFLINE")
            self.update = datetime.datetime.now()
            await asyncio.sleep(5*60) # task runs every 5 minutes
        print("end")

    
    @commands.command(hidden=True)
    async def update(self, ctx):
        await ctx.send(self.update)

    #@commands.command()
    #async def blocksmcself(self, ctx, username):
    #    pass

    #@commands.command()
    #async def funcraft(self, ctx, username):
    #    pass

    #async def hivemc(self, ctx, username):
    #    pass
'''
    @commands.command()
    async def hypixel(self, ctx, username):
        """Get information about a Hypixel user"""
        pass
            

    #@commands.command()
    #async def manacube(self, ctx, username):
    #    pass

    #@commands.command()
    #async def minesage(self, ctx, username):
    #    pass

    #@commands.command()
    #async def universocraft(self, ctx, username):
    #    pass

    #@commands.command()
    #async def veltpvp(self, ctx, username):
    #    pass

    #@commands.command()
    #async def wynncraft(self, ctx, username):
    #    uuid = get_uuid(self.session, username)
    #    if uuid:
    #        url = f"https://api.wynncraft.com/v2/player/{uuid}/stats"
    #        data = await get(self.session, url)

    #        embed = discord.Embed(color=0x00ff00)
    #        
    #        information = ""

    #        dates = ""
    #        dates += f"First Login: `{data['meta']['firstJoin']}`\n"
    #        dates += f"Last Login: `{data['meta']['lastJoin']}`"
    #        dates += f"Playtime: `{data['meta']['playtime']}`"

    #        await ctx.send(embed=embed)
    #    pass
'''