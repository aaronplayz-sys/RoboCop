from redbot.core import commands
from redbot.core.bot import Red
import discord

class vcrename(commands.Cog):
  """Gives server owners and admins ability to rename voice channels via chat."""

  @commands.hybrid_command(name="vcrename", description="Rename voice channels via chat.")
  @commands.has_permissions(manage_channels=True)
  async def vcrename(self, ctx: commands.Context, channel: discord.VoiceChannel, *, new_name):
    await channel.edit(name=new_name)
    embed = discord.Embed(
      color=discord.Color.dark_green()
    )

    embed.add_field(name='Sucess!', value='The voice channel has been updated!')

    await ctx.send(embed=embed)

  @vcrename.error
  async def vcrename_error(self, ctx: commands.Context, error):
    if isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(
        color=discord.Color.Dark_red()
      )

      embed.add_field(name='Sorry, looks like you do not have the right permissions.', value='Do you have the manage channel permission?')

      await ctx.send(embed=embed)
    
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.embed(
        color=discord.Color.gold()
      )

      embed.add_field(name='Looks like you forgot something...', value='Syntax: [Prefix]vcrename "VoiceChanelName" NewVoiceChannelName')

      await ctx.send(embed=embed)