import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_command_error(self,ctx: commands.Context, error: Exception):
        await ctx.send(
            embed=discord.Embed(error.__cause__)
        )

async def setup(bot):
    await bot.add_cog(Events(bot))