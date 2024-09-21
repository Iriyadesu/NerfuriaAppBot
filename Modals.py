import discord

class GuildApplicationModal(discord.ui.Modal, title= "Guild Application"):
    user_name = discord.ui.TextInput(label="Minecraft Username", placeholder="eg. KevinMarryMe", required=True, max_length=100,style=discord.TextStyle.short)
    highest_level = discord.ui.TextInput(label="Highest Combat Level", placeholder="eg. 106", required=True, max_length=3,style=discord.TextStyle.short)
    previous_guilds = discord.ui.TextInput(label="Previous Guilds", placeholder="Please tell us what guilds you've been in and why you left. eg. Nerfuia - Left because of Kevinovicc", required=True, max_length=1000,style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        await interaction.response.send_message("Your application has been processed",ephemeral=True)
        thread = await interaction.channel.create_thread(
        name=f"{self.user_name}",
        type=discord.ChannelType.public_thread)
        await thread.add_user(interaction.user)
        Embed = discord.Embed(
            title="Guild Application",
            description=f"\n\n\n**Minecraft Username:** \n{self.user_name}\n**Highest Combat Level:** \n{self.highest_level}\n**Previous Guilds:** \n{self.previous_guilds}",
        )
        Embed.set_thumbnail(url=interaction.user.display_avatar.url)
        await thread.send(embed=Embed)
        
        
    