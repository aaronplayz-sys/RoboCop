from redbot.core import bot, commands
import discord
import asyncio

class Echo(commands.Cog):
  
  def __init__(self, bot: bot.Red):
    self.bot = bot
  
  @commands.command()
  async def echo(self, ctx, *, message=None):
    """
    A command that repeats the users input back into them
    """
    message = message or "I can't repeat nothing! Add a message for me to mimic!"
   # await ctx.message.delete()
    await ctx.send(message)
