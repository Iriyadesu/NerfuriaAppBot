import discord
from discord.ext import commands
from DynamicButtons import GuildApplicationButton, CommunityApplicationButton
from discord import app_commands
import json
from Helper.Config import ReadConfig, WriteConfig

class Setup(commands.Cog):
    """
    This class is for the initial setup and config handling of the bot.
    """
    def __init__(self, bot):
        self.bot = bot

    #Slash commands for the bot. The name must be all lowercase no spaces. Use interaction.x instead of context. Must use interaction.response to avoid an error message.
    @app_commands.command(
            name="set",
            description="Sets the channels in the config"
    )
    @app_commands.describe(type="Type of config to set")
    @app_commands.checks.has_permissions(administrator=True)
    @app_commands.choices(type=[
                app_commands.Choice(name="Thread channel", value="Thread_Channel_ID"),
                app_commands.Choice(name="Voting Channel", value="Voting_Channel_ID"),
                ])
    async def set(self,interaction: discord.Interaction,type:app_commands.Choice[str], id: str):
        """
        This command is for setting the channels in which application threads are created, and voting tickets are processed in.
        """
        #Getting the config file
        config = await ReadConfig()
        #Changing the channel ID to the one given to us, the config.json is set up like :[ {"Applications": [{"Thread_Channel_ID": ID, "Voting_Channel_ID": ID}]... ] so ["Applications"][0][Type] would let us set the ID for the specified by the Type argument.
        config["Applications"][0][type.value] = int(id)
        #Writing the config back into the file.
        await WriteConfig(config)
        await interaction.response.send_message("Set channel.",ephemeral=True)

    @app_commands.command(
            name="application_message",
            description="Sends the application message with the buttons."
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def application_message(self,interaction: discord.Interaction):
        """
        This command sends the message that has the buttons for guild application.
        """
        #Creating the discord view that we will attach to the message and adding the 2 buttons to it. Pressing them will invoke their own respective Modals.
        view = discord.ui.View(timeout=None)
        view.add_item(GuildApplicationButton(interaction.user.id))
        view.add_item(CommunityApplicationButton(interaction.user.id))
        #Sending the actual message with the discord embed
        await interaction.channel.send(embed=discord.Embed(
            colour=discord.Color.green(),
            title='Applications',
            description="Something something guild application.\n\nSomething something community application"
        ), view=view)
        await interaction.response.send_message("Message created.",ephemeral=True)


async def setup(bot):
    await bot.add_cog(Setup(bot))