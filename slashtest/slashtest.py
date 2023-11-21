import discord

from redbot.core import commands, app_commands, bot

class slashtest(commands.Cog):
    def __init__(self, bot: bot.Red):
        self.bot = bot
    
    @app_commands.command()
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message("Hello World!", ephemeral=True)