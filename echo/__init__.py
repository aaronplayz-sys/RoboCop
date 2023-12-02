from .echo import Echo

def setup(bot):
    cog = Echo(bot)
    bot.add_cog(Echo())
