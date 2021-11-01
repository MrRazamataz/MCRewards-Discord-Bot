from discord.ext import commands, tasks
import json
import discord
from mcrcon import MCRcon

class reward(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        global levels, rewards
        print("Loading levels...")
        with open("levels.json") as f:
            levels = json.load(f)
        print("Levels loaded.")
        with open("rewards.json") as f:
            rewards = json.load(f)
        print("Starting save tasks loop...")
        self.save.start()
        with open("config.json") as f:
            config = json.load(f)
        global recent_change
        recent_change = False
        global rconip
        rconip = config["rconip"]
        global rconport
        rconport = config["rconport"]
        global rconpassword
        rconpassword = config["rconpassword"]
        global prefix
        prefix = config["prefix"]
        global accountdata
        with open("accountdata.json") as f:
            accountdata = json.load(f)
    @commands.Cog.listener()
    async def on_message(self, message):
        global levels, accountdata
        if message.guild is None:
            return
        if not message.author.bot:
            id = str(message.author.id)
            levels[id] = levels.get(id, 0.99) + 0.01
            global recent_change, prefix
            recent_change = True
            if levels[id].is_integer():
                level = round(levels[id])
                rank = "rank"
                lp_group = f"{level}-{rank}"
                await message.channel.send(f"{message.author.mention}, well done! You're now level: `{level}`.")
                if str(message.author.id) in accountdata:
                    if str(level) in rewards:
                        command = rewards[f"{str(level)}"]["command"]
                        try:
                            command = command.replace("%player%", f"{accountdata[id]}")
                        except:
                            pass
                        #await message.channel.send(f"The command: \n`{command}`")
                        with MCRcon(f"{rconip}", f"{rconpassword}", port=rconport) as mcr:
                            resp = mcr.command(f"{command}")
                else:
                    await message.channel.send(f"Please link your Minecraft account to your Discord with `{prefix}link <username>`!")
                #with MCRcon(f"{rconip}", f"{rconpassword}", port=rconport) as mcr:
                    #resp = mcr.command(f"lp user {accountdata[id]} parent add {rank}")

    @commands.command(name="addreward")
    @commands.has_permissions(administrator=True)
    async def addreward(self, ctx, level: int, *, command):
        try:
            global rewards
            if level is None:
                await ctx.send("Please provide a level as a whole number.")
                return

            #if level.is_interger():
                #pass
            #else:
                #await ctx.send("The level you provide needs to be a whole number.")
                #return
            if command is None:
                await ctx.send("Please provide the command that should be ran on the server. You can use `%player%` as a "
                               "placeholder for a players username.")
                return

            with open('rewards.json', 'r+') as f:
                data = json.load(f)
                f.seek(0)
                f.truncate(0)
                data[f'{level}'] = {"command": f"{command}"}
                json.dump(data, f, indent=4)
            await ctx.send(f"Added reward at level `{level}` with the command `{command}`.")
            with open("rewards.json") as f:
                rewards = json.load(f)
        except Exception as e:
            await ctx.send(f"`{e}`")


    @tasks.loop(minutes=3)
    async def save(self):
        global recent_change
        if recent_change is True:
            with open("levels.json", "w") as f:
                json.dump(levels, f, indent=4)
            recent_change = False
            print("Saved")
        else:
            return
def setup(client):
    client.add_cog(reward(client))