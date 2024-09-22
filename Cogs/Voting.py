import discord
from discord.ext import commands
from discord import app_commands
from DynamicButtons import VotingUpvoteButton, VotingDownvoteButton

class Voting(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
            name="nominate",
            description="Nominates someone from the guild"
    )
    async def nominate(self,interaction: discord.Interaction, username: str, reason: str):
        view = discord.ui.View(timeout=None)
        view.add_item(VotingUpvoteButton(context_id=interaction.id, IsDisabled=False))
        view.add_item(VotingDownvoteButton(context_id=interaction.id, IsDisabled=False))
        await interaction.channel.send(f"{interaction.user.name} nominated {username} for reasons: {reason}", view=view)
        await interaction.response.send_message("Nominated", ephemeral=True)

    async def cog_command_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message(error)
        

async def setup(bot):
    await bot.add_cog(Voting(bot))