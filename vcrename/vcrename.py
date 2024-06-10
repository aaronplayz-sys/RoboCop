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
