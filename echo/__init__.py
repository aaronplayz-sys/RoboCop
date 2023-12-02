from .echo import Echo

async def setup(bot):
    cog = Echo(bot)
    await bot.add_cog(Echo())
