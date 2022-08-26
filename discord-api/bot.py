# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

# 1. Importing main libraries (5-16)
import disnake
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
import pytz

# 2. Importing modular commands
from disnake.ext import commands
from Commands import *

# 3. Importing utilities
from Utilities import *

# 4. Importing bot configuration
from config import *

# 5. Creating Discord bot instance with all intents
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix=config['prefix'], intents=intents, sync_commands_debug=True)
bot.remove_command('help')

bot.commands_list = ['help', 'about', 'user', 'guild', '8ball', 'rngen', 'calc', 'settings', 'publish', 'ping', 'weather', 'wiki', 'codec', 'timers']

language = 'ru_RU'
user_col = None
guild_col = None
connectionStartTime = time.time()
MSK = pytz.timezone('Europe/Moscow')

# 6. Initializing SQLite3 server
try:
    database = sqlite3.connect('Database/main.db')
    print(" SQLite datebase connected!")
    cursor = database.cursor()
except sqlite3.Error as e:
    print(" Exception: {0}".format(e))

# 5. Globally blocking all DMs
@bot.check
async def no_DM(ctx):
    return ctx.guild is not None

# 6. Events and message triggers
@bot.event
async def on_ready():
    connectionStartTime = time.time()
    await notifier.showWelcomeMessage(disnake, bot, config)
    await db.create_tables(database, cursor)

@bot.event
async def on_disconnect():
    print(" ERROR: Discord Gateway connection disconnected!")

@bot.event
async def on_guild_join(guild):
    await notifier.updateWelcomeMessage(disnake, bot, config)
    if(await db.if_guild_existed(database, cursor, guild.id) == False):
        await db.add_guild_value(database, guild, cursor)

@bot.event
async def on_guild_leave(guild):
    await notifier.updateWelcomeMessage(disnake, bot, config)

@bot.command(name="help", description=translator.translate('command_description', 'help', 'en_US'))
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def help_cmd(ctx, arg):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    user_data = await sync_db(ctx, 'users', 'regular')
    await help.sendCmdHelpMsg(ctx, bot, links, config, language, disnake, translator, arg)

@bot.slash_command(name="help", description=translator.translate('command_description', 'help', 'en_US'))
async def help_scmd(ctx):
    guild_data = await sync_db(ctx, 'guilds', 'slash')
    language = guild_data[1]
    await help.sendSlashMsg(ctx, bot, config, links, language, disnake, translator)

@bot.command(name="about", description=translator.translate('command_description', 'about', 'en_US'), aliases=['state', 'check'])
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def about_cmd(ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-connectionStartTime))))
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    user_data = await sync_db(ctx, 'users', 'regular')
    await about.sendRegularMsg(ctx, bot, config, links, language, disnake, translator, python_version, uptime)

@bot.slash_command(name="about", description=translator.translate('command_description', 'about', 'en_US'))
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def about_scmd(ctx):
    uptime = str(datetime.timedelta(seconds=int(round(time.time()-connectionStartTime))))
    guild_data = await sync_db(ctx, 'guilds', 'slash')
    language = guild_data[1]
    await about.sendSlashMsg(ctx, bot, config, links, language, disnake, translator, python_version, uptime)

@bot.command(name="user", description=translator.translate('command_description', 'user', 'en_US'), aliases=['member'])
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def user_cmd(ctx, arg):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    user_data = await sync_db(ctx, 'users', 'regular')
    await user.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg)

@bot.slash_command(name="user", description=translator.translate('command_description', 'user', 'en_US'))
async def user_scmd(ctx, member):
    guild_data = await sync_db(ctx, 'guilds', 'slash')
    language = guild_data[1]
    await user.sendSlashMsg(ctx, bot, config, language, disnake, translator, member)

@bot.command(name="avatar", description=translator.translate('command_description', 'avatar', 'en_US'))
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def avatar_cmd(ctx, arg):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    user_data = await sync_db(ctx, 'users', 'regular')
    await avatar.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg)

@bot.slash_command(name="avatar", description=translator.translate('command_description', 'avatar', 'en_US'))
async def avatar_scmd(ctx, member):
    guild_data = await sync_db(ctx, 'guilds', 'slash')
    language = guild_data[1]
    await avatar.sendSlashMsg(ctx, bot, config, language, disnake, translator, member)

