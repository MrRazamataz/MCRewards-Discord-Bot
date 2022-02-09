from discord.ext import commands, tasks
import json
import discord
import urllib3
from decimal import *
version = Decimal("0.04") # dont change, thanks.
class manager(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.updatecheck.start()

    @tasks.loop(minutes=10)
    async def updatecheck(self):
        try:
            version_url = "https://www.mrrazamataz.ga/archive/python/mcrewards/version.txt"
            http = urllib3.PoolManager()
            response = http.request('GET', version_url)
            ver = response.data.decode('utf-8')
            vernum = Decimal(ver)
            if vernum == version:
                pass

            elif vernum < version:
                #print("Meddling detected in `manager.py` (version number invalid), ignoring :P")
                pass
            elif vernum > version:
                print(f"You are running an outdated version! Running: `{version}`, Latest: `{vernum}`. \nFind the latest files here: https://github.com/MrRazamataz/MCRewards-Discord-Bot .")
                await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"new version on GitHub `{vernum}`."))

            else:
                pass

        except Exception as e:
            pass

def setup(client):
    client.add_cog(manager(client))