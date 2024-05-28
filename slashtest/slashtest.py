import discord

from redbot.core import commands, app_commands
from redbot.core import Red

class slashtest(commands.Cog):
    def __init__(self, bot: Red) ->  None:
        self.bot = bot
    
    @app_commands.command()
    async def hello(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message("Hello World!", ephemeral=True)