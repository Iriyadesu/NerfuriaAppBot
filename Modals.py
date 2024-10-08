import discord
from Helper.Config import ReadConfig, WriteConfig

class GuildApplicationModal(discord.ui.Modal, title= "Guild Application"):
    """
    This class is for the guild application view. It's invoked when someone presses the guild application button, and opens a thread once it's filled out.
    """
    #The inputs for the Modal the user will be filling out.
    user_name = discord.ui.TextInput(label="Minecraft Username", placeholder="eg. KevinMarryMe", required=True, max_length=100,style=discord.TextStyle.short)
    highest_level = discord.ui.TextInput(label="Highest Combat Level", placeholder="eg. 106", required=True, max_length=3,style=discord.TextStyle.short)
    previous_guilds = discord.ui.TextInput(label="Previous Guilds", placeholder="Please tell us what guilds you've been in and why you left. eg. Nerfuia - Left because of Kevinovicc", required=True, max_length=1000,style=discord.TextStyle.paragraph)

    async def on_submit(self, interaction: discord.Interaction):
        #Reading the config to know what channel to create the thread in.
        config = await ReadConfig()
        #thread_channel to create the thread in.
        #voting_channel to send a notification that somneone created a ticket.
        thread_channel = discord.utils.get(interaction.guild.channels,id=config["Applications"][0]["Thread_Channel_ID"])
        voting_channel = discord.utils.get(interaction.guild.channels,id=config["Applications"][0]["Voting_Channel_ID"])
        #Creates the thread, and names it after the person applying. After the thread is created it sends an embed with the information the user supplied.
        thread = await thread_channel.create_thread(
        name=f"{self.user_name}",
        type=discord.ChannelType.private_thread)
        await thread.add_user(interaction.user)
        Thread_Embed = discord.Embed(
            title="Guild Application",
            description=f"\n\n\n**Minecraft Username:** \n{self.user_name}\n**Highest Combat Level:** \n{self.highest_level}\n**Previous Guilds:** \n{self.previous_guilds}",
        )
        Thread_Embed.set_thumbnail(url=interaction.user.display_avatar.url)
        await thread.send(embed=Thread_Embed)
        await voting_channel.send(f"{self.user_name} has created an application. See here: {thread.jump_url}")
        await interaction.response.send_message(f"Your application has been processed. Head to {thread.jump_url} for updates.",ephemeral=True)
        
        
    