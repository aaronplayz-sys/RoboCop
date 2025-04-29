from redbot.core.bot import Red

from .linkstoplaylist import linkstoplaylist

async def setup(bot: Red) -> None:
    await bot.add_cog(linkstoplaylist(bot))