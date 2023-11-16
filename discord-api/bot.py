#   Tinelix Microbot
#   -------------------------------------------------------------------------------------------
#   Copyright © 2023 Dmitry Tretyakov (aka. Tinelix)
#
#   This program is free software: you can redistribute it and/or modify it under the terms of
#   the GNU Affero General Public License 3 (or any later version) and/or Apache License 2
#   See the following files in repository directory for the precise terms and conditions of
#   either license:
#
#       LICENSE.APACHE
#       LICENSE.AGPL
#
#   Please see each file in the implementation for copyright and licensing
#   information, (in the opening comment of each file).

# 1. Importing main libraries (5-16)
import disnake
import os
import traceback
import datetime
import time
import sqlite3
import pytz
import sys
import argparse
import threading

# 2. Importing modular commands
from disnake.ext import commands
from Utilities import *
from cogs import Commands, Listeners

# 3. Importing bot configuration
from config import *

setupwiz.gen_config_file(sys, config, links)

# 4. Set the logger
def write_log_file(text):
    log_file = open("microbot-discord.log", "w+")
    log_file.write(text)
    log_file.close()

# 5. Initializing SQLite3 server
try:
    print("\r\n Connecting with SQLite database...")
    database = sqlite3.connect('Database/main.db')
    print("\033[92m SQLite datebase connected!\033[0m")
    cursor = database.cursor()
except sqlite3.Error as e:
    print("\033[91m SQLite Error: {0}\r\n".format(e))
    print("\033[0m If 'Database' directory not yet created,"
        "\r\n create manually inside 'discord-api' directory and try again.\r\n")
    sys.exit()

# 6. Getting custom guild prefix
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


# 7. Creating Discord bot instance with all intents
print(" Preparing to running {0}...".format(config['name']))
intents = disnake.Intents.all()
bot = commands.AutoShardedBot(command_prefix=get_guild_prefix, intents=intents)
bot.remove_command('help')
bot.add_cog(Listeners(bot, database, cursor))
bot.add_cog(Commands(bot, database, cursor))

bot.commands_list = {
        'main': ['help', 'about', 'user', 'guild', 'ping'],
        'fun': ['8ball', 'rngen'],
        'interactivity': ['weather', 'wiki'],
        'personalization': ['settings'],
        'other': ['calc', 'codec', 'timers', 'publish']
    }

language = 'ru_RU'
user_col = None
guild_col = None
connectionStartTime = time.time()

# 8. Globally blocking all DMs
@bot.check
async def no_DM(ctx):
    return ctx.guild is not None

bot.run(tokens['discord_api'])
