# RoboCop

Cogs developed, and/ or modified by me. They can be used in your bot as long I receive credit.

[![badge](https://img.shields.io/badge/AaronPlayz-RoboCop_Cogs-blueviolet?logo=python&logoColor=blueviolet)](https://aaronplayzgaming.gq/) [![](https://img.shields.io/badge/Red%20DiscordBot-V3-red.svg)](https://github.com/Cog-Creators/Red-DiscordBot)

## Contact me

If you have any issues with any of the cogs, <a href="https://github.com/aaronplayz-sys/RoboCop/issues">open an issue on GitHub</a>.

## How to install

[p] = your bot's prefix (ex. !, ?, -)

Type `[p]repo add RoboCop https://github.com/aaronplayz-sys/RoboCop/` to add the repo.

Type `[p]cog install RoboCop <cog>` to install your desired cog.

## Cogs

Click on the cog names to get to my wiki page and learn about them.

***I highly suggest reading through the guides as some cogs may be a bit complicated!*** 
I take no responsibility for misuse of my cogs.

| Name | Description | Hybrid cog? |
| --- | --- | --- |
| [**BROKEN**] [animote](https://github.com/aaronplayz-sys/RoboCop/tree/main/animote) | lets you send animated emotes! | No |
| [echo](https://github.com/aaronplayz-sys/RoboCop/tree/main/echo) | A command that repeats the user's input back into them | Yes |
| [vcrename](https://github.com/aaronplayz-sys/RoboCop/tree/main/vcrename) | lets you & admin's change a voice channel's name with a command! | Yes |
| [slashtest](https://github.com/aaronplayz-sys/RoboCop/tree/main/slashtest) | This commands simply returns 'Hello World'. *Temporary cog* | Yes |

## Modified cogs

| Cog name | What was modified | Original repo or source | Why? |
| --- | --- | --- | --- |
| Tube | `__init__.py` | [CBD-cogs](https://gitlab.com/CrunchBangDev/cbd-cogs) | `bot.add_cog(Tube(bot))` was not awaited cause the cog to not be loaded. |
| [slashsync](https://github.com/aaronplayz-sys/RoboCop/tree/main/slashsync) | swapped imports and `bot.command()` to be compatible with red and made into a cog. | [about.abstractumbra.dev](https://about.abstractumbra.dev/discord.py/2023/01/29/sync-command-example.html) | was not a cog to begin with.

## Changelog
6/10/2024

The vcrename now works, removed local error handling it triggers more errors, using a loop to spit out success message when it did not anything. Might make this a 100% slash command, as it is better.

To-do:
- Attempt to fix animote, and make the cog a hybrid cog.
- Make Tube cog, a hybrid cog