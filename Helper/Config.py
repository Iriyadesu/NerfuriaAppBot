import json
import discord
from discord import app_commands

async def ReadConfig():
        with open("config.json", "r") as read_file:
            return json.load(read_file)
        
async def WriteConfig(data):
        with open("config.json", "w") as read_file:
            json_object = json.dumps(data)
            read_file.write(json_object)

async def on_tree_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.CommandOnCooldown):
        return await interaction.response.send_message(f"Command is currently on cooldown! Try again in **{error.retry_after:.2f}** seconds!", ephemeral=True)
    elif isinstance(error, app_commands.MissingPermissions):
        return await interaction.response.send_message(f"You're missing permissions to use that", ephemeral=True)
    else:
        return await interaction.response.send_message(f"{error}", ephemeral=True)
