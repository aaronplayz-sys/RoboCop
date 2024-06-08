from redbot.core import commands
from redbot.core.bot import Red
import discord
import asyncio


class echo(commands.Cog):
  """Repeats user input!"""
  
  @commands.hybrid_command(name="echo", description="Repeats user input!")
  async def echo(self, ctx: commands.Context, *, message=None):
    """This commands gives users the ability to make the bot repeat their words. Handy if you want the bot to say something instead of you!"""
    message = message or "The message can not be blank, add something!"
    await ctx.send(message)
