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
    async def nominate(self,interaction: discord.Interaction, user: discord.Member, reason: str):
        view = discord.ui.View(timeout=None)
        view.add_item(VotingUpvoteButton(context_id=interaction.id))
        view.add_item(VotingDownvoteButton(context_id=interaction.id))
        await interaction.channel.send(f"{interaction.user.name} nominated {user.mention} for reasons: {reason}", view=view)
        await interaction.response.send_message("Nominated", ephemeral=True)

        

async def setup(bot):
    await bot.add_cog(Voting(bot))