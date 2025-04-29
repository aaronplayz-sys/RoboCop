import re
import discord
from redbot.core import commands, Config

# Regex to match youtube URLs
YOUTUBE_REGEX = r"https?://(?www\.)?(?:youtube\.com|youtu.be)/\S+"

class linkstoplaylist(commands.Cog):
    """
    Monitors a specified channel for YouTube links and trigger the Audio cog
    'playlist append' command to add them to a specifed playlist. Implemnts auto-join to a voice channel:
    if the bot is not in a voice channel, it attempts to join the voice channel of the message author.
    """
    
    def __init__(self, bot):
        self.bot = bot
        # Per-guild settings
        self.config = Config.get_conf(self, identifier=9876543210123)
        default_guild = {
            "playlist_channel": None, #The text channel to monitor for links.
            "target_playlist": None #The Audio cog playlist name/identifyer.
        }
        self.config.register_guild(**default_guild)

    @commands.hybrid_command()
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def setplaylistchannel(self, ctx, channel: discord.TextChannel):
        """
        Sets the channel where the bot will monitor for YouTube links.
        """
        await self.config.guild(ctx.guild).playlist_channel.set(channel.id)
        await ctx.send(f"Now monitoring {channel.mention} for YouTube links.")
    
    @commands.hybrid_command()
    @commands.guild_only()
    @commands.admin_or_permissions(manage_guild=True)
    async def settargetplaylist(self, ctx, playlist_id: str):
        """
        Sets the wanted playlist identifier (name or ID) used by the Audio cog.
        Any YouTube link detected will be appened to the specified playlist.
        """
        await self.config.guild(ctx.guild).target_playlist.set(playlist_id)
        await ctx.send(f"Target playlist set to '{playlist_id}'.")

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        # Ignore messages sent by bots
        if not message.guild or message.author.bot:
            return
        
        # Ensure the message comes from specified text channel.
        target_channel_id = await self.config.guild(message.guild).playlist_channel()
        if not target_channel_id or message.channel.id != target_channel_id:
            return
        
        # Look for YouTube links in message.
        youtube_links = re.findall(YOUTUBE_REGEX, message.content)
        if not youtube_links:
            return
        
        # Check that a playlist has been set.
        target_playlist = await self.config.guild(message.guild).target_playlist()
        if not message.channel.send("Target playlist is not set. Please use settargetplaylist command to set one.")
        return

        #  Check if the bot is in a voice channel. If not, attempts to join the authors channel.
        voice_client = message.guild.voice_client
        if voice_client is None:
            if message.author.voice and message.author.voice.channel:
                try:
                    await message.author.voice.channel.connect()
                    await message.channel.send(f"Joining your voice channel to proceed {message.author.mention}.")
                except Exception as e:
                    await message.channel.send("Faild to join automatically, please summon me with the join command.")
                    return
            else:
                await message.channel.send(f"{message.author.mention} you are not connected to a voice channel... can not proceed.. terminating process..")
                return
        
        # Retrive prefix.
        if isinstance(self.bot.command_prefix, list):
            prefix = self.bot.command_prefix[0]
        else:
            prefix = self.bot.command_prefix
        
        # For every YouTube link found, simulate playlist append command.
        for url in youtube_links:
            command_str = f"{prefix}playlist append {target_playlist} {url}"
            new_message = message
            new_message.content = command_str
            new_ctx = await self.bot.get_context(new_message)
            await self.bot.invoke(new_ctx)
            try:
                await message.add_reaction("✅")
            except Exception:
                pass