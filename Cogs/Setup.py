import discord
from discord.ext import commands
from DynamicButtons import GuildApplicationButton, CommunityApplicationButton

class Setup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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