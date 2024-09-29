import discord
from discord.ext import commands
from DynamicButtons import GuildApplicationButton, CommunityApplicationButton
from discord import app_commands
import json
from Helper.Config import ReadConfig, WriteConfig

class Setup(commands.Cog):
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
        config = await ReadConfig()
        config["Applications"][0][type.value] = int(id)
        await WriteConfig(config)
        await interaction.response.send_message("Set channel.",ephemeral=True)

    @app_commands.command(
            name="application_message",
            description="Sends the application message with the buttons."
    )
    @app_commands.checks.has_permissions(administrator=True)
    async def application_message(self,interaction: discord.Interaction):
        """Starts a dynamic button."""

        view = discord.ui.View(timeout=None)
        view.add_item(GuildApplicationButton(interaction.user.id))
        view.add_item(CommunityApplicationButton(interaction.user.id))
        await interaction.channel.send(embed=discord.Embed(
            colour=discord.Color.green(),
            title='Applications',
            description="Something something guild application.\n\nSomething something community application"
        ), view=view)
        await interaction.response.send_message("Message created.",ephemeral=True)

    # @commands.command()
    # async def SendApplicationMessage(self, ctx: commands.Context):
    #     """Starts a dynamic button."""

    #     view = discord.ui.View(timeout=None)
    #     view.add_item(GuildApplicationButton(ctx.author.id))
    #     view.add_item(CommunityApplicationButton(ctx.author.id))
    #     await ctx.send(embed=discord.Embed(
    #         colour=discord.Color.green(),
    #         title='Applications',
    #         description="Something something guild application.\n\nSomething something community application"
    #     ), view=view)

    


async def setup(bot):
    await bot.add_cog(Setup(bot))