@bot.command(name="8ball", description=translator.translate('command_description', '8ball', 'en_US'))
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def eightball_cmd(ctx, arg):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    user_data = await sync_db(ctx, 'users', 'regular')
    await eightball.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg)

@bot.slash_command(name="8ball", description=translator.translate('command_description', '8ball', 'en_US'))
async def eightball_scmd(ctx, question):
    guild_data = await sync_db(ctx, 'guilds', 'slash')
    language = guild_data[1]
    await eightball.sendSlashMsg(ctx, bot, config, language, disnake, translator, question)

@bot.command(name="rngen", description=translator.translate('command_description', 'rngen', 'en_US'), aliases=['rand'])
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def rngen_cmd(ctx, arg):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    user_data = await sync_db(ctx, 'users', 'regular')

@bot.slash_command(name="rngen", description=translator.translate('command_description', 'rngen', 'en_US'))
async def rngen_scmd(ctx, range):
    guild_data = await sync_db(ctx, 'guilds', 'slash')
    language = guild_data[1]
    await rngen.sendSlashMsg(ctx, bot, config, language, disnake, translator, range)

@bot.command(name="eval")
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def eval_cmd(ctx, arg):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    user_data = await sync_db(ctx, 'users', 'regular')
    await eval.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg)

@bot.command(name="guild", description=translator.translate('command_description', 'guild', 'en_US'), aliases=['server'])
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def guild_cmd(ctx):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    user_data = await sync_db(ctx, 'users', 'regular')
    await guild.sendRegularMsg(ctx, bot, config, language, disnake, translator)

@bot.slash_command(name="guild", description=translator.translate('command_description', 'guild', 'en_US'))
async def guild_scmd(ctx):
    guild_data = await sync_db(ctx, 'guilds', 'slash')
    language = guild_data[1]
    await guild.sendSlashMsg(ctx, bot, config, language, disnake, translator)

@bot.command(name="calc", description=translator.translate('command_description', 'calc', 'en_US'))
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def calc_cmd(ctx, arg):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    user_data = await sync_db(ctx, 'users', 'regular')
    await calc.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg)

@bot.slash_command(name="calc", description=translator.translate('command_description', 'calc', 'en_US'))
async def calc_scmd(ctx, expression):
    guild_data = await sync_db(ctx, 'guilds', 'slash')
    language = guild_data[1]
    await calc.sendSlashMsg(ctx, bot, config, language, disnake, translator, expression)

@bot.command(name="settings", description=translator.translate('command_description', 'settings', 'en_US'))
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def settings_cmd(ctx, *arg):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    user_data = await sync_db(ctx, 'users', 'regular')
    await settings.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg, db, database, cursor)

@bot.command(name="publish", description=translator.translate('command_description', 'publish', 'en_US'), aliases=['post'])
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def publish_cmd(ctx, *, arg):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    user_data = await sync_db(ctx, 'users', 'regular')
    now = datetime.datetime.now(datetime.timezone.utc).astimezone()
    await publish.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg)


@bot.command(name="ping", description=translator.translate('command_description', 'ping', 'en_US'))
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def ping_cmd(ctx):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    user_data = await sync_db(ctx, 'users', 'regular')
    await ping.sendRegularMsg(ctx, bot, config, language, disnake, translator)

@bot.slash_command(name="ping", description=translator.translate('command_description', 'ping', 'en_US'))
async def ping_scmd(ctx):
    guild_data = await sync_db(ctx, 'guilds', 'slash')
    language = guild_data[1]
    await ping.sendSlashMsg(ctx, bot, config, language, disnake, translator)

@bot.command(name="weather", description=translator.translate('command_description', 'weather', 'en_US'))
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def weather_cmd(ctx, *, arg):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    await weather.sendRegularMsg(ctx, bot, config, tokens, language, disnake, translator, arg)

@bot.slash_command(name="weather", description=translator.translate('command_description', 'weather2', 'en_US'))
async def weather_scmd(ctx, *, arg):
    guild_data = await sync_db(ctx, 'guilds', 'slash')
    language = guild_data[1]
    await weather.sendSlashMsg(ctx, bot, config, tokens, language, disnake, translator, arg)

@bot.command(name="wiki", description=translator.translate('command_description', 'wiki', 'en_US'))
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def wiki_cmd(ctx, *, arg):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    await wiki.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg)

