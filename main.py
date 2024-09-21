#IMPORTING EVERYTHING NEEDED AND SETTING UP VARIABLES

from __future__ import annotations

from discord.ext import commands
import discord
import re
import sys
import os
import asyncio

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
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents)

    async def setup_hook(self) -> None:

        # For dynamic items, we must register the classes
        self.add_dynamic_items(GuildApplicationButton)
        self.add_dynamic_items(CommunityApplicationButton)

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')


bot = PersistentViewBot()

async def load_extensions():
    for filename in os.listdir("./Cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"Cogs.{filename[:-3]}")

async def main():
    async with bot:
        await load_extensions()
        await bot.start(TOKEN)

asyncio.run(main())