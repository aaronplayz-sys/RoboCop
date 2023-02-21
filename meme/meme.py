import discord
from redbot.core import commands
import asyncpraw
import random

reddit = asyncpraw.Reddit(
    user_agent="Chrome",
    client_id="INPUTID",
    client_secret="INPUTSECRET",
    username="urbotusername",
    password="urbotpassword",
)

class Meme(commands.Cog):
    @commands.guild_only()
    @commands.command(name='meme')
    async def meme(self, ctx):
        """
        Generates a meme from Reddit
        """
        await ctx.send("Retreving...")

        subreddit = await reddit.subreddit("dankmemes", fetch=True)
        all_subs = []

        top = subreddit.top(limit = 50)

        async for submission in top:
            all_subs.append(submission)
        
        random_sub = random.choice(all_subs)

        name = random_sub.title
        url = random_sub.url

        embed = discord.Embed(title = name)

        embed.set_image(url=url)
        embed.set_footer(text="NOTE: This command is a W.I.P.")

        await ctx.send(embed=embed)
