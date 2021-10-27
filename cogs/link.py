from discord.ext import commands
import json
import discord

class link(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.Cog.listener()
    async def on_ready(self):
        global accountdata
        with open("accountdata.json") as f:
            accountdata = json.load(f)
        print("Account data loaded.")
    @commands.command(name="link")
    async def link(self, ctx, username=None):
        if username is None:
            await ctx.send("No username provided.")
            return
        global accountdata
        try:
            accountdata.pop(f"{ctx.author.id}")
            await ctx.send("Replacing old username...")
            id = str(ctx.author.id)
            accountdata[id] = accountdata.get(id, f"{username}")
            with open("accountdata.json", "w") as f:
                json.dump(accountdata, f, indent=4)
            await ctx.send(f"`{ctx.author.name}`, your username has been changed to `{username}`.")
        except Exception as e:
            id = str(ctx.author.id)
            accountdata[id] = accountdata.get(id, f"{username}")
            with open("accountdata.json", "w") as f:
                json.dump(accountdata, f, indent=4)
            await ctx.send(f"`{ctx.author.name}`, you have been added as `{username}`.")
    @commands.command(name="show")
    async def show(self, ctx, member: discord.Member):
        global accountdata
        id = str(member.id)
        embed = discord.Embed(title="User found!", description="\u200b", color=0x00ff00)
        embed.set_author(name="MCRewards", url="https://mrrazamataz.ga")
        embed.add_field(name=f"`{member.name}` is", value=f"`{accountdata[id]}` in Minecraft", inline=False)
        await ctx.send(embed=embed)




def setup(client):
    client.add_cog(link(client))
