# This was an idea that formed after seeing this post on r/admincraft https://www.reddit.com/r/admincraft/comments/qh3175/plugin_for_ingame_rewards_for_being_active_in/

import discord, json
from mcrcon import MCRcon
from discord.ext import commands


print("Starting up...")
f = open('config.json')
config = json.load(f)
token = config["token"]
terminalprefix = config["terminalprefix"]
prefix = config["prefix"]
f.close()
client = commands.Bot(command_prefix=prefix, help_command=None, case_insensitive=True)
cogs = ['cogs.reward', 'cogs.manager', 'cogs.link']
for cog in cogs:
    client.load_extension(cog)
    print(f"{terminalprefix} Loaded cog")


@client.event
async def on_ready():
    print(f"{terminalprefix} Connected to Discord.")
    print(f"{client.user.name} is ready.")


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please make sure to say all required arguments (ERROR:MissingRequiredArgument). ")
    elif isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send("Hey! Sorry but you don't have perms for that command. Duh-Doy!")


client.run(token)
