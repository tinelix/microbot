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
from disnake.ext import commands

# 1. Importing utilities
from Commands import *
from Utilities import *
from config import *
from version import *

class Commands(commands.Cog):
    def __init__(self, bot, database, cursor):
        self.bot = bot
        self._last_member = None
        self.cog = bot.get_cog('Commands')
        self.bot.database = database
        self.bot.cursor = cursor
        self.connectionStartTime = time.time()
        self.tz = pytz.timezone('Europe/Moscow')

    @commands.command(name="help", description=translator.translate('command_description', 'help', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def help_cmd(self, ctx, arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await help.sendCmdHelpMsg(ctx, self, links, config, disnake, translator, arg)

    @commands.slash_command(name="help", description=translator.translate('command_description', 'help', 'en_US'))
    async def help_scmd(self, ctx):
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        user_data = await sync_db(self, ctx, 'users', 'slash')
        await help.sendSlashMsg(ctx, self, config, links, version, disnake, translator)

    @commands.command(name="about", description=translator.translate('command_description', 'about', 'en_US'), aliases=['state', 'check'])
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def about_cmd(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time() - self.connectionStartTime))))
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await about.sendRegularMsg(ctx, self, config, links, disnake, translator,
                                   python_version, version, uptime)

    @commands.slash_command(name="about", description=translator.translate('command_description', 'about', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def about_scmd(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time() - self.connectionStartTime))))
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        user_data = await sync_db(self, ctx, 'users', 'slash')
        await about.sendSlashMsg(ctx, self, config, links, disnake, translator, python_version, version, uptime)

    @commands.command(name="user", description=translator.translate('command_description', 'user', 'en_US'), aliases=['member'])
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def user_cmd(self, ctx, arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await user.sendRegularMsg(ctx, self.bot, config, disnake, translator, arg)

    @commands.slash_command(name="user", description=translator.translate('command_description', 'user', 'en_US'))
    async def user_scmd(self, ctx, member):
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        user_data = await sync_db(self, ctx, 'users', 'slash')
        await user.sendSlashMsg(ctx, self.bot, config, disnake, translator, member)

    @commands.command(name="avatar", description=translator.translate('command_description', 'avatar', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def avatar_cmd(self, ctx, arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await avatar.sendRegularMsg(ctx, self.bot, config, disnake, translator, arg)

    @commands.slash_command(name="avatar", description=translator.translate('command_description', 'avatar', 'en_US'))
    async def avatar_scmd(self, ctx, member):
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        user_data = await sync_db(self, ctx, 'users', 'slash')
        await avatar.sendSlashMsg(ctx, self.bot, config, disnake, translator, member)

    @commands.command(name="8ball", description=translator.translate('command_description', '8ball', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def eightball_cmd(self, ctx, arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await eightball.sendRegularMsg(ctx, self, config, disnake, translator, arg)

    @commands.slash_command(name="8ball", description=translator.translate('command_description', '8ball', 'en_US'))
    async def eightball_scmd(self, ctx, question):
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        user_data = await sync_db(self, ctx, 'users', 'slash')
        await eightball.sendSlashMsg(ctx, self, config, disnake, translator, question)

    @commands.command(name="rngen", description=translator.translate('command_description', 'rngen', 'en_US'), aliases=['rand'])
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def rngen_cmd(self, ctx, arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await rngen.sendRegularMsg(ctx, self, config, disnake, translator, arg)

    @commands.slash_command(name="rngen", description=translator.translate('command_description', 'rngen', 'en_US'))
    async def rngen_scmd(self, ctx, range):
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        user_data = await sync_db(self, ctx, 'users', 'slash')
        await rngen.sendSlashMsg(ctx, self, config, disnake, translator, range)

    @commands.command(name="guild", description=translator.translate('command_description', 'guild', 'en_US'), aliases=['server'])
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def guild_cmd(self, ctx):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await guild.sendRegularMsg(ctx, self, config, language, disnake, translator, self.tz)

    @commands.slash_command(name="guild", description=translator.translate('command_description', 'guild', 'en_US'))
    async def guild_scmd(self, ctx):
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        user_data = await sync_db(self, ctx, 'users', 'slash')
        await guild.sendSlashMsg(ctx, self, config, disnake, translator, self.tz)

    @commands.command(name="calc", description=translator.translate('command_description', 'calc', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def calc_cmd(self, ctx, arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await calc.sendRegularMsg(ctx, self, config, disnake, translator, arg)

    @commands.slash_command(name="calc", description=translator.translate('command_description', 'calc', 'en_US'))
    async def calc_scmd(self, ctx, expression):
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        user_data = await sync_db(self, ctx, 'users', 'slash')
        await calc.sendSlashMsg(ctx, self, config, disnake, translator, expression)

    @commands.command(name="settings", description=translator.translate('command_description', 'settings', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def settings_cmd(self, ctx, *arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await settings.sendRegularMsg(ctx, self, config, disnake,
                                      translator, arg, db, guild_data, user_data)

    @commands.slash_command(name="settings", description=translator.translate('command_description', 'settings', 'en_US'))
    async def settings_scmd(self, ctx, language: str = "", prefix: str = "", timezone: str = ""):
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        user_data = await sync_db(self, ctx, 'users', 'slash')
        arg = ""
        if(len(language) > 0):
            arg = "-L {0}".format(language).split(" ")
        elif(len(prefix) > 0):
            arg = "-P {0}".format(prefix).split(" ")
        elif(len(timezone) > 0):
            arg = "-tz {0}".format(timezone).split(" ")
        await settings.sendSlashMsg(ctx, self, config, disnake, translator,
                                    arg, db, guild_data, user_data)

    @commands.command(name="publish", description=translator.translate('command_description', 'publish', 'en_US'), aliases=['post'])
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def publish_cmd(self, ctx, *, arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        now = datetime.datetime.now(datetime.timezone.utc).astimezone()
        await publish.sendRegularMsg(ctx, self, config, disnake, translator, arg)

    @commands.slash_command(name="publish", description=translator.translate('command_description', 'publish', 'en_US'), aliases=['post'])
    async def publish_scmd(self, ctx, *, text):
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        user_data = await sync_db(self, ctx, 'users', 'slash')
        now = datetime.datetime.now(datetime.timezone.utc).astimezone()
        await publish.sendSlashMsg(ctx, self, config, disnake, translator, text)

    @commands.command(name="ping", description=translator.translate('command_description', 'ping', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def ping_cmd(self, ctx):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await ping.sendRegularMsg(ctx, self, config, disnake, translator)

    @commands.slash_command(name="ping", description=translator.translate('command_description', 'ping', 'en_US'))
    async def ping_scmd(self, ctx):
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        user_data = await sync_db(self, ctx, 'users', 'slash')
        await ping.sendSlashMsg(ctx, self, config, disnake, translator)

    @commands.command(name="weather", description=translator.translate('command_description', 'weather', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def weather_cmd(self, ctx, *, arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await weather.sendRegularMsg(ctx, self, config, tokens, disnake, translator, arg)

    @commands.slash_command(name="weather", description=translator.translate('command_description', 'weather2', 'en_US'))
    async def weather_scmd(self, ctx, *, arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        user_data = await sync_db(self, ctx, 'users', 'slash')
        await weather.sendSlashMsg(ctx, self, config, tokens, disnake, translator, arg)

    @commands.command(name="wiki", description=translator.translate('command_description', 'wiki', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def wiki_cmd(self, ctx, *, arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await wiki.sendRegularMsg(ctx, self, config, disnake, translator, arg)

    @commands.slash_command(name="wiki", description=translator.translate('command_description', 'wiki', 'en_US'))
    async def wiki_scmd(self, ctx, *, arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        user_data = await sync_db(self, ctx, 'users', 'slash')
        await wiki.sendSlashMsg(ctx, self, config, disnake, translator, arg)

    @commands.command(name="codec", description=translator.translate('command_description', 'codec', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def codec_cmd(self, ctx, *arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        now = datetime.datetime.now(datetime.timezone.utc).astimezone()
        await codec.sendRegularMsg(ctx, self, config, disnake, translator, arg, binary)

    @commands.slash_command(name="codec", description=translator.translate('command_description', 'codec', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def codec_scmd(self, ctx, encode: str = "", decode: str = "", *, text):
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        user_data = await sync_db(self, ctx, 'users', 'slash')
        now = datetime.datetime.now(datetime.timezone.utc).astimezone()
        await codec.sendSlashMsg(ctx, self, config, disnake, translator, encode, decode, text, binary)

    @commands.command(name="timers", description=translator.translate('command_examples', 'timers', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def timers_cmd(self, ctx, *, arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await timers.sendRegularMsg(ctx, self, config, disnake, translator, arg, db)

    @commands.command(name="eval")
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def eval_cmd(self, ctx, *, arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await eval.sendRegularMsg(ctx, self, config, disnake, translator, arg)

    @commands.command(name="test")
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def test_cmd(self, ctx, arg):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await test.sendRegularMsg(ctx, self, config, disnake, translator, arg, fatalerr_reporter)

    @commands.command(name="shutdown")
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def shutdown_cmd(self, ctx):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        user_data = await sync_db(self, ctx, 'users', 'regular')
        await eval.sendGoodbyeMsg(ctx, self, config, disnake, translator)

class Listeners(commands.Cog):
    def __init__(self, bot, database, cursor):
        self.bot = bot
        self._last_member = None
        self.cog = bot.get_cog('Listeners')
        self.bot.database = database
        self.bot.cursor = cursor
        self.connectionStartTime = time.time()

    @commands.Cog.listener()
    async def on_ready(self):
        self.connectionStartTime = time.time()
        await notifier.showWelcomeMessage(disnake, self.bot, config, version)
        await db.create_tables(self.bot.database, self.bot.cursor)

    @commands.Cog.listener()
    async def on_disconnect(self):
        print(" ERROR: Discord Gateway connection disconnected!")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if(await db.if_guild_existed(self.bot.database, self.bot.cursor, guild.id) == False):
            await db.add_guild_value(config, self.bot.database, guild, self.bot.cursor)

    @commands.Cog.listener()
    async def on_guild_leave(guild):
        await notifier.updateWelcomeMessage(disnake, bot, config, version)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        guild_data = await sync_db(self, ctx, 'guilds', 'regular')
        custom_prefix = ''
        user_data = await sync_db(self, ctx, 'users', 'regular')
        self.tz = pytz.timezone(user_data[5])
        for prefix in await self.bot.get_prefix(ctx.message):
            if(ctx.message.content.startswith(prefix)):
                custom_prefix = prefix
        if isinstance(error, commands.MissingRequiredArgument):
            if(ctx.message.content == '{0}help'.format(config['prefix']) or ctx.message.content == '{0}help'.format(custom_prefix)):
                await help.sendRegularMsg(ctx, self.bot, config, links, version, language, disnake, translator)
            elif(ctx.message.content == '{0}timers'.format(config['prefix']) or ctx.message.content == '{0}timers'.format(custom_prefix)):
                await timers.sendRegularMsgWithoutArgs(ctx, self.bot, config, language, disnake, translator, db, self.bot.database, self.bot.cursor, self.tz)
            else:
                await help.sendCmdHelpWithoutArgs(ctx, self.bot, config, language, disnake, translator)
        elif isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.message.add_reaction('🥸')
        else:
            error_list = []
            error_text = "".join(traceback.TracebackException.from_exception(error).format())
            if(config['bugs_ch'] > 0):
                await fatalerr_reporter.send(ctx, self, config, version, disnake, translator, error_text, 'regular')
            else:
                print(' WE\'VE GOT SOMETHING BROKEN!\r\n{0}'.format(error_text))

    @commands.Cog.listener()
    async def on_slash_command_error(self, ctx, error):
        guild_data = await sync_db(self, ctx, 'guilds', 'slash')
        language = guild_data[2]
        custom_prefix = ''
        user_data = await sync_db(self, ctx, 'users', 'slash')
        self.tz = pytz.timezone(user_data[5])
        error_list = []
        error_text = "".join(traceback.TracebackException.from_exception(error).format())
        if(config['bugs_ch'] > 0):
            await fatalerr_reporter.send(ctx, self, config, version, disnake, translator, error_text, 'slash')
        else:
            print(' BUGREPORT:\r\n{0}'.format(error_text))

async def sync_db(self, ctx, table, message_type):
    if(message_type == 'regular'):
        self.cursor = self.bot.database.cursor()
        self.database = self.bot.database
        # for user values sync
        if(await db.if_user_existed(self.bot.database, self.cursor, ctx.message.author.id) == True):
            self.cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.message.author.id))
            user_data = self.cursor.fetchone()
            await db.update_value(ctx, self.bot.database, self.cursor, 'users', 'sended_msg_timestamp', '\'{0}\''.format(ctx.message.created_at.strftime('%Y-%m-%d %H:%M:%S')), ctx.message.author.id)
            await db.update_value(ctx, self.bot.database, self.cursor, 'users', 'global_name', '\'{0}\''.format(ctx.message.author.global_name), ctx.message.author.id)
        else:
            await db.add_user_value(self.bot.database, ctx.message, self.cursor)
            self.cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.message.author.id))
            user_data = self.cursor.fetchone()
        # for guild values sync and cooldown
        if(await db.if_guild_existed(self.bot.database, self.cursor, ctx.message.guild.id) == True):
            self.cursor.execute("SELECT * FROM guilds WHERE id='{0}';".format(ctx.message.guild.id))
            guild_data = self.cursor.fetchone()
            await db.update_value(ctx, self.bot.database, self.cursor, 'guilds', 'name', '\'{0}\''.format(ctx.guild.name), ctx.guild.id)
        else:
            language = 'en_US'
            await db.add_guild_value(config, self.bot.database, ctx.message.guild, self.cursor)
            self.cursor.execute("SELECT * FROM guilds WHERE id='{0}';".format(ctx.message.guild.id))
            guild_data = self.cursor.fetchone()
        if(table == 'guilds'):
            self.language = guild_data[2]
            return guild_data
        else:
            self.tz = pytz.timezone(user_data[5])
            return user_data
    else:
        self.cursor = bot.database.cursor()
        # for user values sync
        if(await db.if_user_existed(bot.database, self.cursor, ctx.author.id) == True):
            self.cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.author.id))
            user_data = cursor.fetchone()
            await db.update_value(ctx, self.bot.database, self.cursor, 'users', 'sended_msg_timestamp', '\'{0}\''.format(ctx.created_at.strftime('%Y-%m-%d %H:%M:%S')), ctx.author.id)
            await db.update_value(ctx, self.bot.database, self.cursor, 'users', 'global_name', '\'{0}\''.format(ctx.author.global_name), ctx.author.id)
        else:
            await db.add_user_value(self.bot.database, ctx, cursor)
            self.cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.author.id))
            user_data = cursor.fetchone()
            # for guild values sync and cooldown
        if(await db.if_guild_existed(bot.database, self.cursor, ctx.guild.id) == True):
            self.cursor.execute("SELECT * FROM guilds WHERE id='{0}';".format(ctx.guild.id))
            guild_data = cursor.fetchone()
            await db.update_value(ctx, self.bot.database, self.cursor, 'guilds', 'name', '\'{0}\''.format(ctx.guild.name), ctx.guild.id)
        else:
            self.language = 'en_US'
            await db.add_guild_value(config, self.bot.database, ctx.guild, self.cursor)
            self.cursor.execute("SELECT * FROM guilds WHERE id='{0}';".format(ctx.guild.id))
            guild_data = cursor.fetchone()
        if(table == 'guilds'):
            self.language = guild_data[2]
            return guild_data
        else:
            self.tz = pytz.timezone(user_data[5])
            return user_data
