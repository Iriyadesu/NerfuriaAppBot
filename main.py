#IMPORTING EVERYTHING NEEDED AND SETTING UP VARIABLES

from __future__ import annotations

from discord.ext import commands
import discord
import sys
import os
import asyncio
import json 
from discord import app_commands
from Helper.Config import on_tree_error
from DynamicButtons import *

#GETTING THE TOKEN FOR THE BOT

if len(sys.argv) > 1:  # if the patch is specified as an argument
    path = sys.argv[1]
else:  # default path
    path = '.env'

    with open(path, 'r') as file:  # get the token
        TOKEN = file.read()

#SETTING UP THE BOT


class PersistentViewBot(commands.Bot):
    def __init__(self):

        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=discord.Intents.all())

    async def setup_hook(self) -> None:

        # For dynamic items, we must register the classes
        self.add_dynamic_items(GuildApplicationButton)
        self.add_dynamic_items(CommunityApplicationButton)
        self.add_dynamic_items(VotingUpvoteButton)
        self.add_dynamic_items(VotingDownvoteButton)

    async def on_ready(self):
        # Logging that the bot is online
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        #Loading extentions
        await load_extensions()
        synced = await bot.tree.sync()
        #Syncing the bot command tree
        print(f"Synced {synced} commands")
        print('------')

    
async def load_extensions():
    for filename in os.listdir("./Cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"Cogs.{filename[:-3]}")

bot = PersistentViewBot()

#Setting the error handler to my own custom one
bot.tree.on_error = on_tree_error

#Manual command tree sync in case it needs to be used without the bot restarting
@bot.command()
async def SyncTree(ctx: commands.Context):
        synced = await bot.tree.sync()
        await ctx.send(f"Synced {synced} commands")

#Running the actual bot
async def main():
    async with bot:
        await bot.start(TOKEN)


asyncio.run(main())