@bot.slash_command(name="wiki", description=translator.translate('command_description', 'wiki', 'en_US'))
async def wiki_scmd(ctx, *, arg):
    guild_data = await sync_db(ctx, 'guilds', 'slash')
    language = guild_data[1]
    await wiki.sendSlashMsg(ctx, bot, config, language, disnake, translator, arg)

@bot.command(name="codec", description=translator.translate('command_description', 'codec', 'en_US'))
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def codec_cmd(ctx, *arg):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    now = datetime.datetime.now(datetime.timezone.utc).astimezone()
    await codec.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg, binary)


@bot.command(name="timers", description=translator.translate('command_examples', 'timers', 'en_US'))
@commands.cooldown(1, config['cooldown'], commands.BucketType.user)
async def timers_cmd(ctx, *, arg):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    user_data = await sync_db(ctx, 'users', 'regular')
    await timers.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg, db, database, cursor)

@bot.event
async def on_command_error(ctx, error):
    guild_data = await sync_db(ctx, 'guilds', 'regular')
    language = guild_data[1]
    if isinstance(error, commands.MissingRequiredArgument):
        if(ctx.message.content == '{0}help'.format(config['prefix'])):
            await help.sendRegularMsg(ctx, bot, config, links, language, disnake, translator)
        elif(ctx.message.content == '{0}timers'.format(config['prefix'])):
            await timers.sendRegularMsgWithoutArgs(ctx, bot, config, language, disnake, translator, db, database, cursor)
        else:
            await help.sendCmdHelpWithoutArgs(ctx, bot, config, language, disnake, translator)
    elif isinstance(error, commands.CommandNotFound):
        pass
    elif isinstance(error, commands.CommandOnCooldown):
        await ctx.message.add_reaction('🥸')
    else:
        error_list = []
        error_text = "".join(traceback.TracebackException.from_exception(error).format())
        if(config['bugs_ch'] > 0):
            await bugreporter.send(ctx, bot, config, language, disnake, translator, error_text)
        else:
            print(' BUGREPORT:\r\n{0}'.format(error_text))

# 7. Database autosynchronization
async def sync_db(ctx, table, message_type):
    if(message_type == 'regular'):
        cursor = database.cursor()
        # for user values sync
        if(await db.if_user_existed(database, cursor, ctx.message.author.id) == True):
            cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.message.author.id))
            user_data = cursor.fetchone()
            await db.update_value(ctx, database, cursor, 'users', 'sended_msg_timestamp', '\'{0}\''.format(ctx.message.created_at.strftime('%Y-%m-%d %H:%M:%S')), ctx.message.author.id)
        else:
            await db.add_user_value(database, ctx.message, cursor)
            cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.message.author.id))
            user_data = cursor.fetchone()
        # for guild values sync and cooldown
        if(await db.if_guild_existed(database, cursor, ctx.message.guild.id) == True):
            cursor.execute("SELECT * FROM guilds WHERE id='{0}';".format(ctx.message.guild.id))
            guild_data = cursor.fetchone()
        else:
            language = 'en_US'
            await db.add_guild_value(database, ctx.message.guild, cursor)
            cursor.execute("SELECT * FROM guilds WHERE id='{0}';".format(ctx.message.guild.id))
            guild_data = cursor.fetchone()
        if(table == 'guilds'):
            return guild_data
        else:
            return user_data
    else:
        cursor = database.cursor()
        # for user values sync
        if(await db.if_user_existed(database, cursor, ctx.author.id) == True):
            cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.author.id))
            user_data = cursor.fetchone()
            await db.update_value(ctx, database, cursor, 'users', 'sended_msg_timestamp', '\'{0}\''.format(ctx.created_at.strftime('%Y-%m-%d %H:%M:%S')), ctx.author.id)
        else:
            await db.add_user_value(database, ctx, cursor)
            cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.author.id))
            user_data = cursor.fetchone()
        # for guild values sync and cooldown
        if(await db.if_guild_existed(database, cursor, ctx.guild.id) == True):
            cursor.execute("SELECT * FROM guilds WHERE id='{0}';".format(ctx.guild.id))
            guild_data = cursor.fetchone()
        else:
            language = 'en_US'
            await db.add_guild_value(database, ctx.guild, cursor)
            cursor.execute("SELECT * FROM guilds WHERE id='{0}';".format(ctx.guild.id))
            guild_data = cursor.fetchone()
        if(table == 'guilds'):
            return guild_data
        else:
            return user_data

bot.run(tokens['discord_api'])
