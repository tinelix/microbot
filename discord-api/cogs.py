import disnake
import platform
import os
import json
import traceback
import glob
import sys
import datetime
import time
# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

from platform import python_version
import sqlite3
import pytz
from disnake.ext import commands

# 1. Importing utilities
from Commands import *
from Utilities import *
from config import *

class Commands(commands.Cog):
    def __init__(self, bot, database, cursor):
        self.bot = bot
        self._last_member = None
        self.cog = bot.get_cog('Commands')
        self.bot.database = database
        self.bot.cursor = cursor
        self.connectionStartTime = time.time()

    @commands.command(name="help", description=translator.translate('command_description', 'help', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def help_cmd(self, ctx, arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        user_data = await sync_db(self.bot, ctx, 'users', 'regular')
        await help.sendCmdHelpMsg(ctx, self.bot, links, config, language, disnake, translator, arg)

    @commands.slash_command(name="help", description=translator.translate('command_description', 'help', 'en_US'))
    async def help_scmd(self, ctx):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'slash')
        language = guild_data[1]
        await help.sendSlashMsg(ctx, self.bot, config, links, language, disnake, translator)

    @commands.command(name="about", description=translator.translate('command_description', 'about', 'en_US'), aliases=['state', 'check'])
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def about_cmd(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time() - self.connectionStartTime))))
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        user_data = await sync_db(self.bot, ctx, 'users', 'regular')
        await about.sendRegularMsg(ctx, self.bot, config, links, language, disnake, translator, python_version, uptime)

    @commands.slash_command(name="about", description=translator.translate('command_description', 'about', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def about_scmd(self, ctx):
        uptime = str(datetime.timedelta(seconds=int(round(time.time() - self.connectionStartTime))))
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'slash')
        language = guild_data[1]
        await about.sendSlashMsg(ctx, self.bot, config, links, language, disnake, translator, python_version, uptime)

    @commands.command(name="user", description=translator.translate('command_description', 'user', 'en_US'), aliases=['member'])
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def user_cmd(self, ctx, arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        user_data = await sync_db(self.bot, ctx, 'users', 'regular')
        await user.sendRegularMsg(ctx, self.bot, config, language, disnake, translator, arg)

    @commands.slash_command(name="user", description=translator.translate('command_description', 'user', 'en_US'))
    async def user_scmd(self, ctx, member):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'slash')
        language = guild_data[1]
        await user.sendSlashMsg(ctx, self.bot, config, language, disnake, translator, member)

    @commands.command(name="avatar", description=translator.translate('command_description', 'avatar', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def avatar_cmd(self, ctx, arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        user_data = await sync_db(self.bot, ctx, 'users', 'regular')
        await avatar.sendRegularMsg(ctx, self.bot, config, language, disnake, translator, arg)

    @commands.slash_command(name="avatar", description=translator.translate('command_description', 'avatar', 'en_US'))
    async def avatar_scmd(self, ctx, member):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'slash')
        language = guild_data[1]
        await avatar.sendSlashMsg(ctx, self.bot, config, language, disnake, translator, member)

    @commands.command(name="8ball", description=translator.translate('command_description', '8ball', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def eightball_cmd(self, ctx, arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        user_data = await sync_db(self.bot, ctx, 'users', 'regular')
        await eightball.sendRegularMsg(ctx, self.bot, config, language, disnake, translator, arg)

    @commands.slash_command(name="8ball", description=translator.translate('command_description', '8ball', 'en_US'))
    async def eightball_scmd(self, ctx, question):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'slash')
        language = guild_data[1]
        await eightball.sendSlashMsg(ctx, self.bot, config, language, disnake, translator, question)

    @commands.command(name="rngen", description=translator.translate('command_description', 'rngen', 'en_US'), aliases=['rand'])
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def rngen_cmd(self, ctx, arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        user_data = await sync_db(self.bot, ctx, 'users', 'regular')
        await rngen.sendRegularMsg(ctx, self.bot, config, language, disnake, translator, arg)

    @commands.slash_command(name="rngen", description=translator.translate('command_description', 'rngen', 'en_US'))
    async def rngen_scmd(self, ctx, range):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'slash')
        language = guild_data[1]
        await rngen.sendSlashMsg(ctx, self.bot, config, language, disnake, translator, range)

    @commands.command(name="eval")
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def eval_cmd(self, ctx, arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        user_data = await sync_db(self.bot, ctx, 'users', 'regular')
        await eval.sendRegularMsg(ctx, self.bot, config, language, disnake, translator, arg)

    @commands.command(name="guild", description=translator.translate('command_description', 'guild', 'en_US'), aliases=['server'])
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def guild_cmd(self, ctx):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        user_data = await sync_db(self.bot, ctx, 'users', 'regular')
        await guild.sendRegularMsg(ctx, self.bot, config, language, disnake, translator)

    @commands.slash_command(name="guild", description=translator.translate('command_description', 'guild', 'en_US'))
    async def guild_scmd(self, ctx):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'slash')
        language = guild_data[1]
        await guild.sendSlashMsg(ctx, self.bot, config, language, disnake, translator)

    @commands.command(name="calc", description=translator.translate('command_description', 'calc', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def calc_cmd(self, ctx, arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        user_data = await sync_db(self.bot, ctx, 'users', 'regular')
        await calc.sendRegularMsg(ctx, self.bot, config, language, disnake, translator, arg)

    @commands.slash_command(name="calc", description=translator.translate('command_description', 'calc', 'en_US'))
    async def calc_scmd(self, ctx, expression):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'slash')
        language = guild_data[1]
        await calc.sendSlashMsg(ctx, self.bot, config, language, disnake, translator, expression)

    @commands.command(name="settings", description=translator.translate('command_description', 'settings', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def settings_cmd(self, ctx, *arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        user_data = await sync_db(self.bot, ctx, 'users', 'regular')
        await settings.sendRegularMsg(ctx, self.bot, config, language, disnake, translator, arg, db, self.bot.database, self.bot.cursor)

    @commands.command(name="publish", description=translator.translate('command_description', 'publish', 'en_US'), aliases=['post'])
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def publish_cmd(self, ctx, *, arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        user_data = await sync_db(self.bot, ctx, 'users', 'regular')
        now = datetime.datetime.now(datetime.timezone.utc).astimezone()
        await publish.sendRegularMsg(ctx, self.bot, config, language, disnake, translator, arg)

    @commands.command(name="ping", description=translator.translate('command_description', 'ping', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def ping_cmd(self, ctx):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        user_data = await sync_db(self.bot, ctx, 'users', 'regular')
        await ping.sendRegularMsg(ctx, self.bot, config, language, disnake, translator)

    @commands.slash_command(name="ping", description=translator.translate('command_description', 'ping', 'en_US'))
    async def ping_scmd(self, ctx):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'slash')
        language = guild_data[1]
        await ping.sendSlashMsg(ctx, self.bot, config, language, disnake, translator)

    @commands.command(name="weather", description=translator.translate('command_description', 'weather', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def weather_cmd(self, ctx, *, arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        await weather.sendRegularMsg(ctx, self.bot, config, tokens, language, disnake, translator, arg)

    @commands.slash_command(name="weather", description=translator.translate('command_description', 'weather2', 'en_US'))
    async def weather_scmd(self, ctx, *, arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'slash')
        language = guild_data[1]
        await weather.sendSlashMsg(ctx, self.bot, config, tokens, language, disnake, translator, arg)

    @commands.command(name="wiki", description=translator.translate('command_description', 'wiki', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def wiki_cmd(self, ctx, *, arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        await wiki.sendRegularMsg(ctx, self.bot, config, language, disnake, translator, arg)

    @commands.slash_command(name="wiki", description=translator.translate('command_description', 'wiki', 'en_US'))
    async def wiki_scmd(self, ctx, *, arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'slash')
        language = guild_data[1]
        await wiki.sendSlashMsg(ctx, self.bot, config, language, disnake, translator, arg)

    @commands.command(name="codec", description=translator.translate('command_description', 'codec', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def codec_cmd(self, ctx, *arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        now = datetime.datetime.now(datetime.timezone.utc).astimezone()
        await codec.sendRegularMsg(ctx, self.bot, config, language, disnake, translator, arg, binary)

    @commands.command(name="timers", description=translator.translate('command_examples', 'timers', 'en_US'))
    @commands.cooldown(1, config['cooldown'], commands.BucketType.user)
    async def timers_cmd(self, ctx, *, arg):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        user_data = await sync_db(self.bot, ctx, 'users', 'regular')
        await timers.sendRegularMsg(ctx, self.bot, config, language, disnake, translator, arg, db, self.bot.database, self.bot.cursor)

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
        await notifier.showWelcomeMessage(disnake, self.bot, config)
        await db.create_tables(self.bot.database, self.bot.cursor)

    @commands.Cog.listener()
    async def on_disconnect(self):
        print(" ERROR: Discord Gateway connection disconnected!")

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        if(await db.if_guild_existed(self.bot.database, self.bot.cursor, guild.id) == False):
            await db.add_guild_value(self.bot.database, guild, self.bot.cursor)

    @commands.Cog.listener()
    async def on_guild_leave(guild):
        await notifier.updateWelcomeMessage(disnake, bot, config)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        guild_data = await sync_db(self.bot, ctx, 'guilds', 'regular')
        language = guild_data[1]
        custom_prefix = ''
        for prefix in await self.bot.get_prefix(ctx.message):
            if(ctx.message.content.startswith(prefix)):
                custom_prefix = prefix
        if isinstance(error, commands.MissingRequiredArgument):
            if(ctx.message.content == '{0}help'.format(config['prefix']) or ctx.message.content == '{0}help'.format(custom_prefix)):
                await help.sendRegularMsg(ctx, self.bot, config, links, language, disnake, translator)
            elif(ctx.message.content == '{0}timers'.format(config['prefix']) or ctx.message.content == '{0}timers'.format(custom_prefix)):
                await timers.sendRegularMsgWithoutArgs(ctx, self.bot, config, language, disnake, translator, db, self.bot.database, self.bot.cursor)
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
                await bugreporter.send(ctx, self.bot, config, language, disnake, translator, error_text)
            else:
                print(' BUGREPORT:\r\n{0}'.format(error_text))

async def sync_db(bot, ctx, table, message_type):
        if(message_type == 'regular'):
            cursor = bot.database.cursor()
            # for user values sync
            if(await db.if_user_existed(bot.database, cursor, ctx.message.author.id) == True):
                cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.message.author.id))
                user_data = cursor.fetchone()
                await db.update_value(ctx, bot.database, cursor, 'users', 'sended_msg_timestamp', '\'{0}\''.format(ctx.message.created_at.strftime('%Y-%m-%d %H:%M:%S')), ctx.message.author.id)
            else:
                await db.add_user_value(bot.database, ctx.message, cursor)
                cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.message.author.id))
                user_data = cursor.fetchone()
            # for guild values sync and cooldown
            if(await db.if_guild_existed(bot.database, cursor, ctx.message.guild.id) == True):
                cursor.execute("SELECT * FROM guilds WHERE id='{0}';".format(ctx.message.guild.id))
                guild_data = cursor.fetchone()
            else:
                language = 'en_US'
                await db.add_guild_value(bot.database, ctx.message.guild, cursor)
                cursor.execute("SELECT * FROM guilds WHERE id='{0}';".format(ctx.message.guild.id))
                guild_data = cursor.fetchone()
            if(table == 'guilds'):
                return guild_data
            else:
                return user_data
        else:
            cursor = bot.database.cursor()
            # for user values sync
            if(await db.if_user_existed(bot.database, cursor, ctx.author.id) == True):
                cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.author.id))
                user_data = cursor.fetchone()
                await db.update_value(ctx, bot.database, cursor, 'users', 'sended_msg_timestamp', '\'{0}\''.format(ctx.created_at.strftime('%Y-%m-%d %H:%M:%S')), ctx.author.id)
            else:
                await db.add_user_value(bot.database, ctx, cursor)
                cursor.execute("SELECT * FROM users WHERE id='{0}';".format(ctx.author.id))
                user_data = cursor.fetchone()
            # for guild values sync and cooldown
            if(await db.if_guild_existed(bot.database, cursor, ctx.guild.id) == True):
                cursor.execute("SELECT * FROM guilds WHERE id='{0}';".format(ctx.guild.id))
                guild_data = cursor.fetchone()
            else:
                language = 'en_US'
                await db.add_guild_value(bot.database, ctx.guild, cursor)
                cursor.execute("SELECT * FROM guilds WHERE id='{0}';".format(ctx.guild.id))
                guild_data = cursor.fetchone()
            if(table == 'guilds'):
                return guild_data
            else:
                return user_data
