import discord

from redbot.core import commands, app_commands
from discord import app_commands
from discord.ext import commands

class slashtest(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command()
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello World!", ephemeral=True)