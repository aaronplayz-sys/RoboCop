from redbot.core.bot import Red
from .animote import Emoji

async def setup(bot: Red) -> None:
    await bot.add_cog(Emoji())