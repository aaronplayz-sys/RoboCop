from redbot.core.bot import Red

from .vcrename import vcrename

async def setup(bot: Red) -> None:
    await bot.add_cog(vcrename())