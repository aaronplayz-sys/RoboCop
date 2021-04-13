from redbot.core import commands
import discord

class Echo(commands.Cog):
  
  @commands.Cog.listener()
  async def on_ready(self):
    print("echo cog has been loaded")
  
  @commands.command()
  async def echo(self, ctx, *, message=None):
    """
    A command that repeats the users input back into them
    """
    message = message or "I can't repeat nothing! Add a message for me to mimic!"
   # await ctx.message.delete()
    await ctx.send(message)
