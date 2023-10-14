# Microbot
Microbot is a simple and compact bot for Discord and Revolt. Powered by Disnake (discord.py fork), Voltage for Revolt Chat API and SQLite for databases. Writen on Python programming language.

### Links

[Show screenshots](https://github.com/tinelix/microbot/tree/main/Screenshots) | [Add to Discord server](https://discordapp.com/api/oauth2/authorize?client_id=994906248526970951&permissions=2147862592&scope=bot) | [Add to Revolt server](https://app.revolt.chat/bot/01GAWYPXPN741ESRZS6T0ZBVGQ)

### Installation manual (for Discord)
1. Download or clone this repository with Git: `git clone https://github.com/tinelix/microbot.git`
2. In `discord_api` folder, create `Database` required folder for SQLite DB storage.
3. If running Windows, in `discord.bat` file, replace `your_token_here` to your Discord bot token. Or if running Linux or UNIX-like OS, in `discord.sh` file, replace `your_token_here` to your Discord bot token. 

   #### Notes:
   1. The token can be obtained from [Discord developer portal](https://discord.com/developers).
   2. To protect against bot hacks, before commiting we strongly advise you to disable change tracking for *.bat and *.sh files using the line: `git update-index --assume-unchanged *.bat *.sh`
    
5. Run script.

### Installation manual (for Revolt)
1. Download or clone this repository with Git: `git clone https://github.com/tinelix/microbot.git`
2. In `revolt_api` folder, create `Database` required folder for SQLite DB storage.
3. If running Windows, in `revolt.bat` file replace `your_token_here` to your Revolt bot token. If running Linux or UNIX-like OS, in `revolt.sh` file replace `your_token_here` to your Revolt bot token.

   #### Notes:
   1. The token can be obtained from Revolt web client: 'Settings' → 'My Bots' → 'Token' → 'Reveal'.
   2. To protect against bot hacks, before commiting we strongly advise you to disable change tracking for *.bat and *.sh files using the line: `git update-index --assume-unchanged *.bat *.sh`
4. Run script.

### License

Apache License 2.0 & GNU Affero GPL 3.0 (or higher)

###### Created by Dmitry Tretyakov (aka Tinelix)
