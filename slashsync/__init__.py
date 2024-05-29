from redbot.core.bot import Red

from .slashsync import slashsync

async def setup(bot: Red) -> None:
    await bot.add_cog(slashsync())