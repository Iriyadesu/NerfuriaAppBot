import discord
from discord.ext import commands
from DynamicButtons import GuildApplicationButton, CommunityApplicationButton
from discord import app_commands

class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #Slash commands for the bot. The name must be all lowercase no spaces. Use interaction.x instead of context. Must use interaction.response to avoid an error message.

    @app_commands.command(
            name="application_message",
            description="Sends the application message with the buttons."
    )
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

    @commands.command()
    async def SendApplicationMessage(self, ctx: commands.Context):
        """Starts a dynamic button."""

        view = discord.ui.View(timeout=None)
        view.add_item(GuildApplicationButton(ctx.author.id))
        view.add_item(CommunityApplicationButton(ctx.author.id))
        await ctx.send(embed=discord.Embed(
            colour=discord.Color.green(),
            title='Applications',
            description="Something something guild application.\n\nSomething something community application"
        ), view=view)


async def setup(bot):
    await bot.add_cog(Setup(bot))