import discord
from redbot.core import commands
import asyncpraw
import random

reddit = asyncpraw.Reddit(
    user_agent="RoboCop-8070",
    client_id="7FoQYOQIEsx6DA",
    client_secret="kGtpyGAyuZ8Zp_aBxbj3I3wGGj8SZA",
    username="RoboCop-8070",
    password="qVxjMuUnZigh35s",
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
