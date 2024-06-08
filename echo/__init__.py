from redbot.core.bot import Red

from .echo import echo

async def setup(bot: Red) -> None:
    await bot.add_cog(echo())
