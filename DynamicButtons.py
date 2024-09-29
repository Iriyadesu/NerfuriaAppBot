from __future__ import annotations

from discord.ext import commands
import discord
import re
import Modals

class GuildApplicationButton(discord.ui.DynamicItem[discord.ui.Button], template=r'guildapp:user:(?P<id>[0-9]+)'):
    """
    This class is for the application view. It's the button for people applying for the guild and when pressed invokes the guild app Modal.
    """
    def __init__(self, user_id: int) -> None:
        super().__init__(
            discord.ui.Button(
                label='Guild Application',
                style=discord.ButtonStyle.blurple,
                custom_id=f'guildapp:user:{user_id}',
                emoji='🪐',
            )
        )
        self.user_id: int = user_id

    # This is called when the button is clicked and the custom_id matches the template.
    @classmethod
    async def from_custom_id(cls, interaction: discord.Interaction, item: discord.ui.Button, match: re.Match[str], /):
        user_id = int(match['id'])
        return cls(user_id)

    async def callback(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_modal(Modals.GuildApplicationModal())


class CommunityApplicationButton(discord.ui.DynamicItem[discord.ui.Button], template=r'commapp:user:(?P<id>[0-9]+)'):
    """
    This class is for the application view. It's the button for people applying for community and when pressed invokes the comm app Modal.
    """
    def __init__(self, user_id: int) -> None:
        super().__init__(
            discord.ui.Button(
                label='Community Application',
                style=discord.ButtonStyle.blurple,
                custom_id=f'commapp:user:{user_id}',
                emoji='💞',
            )
        )
        self.user_id: int = user_id

    # This is called when the button is clicked and the custom_id matches the template.
    @classmethod
    async def from_custom_id(cls, interaction: discord.Interaction, item: discord.ui.Button, match: re.Match[str], /):
        user_id = int(match['id'])
        return cls(user_id)

    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        # Only allow the user who created the button to interact with it.
        return interaction.user.id == self.user_id

    async def callback(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message('This is your very own button!', ephemeral=True)


class VotingUpvoteButton(discord.ui.DynamicItem[discord.ui.Button], template=r'voteup:user:(?P<id>[0-9]+)'):
    """
    This class is for the voting view. It's for upvoting a nomination. It uses the interaction ID as it's identifier.
    """
    def __init__(self, context_id: int) -> None:
        super().__init__(
            discord.ui.Button(
                label='Upvote',
                style=discord.ButtonStyle.blurple,
                custom_id=f'voteup:user:{context_id}',
                emoji='✅',
            )
        )
        self.context_id: int = context_id


    # This is called when the button is clicked and the custom_id matches the template.
    @classmethod
    async def from_custom_id(cls, interaction: discord.Interaction, item: discord.ui.Button, match: re.Match[str], /):
        user_id = int(match['id'])
        return cls(user_id)

    async def callback(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"Upvoted. {self.context_id}")

class VotingDownvoteButton(discord.ui.DynamicItem[discord.ui.Button], template=r'votedown:user:(?P<id>[0-9]+)'):
    """
    This class is for the voting view. It's for downvoting a nomination. It uses the interaction ID as it's identifier.
    """
    def __init__(self, context_id: int) -> None:
        super().__init__(
            discord.ui.Button(
                label='Downvote',
                style=discord.ButtonStyle.blurple,
                custom_id=f'votedown:user:{context_id}',
                emoji='❌',

            )
        )
        self.context_id: int = context_id

    # This is called when the button is clicked and the custom_id matches the template.
    @classmethod
    async def from_custom_id(cls, interaction: discord.Interaction, item: discord.ui.Button, match: re.Match[str], /):
        user_id = int(match['id'])
        return cls(user_id)

    async def callback(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"Downvoted. {self.context_id}")

