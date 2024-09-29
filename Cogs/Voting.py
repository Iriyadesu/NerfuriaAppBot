import discord
from discord.ext import commands
from discord import app_commands
from DynamicButtons import VotingUpvoteButton, VotingDownvoteButton

class Voting(commands.Cog):
    """
    This class is reponsible for handling all the voting related commands. 
    Work in progress.
    """
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(
            name="nominate",
            description="Nominates someone from the guild"
    )
    async def nominate(self,interaction: discord.Interaction, user: discord.Member, reason: str):
        """
        This command is for nominating someone for a promotion. Highly unfinished and everything is a placeholder for now.
        """
        #Creating the view and attaching the buttons to it.
        view = discord.ui.View(timeout=None)
        view.add_item(VotingUpvoteButton(context_id=interaction.id))
        view.add_item(VotingDownvoteButton(context_id=interaction.id))
        #Sending the discord message with the view added.
        await interaction.channel.send(f"{interaction.user.name} nominated {user.mention} for reasons: {reason}", view=view)
        await interaction.response.send_message("Nominated", ephemeral=True)

        

async def setup(bot):
    await bot.add_cog(Voting(bot))