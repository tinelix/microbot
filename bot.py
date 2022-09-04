# Den4ik Bot
# Created by tretdm (aka. tinelix) at 2022-08-18 from Den4ik
# Based on Microbot Discord bot: https://github.com/tinelix/microbot.
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher.

# 1. Importing main libraries (5-16)
import disnake
import os
import traceback
import datetime
import time
import sqlite3
import pytz

# 2. Importing modular commands
from disnake.ext import commands
from Utilities import *
from cogs import Commands, Listeners

# 3. Importing bot configuration
from config import *

# 4. Initializing SQLite3 server
try:
    database = sqlite3.connect('Database/main.db')
    print(" SQLite datebase connected!")
    cursor = database.cursor()
except sqlite3.Error as e:
    print(" Exception: {0}".format(e))

# 5. Getting custom guild prefix
prefixes = {}

async def get_guild_prefix(bot, message):
    cursor.execute("SELECT id, prefix FROM guilds;")
    guild_data = cursor.fetchall()
    for guild in guild_data:
        if message.guild.id == guild[0]:
            prefixes[f'{guild[0]}'] = guild[1]
    try:
        if(prefixes[f'{message.guild.id}']):
            return [config['prefix'], prefixes[f'{message.guild.id}']]
        else:
            return config['prefix']
    except Exception as e:
        return config['prefix']

# 6. Creating Discord bot instance with all intents
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix=get_guild_prefix, intents=intents, sync_commands_debug=True)
bot.remove_command('help')
bot.add_cog(Listeners(bot, database, cursor))
bot.add_cog(Commands(bot, database, cursor))

bot.commands_list = {
        'main': ['help', 'about', 'user', 'guild', 'ping'],
        'fun': ['8ball', 'rngen'],
        'personalization': ['settings'],
        'other': ['calc']
    }

language = 'ru_RU'
user_col = None
guild_col = None
connectionStartTime = time.time()

# 7. Globally blocking all DMs
@bot.check
async def no_DM(ctx):
    return ctx.guild is not None

bot.run(tokens['discord_api'])
