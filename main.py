#IMPORTING EVERYTHING NEEDED AND SETTING UP VARIABLES

from __future__ import annotations

from discord.ext import commands
import discord
import sys
import os
import asyncio
import json 
from discord import app_commands

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

@bot.command()
async def SyncTree(ctx: commands.Context):
        synced = await bot.tree.sync()
        await ctx.send(f"Synced {synced} commands")


async def load_extensions():
    for filename in os.listdir("./Cogs"):
        if filename.endswith(".py"):
            # cut off the .py from the file name
            await bot.load_extension(f"Cogs.{filename[:-3]}")

async def main():
    async with bot:
        await bot.start(TOKEN)

async def on_tree_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        return await interaction.response.send_message(f"Command is currently on cooldown! Try again in **{error.retry_after:.2f}** seconds!", ephemeral=True)
    elif isinstance(error, app_commands.MissingPermissions):
        return await interaction.response.send_message(f"You're missing permissions to use that", ephemeral=True)
    else:
        return await interaction.response.send_message(f"{error}", ephemeral=True)

bot.tree.on_error = on_tree_error

asyncio.run(main())