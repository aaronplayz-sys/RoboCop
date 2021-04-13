from redbot.core import commands
import discord

class VcRename(commands.Cog):

  @commands.command(
    name='vcrename',
    aliases=['vcre']
  )
  @commands.has_permissions(manage_channels=True)
  async def vcrename(self, ctx, channel: discord.VoiceChannel, *, new_name):
    await channel.edit(name=new_name)
    embed = discord.Embed(
      color = discord.Color.dark_green()
    )

    embed.add_field(name='Success!', value='The voice channel has been updated successfully!')
    
    
    await ctx.send(embed=embed)

  @vcrename.error
  async def vcrename_error(self, ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(
        color = discord.Color.dark_red()
      )

      embed.add_field(name='Sorry, looks like you do not have the right permissions', value='Do you have the manage channel permission?')


      await ctx.send(embed=embed)
    if isinstance(error, commands.MissingRequiredArgument):
      embed = discord.Embed(
        color = discord.Color.gold()
      )

      embed.add_field(name='Looks like you forgotten to add something....', value='Ex. >vcrename "VoiceChannelName" NewVoiceChannelName')


      await ctx.send(embed=embed)