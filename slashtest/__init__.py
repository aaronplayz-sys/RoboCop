from redbot.core.bot import Red

from .slashtest import slashtest

async def setup(bot: Red):
    await bot.add_cog(slashtest(bot))