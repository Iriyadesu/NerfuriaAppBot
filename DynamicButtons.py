from __future__ import annotations

from discord.ext import commands
import discord
import re
import Modals

class GuildApplicationButton(discord.ui.DynamicItem[discord.ui.Button], template=r'guildapp:user:(?P<id>[0-9]+)'):
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