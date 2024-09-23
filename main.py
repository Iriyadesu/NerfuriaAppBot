#IMPORTING EVERYTHING NEEDED AND SETTING UP VARIABLES

from __future__ import annotations

from discord.ext import commands
import discord
import sys
import os
import asyncio
import json 

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
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        await load_extensions()
        synced = await bot.tree.sync()
        print(f"synced {synced} commands")
        print('------')

bot = PersistentViewBot()

async def load_extensions():
    for filename in os.listdir("./Cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"Cogs.{filename[:-3]}")

async def main():
    async with bot:
        await bot.start(TOKEN)


asyncio.run(main())