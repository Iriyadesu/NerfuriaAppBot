import discord

class GuildApplicationModal(discord.ui.Modal, title= "Guild Application"):
    user_name = discord.ui.TextInput(label="Minecraft Username", placeholder="eg. KevinMarryMe", required=True, max_length=100,style=discord.TextStyle.short)
    highest_level = discord.ui.TextInput(label="Highest Combat Level", placeholder="eg. 106", required=True, max_length=3,style=discord.TextStyle.short)
    previous_guilds = discord.ui.TextInput(label="Previous Guilds", placeholder="Please tell us what guilds you've been in and why you left. eg. Nerfuia - Left because of Kevinovicc", required=True, max_length=1000,style=discord.TextStyle.paragraph)