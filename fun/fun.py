from redbot.core import commands
import discord
import random

WotarLinks = ["https://www.scienceabc.com/wp-content/uploads/2016/04/water-meme.jpg", "https://media.makeameme.org/created/Water-Water-Everywhere.jpg", "https://aaronplayzgaming.gq/wp-content/uploads/2020/08/watermeme1.png", "https://cdn.discordapp.com/attachments/417837573256380426/744421558193356831/l9iagtff2tb21.png"]

AnimeLinks = ["https://i.redd.it/pwa93m21f7y51.jpg", "https://i.redd.it/q3jcu7v007y51.jpg", "https://i.redd.it/tujr2ekmt8y51.png", "https://i.redd.it/49cratyww6y51.jpg", "https://i.redd.it/utrg3xtw08y51.jpg", "https://i.redd.it/68yea01jw8y51.jpg", "https://i.redd.it/bk8xwq9hk8y51.jpg", "https://i.redd.it/iw7ldik989y51.png", "https://i.redd.it/u7h5lxtsf8y51.jpg", "https://i.redd.it/7u2h437we6x51.jpg", "https://i.redd.it/psbongy858y51.jpg", "https://i.redd.it/k6bmas9219y51.jpg", "https://i.redd.it/6t554kx5hay51.jpg", "https://i.redd.it/9wbnvqc6s1y51.jpg" , "https://i.redd.it/juehssyyy8y51.jpg", "https://i.redd.it/qten1zq9iis51.png", "https://i.redd.it/py4s27ac33y51.jpg", "https://i.redd.it/cf44n08r7zx51.jpg", "https://i.redd.it/if0mikf4xzx51.jpg"]

class Fun(commands.Cog):

  @commands.command(
    name='wotar'
  )
  async def wotar(self, ctx):
    choosen_image = random.choice(WotarLinks)

    embed = discord.Embed(
      color=0x00ffff

    )

    embed.set_author(name='HERE TAKE SOME WOTAR')
    embed.set_image(url=choosen_image)
    embed.set_footer(text=f"Requested by: {ctx.author.name}")


    await ctx.send(embed=embed)

  @wotar.error
  async def wotar_error(self, ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
      await ctx.send('Looks like I can not send embeds here... I recommend you give me the embed permission to my role to prevent this error from happening again.')

  @commands.command(
    name='anime'
  )
  async def anime(self, ctx):
    choosen_image = random.choice(AnimeLinks)

    embed = discord.Embed(
      color=0xf6a3ef
    )

    embed.set_author(name='Here, take some hawt anime memes')
    embed.set_image(url=choosen_image)
    embed.set_footer(text=f"Requested by: {ctx.author.name}")


    await ctx.send(embed=embed)

  @anime.error
  async def anime_error(self, ctx, error):
    if isinstance(error, commands.BotMissingPermissions):
      await ctx.send('Looks like I can not send embeds here... I recommend you give me the embed permission to my role to prevent this error from happening again.')
