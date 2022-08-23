# Microbot Revolt bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

# 1. Importing main libraries (5-16)
import voltage       # for install type 'pip install git+https://github.com/EnokiUN/voltage'
import platform
import os
import json
import traceback
import glob
import sys
import datetime
import time
from platform import python_version
import sqlite3

# 2. Importing modular commands
from voltage.ext import commands
from Commands import *

# 3. Importing utilities
from Utilities import *

# 4. Importing bot configuration
from config import *

class HelpCommand:
    def __init__(self, client: commands.CommandsClient):
        self.client = client
        self.commands_list = ['help', 'about', 'user', 'guild', '8ball', 'rngen', 'calc', 'settings', 'publish', 'ping', 'weather', 'wiki', 'codec']

    async def send_help(self, ctx: commands.CommandContext):
        #server_data = await sync_db(ctx, 'servers', 'regular')
        #language = guild_data[1]
        await help.sendRegularMsg(ctx, bot, config, links, language, voltage, self.commands_list, translator)

    async def send_command_help(self, ctx: commands.CommandContext, cmd):
        #server_data = await sync_db(ctx, 'servers', 'regular')
        #language = guild_data[1]
        await help.sendCmdHelpMsg(ctx, bot, links, config, language, voltage, translator, cmd.name)

    async def send_not_found(self, ctx: commands.CommandContext, arg):
        #server_data = await sync_db(ctx, 'servers', 'regular')
        #language = guild_data[1]
        await help.sendRegularMsg(ctx, bot, config, links, language, voltage, self.commands_list, translator)


# 6. Creating Revolt bot instance with all intents
bot = commands.CommandsClient(config['prefix'], help_command=HelpCommand)

# 7. Initializing SQLite3 server
try:
    database = sqlite3.connect('Database/main.db')
    print(" SQLite datebase connected!")
    cursor = database.cursor()
except sqlite3.Error as e:
    print(" Exception: {0}".format(e))

language = 'ru_RU'
user_col = None
guild_col = None
connectionStartTime = time.time()

# 8. Commands and events listener
@bot.listen("ready")
async def ready():
    connectionStartTime = time.time()
    await notifier.showWelcomeMessage(voltage, bot, config)
    await db.create_tables(database, cursor)

@bot.command(name="about", description=translator.translate('command_description', "about", "en_US"), aliases=["state", "health"])
async def about_cmd(ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-connectionStartTime))))
    #guild_data = await sync_db(ctx, 'guilds', 'regular')
    #language = guild_data[1]
    await about.sendRegularMsg(ctx, bot, config, links, language, voltage, translator, python_version, uptime)

@bot.command(name="guild", description=translator.translate('command_description', "guild", "en_US"), aliases=["server"])
async def guild_cmd(ctx):
    await server.sendRegularMsg(ctx, bot, config, language, voltage, translator)

@bot.command(name="user", description=translator.translate('command_description', "user", "en_US"), aliases=["member"])
async def user_cmd(ctx, arg):
    await user.sendRegularMsg(ctx, bot, config, language, voltage, translator, arg)

@bot.command(name="calc", description=translator.translate('command_description', "calc", "en_US"))
async def calc_cmd(ctx, *, arg):
    await calc.sendRegularMsg(ctx, bot, config, language, voltage, translator, arg)

@bot.command(name="wiki", description=translator.translate('command_description', "wiki", "en_US"))
async def wiki_cmd(ctx, *, arg):
    await wiki.sendRegularMsg(ctx, bot, config, language, voltage, translator, arg)

@bot.command(name="eval")
async def eval_cmd(ctx, *, arg):
    await eval.sendRegularMsg(ctx, bot, config, language, voltage, translator, arg)

@bot.command(name="rngen", description=translator.translate('command_description', "rngen", "en_US"), aliases=["rand"])
async def rngen_cmd(ctx, *, arg):
    await rngen.sendRegularMsg(ctx, bot, config, language, voltage, translator, arg)

@bot.command(name="8ball", description=translator.translate('command_description', "8ball", "en_US"))
async def eightball_cmd(ctx, *, arg):
    await eightball.sendRegularMsg(ctx, bot, config, language, voltage, translator, arg)

@bot.command(name="avatar", description=translator.translate('command_description', "avatar", "en_US"))
async def avatar_cmd(ctx, arg):
    await avatar.sendRegularMsg(ctx, bot, config, language, voltage, translator, arg)

@bot.error("message")
async def on_message_error(error: Exception, message):
    if isinstance(error, voltage.errors.NotEnoughArgs):
        await help.sendCmdHelpWithoutArgs(message, bot, config, language, voltage, translator)
    elif isinstance(error, voltage.errors.CommandNotFound):
        pass
    else:
        error_list = []
        error_text = "".join(traceback.TracebackException.from_exception(error).format())
        if(config['bugs_ch'] != ''):
            await bugreporter.send(message, bot, config, language, voltage, translator, error_text)
        else:
            print(error_text)

# 9. Database autosynchronization
async def sync_db(ctx, table, message_type):
    if(message_type == 'regular'):
        cursor = database.cursor()
        # for user values sync and cooldown
        if(await db.if_user_existed(database, cursor, ctx.message.author.id) == True):
            cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.message.author.id))
            user_data = cursor.fetchone()
            await db.update_value(ctx, database, cursor, 'users', 'sended_msg_timestamp', '\'{0}\''.format(ctx.created_at.strftime('%Y-%m-%d %H:%M:%S')), ctx.message.author.id)
        else:
            await db.add_user_value(database, ctx.message, cursor)
            cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.message.author.id))
            user_data = cursor.fetchone()
        # for server values sync and cooldown
        if(await db.if_server_existed(database, cursor, ctx.message.server.id) == True):
            cursor.execute("SELECT * FROM servers WHERE id='{0}';".format(ctx.message.server.id))
            guild_data = cursor.fetchone()
        else:
            language = 'en_US'
            await db.add_server_value(database, ctx.message.server, cursor)
            cursor.execute("SELECT * FROM servers WHERE id='{0}';".format(ctx.message.server.id))
            guild_data = cursor.fetchone()
        if(table == 'server'):
            return server_data
        else:
            return user_data
    else:
        cursor = database.cursor()
        # for user values sync and cooldown
        if(await db.if_user_existed(database, cursor, ctx.author.id) == True):
            cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.author.id))
            user_data = cursor.fetchone()
            await db.update_value(ctx, database, cursor, 'users', 'sended_msg_timestamp', '\'{0}\''.format(ctx.created_at.strftime('%Y-%m-%d %H:%M:%S')), ctx.author.id)
        else:
            await db.add_user_value(database, ctx, cursor)
            cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.author.id))
            user_data = cursor.fetchone()
        # for server values sync and cooldown
        if(await db.if_server_existed(database, cursor, ctx.server.id) == True):
            cursor.execute("SELECT * FROM servers WHERE id='{0}';".format(ctx.server.id))
            guild_data = cursor.fetchone()
        else:
            language = 'en_US'
            await db.add_server_value(database, ctx.server, cursor)
            cursor.execute("SELECT * FROM servers WHERE id='{0}';".format(ctx.server.id))
            guild_data = cursor.fetchone()
        if(table == 'guilds'):
            return guild_data
        else:
            return user_data

bot.run(tokens['revolt_api'])
