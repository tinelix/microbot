# 1. Importing main libraries (2-10)
import disnake
import platform
import os
import json
import traceback
import glob
import sys
from platform import python_version
import discord_components

# 2. Importing modular commands
from disnake.ext import commands
from Commands import *

# 3. Importing utilities
from Utilities import *

# 4. Importing bot configuration
from config import *

# 5. Creating Discord bot instance with all intents
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix=config['prefix'], intents=intents, sync_commands=True)
bot.remove_command('help')

language = 'ru_RU'

# 6. Globally blocking all DMs
@bot.check
async def no_DM(ctx):
    return ctx.guild is not None

# 7. Events and message triggers
@bot.event
async def on_ready():
    await notifer.showWelcomeMessage(disnake, bot, config)

@bot.event
async def on_guild_join(guild):
    await notifer.refreshStatus(disnake, bot, config)

@bot.event
async def on_guild_leave(guild):
    await notifer.refreshStatus(disnake, bot, config)

@bot.command(name="help", description=translator.translate('command_description', 'help', 'en_US'))
async def help_cmd(ctx, arg):
    await help.sendCmdHelpMsg(ctx, bot, links, config, language, disnake, translator, arg)

@bot.slash_command(name="help", description=translator.translate('command_description', 'help', 'en_US'))
async def help_scmd(ctx):
    await help.sendSlashMsg(ctx, bot, config, links, language, disnake, translator)

@bot.command(name="about", description=translator.translate('command_description', 'about', 'en_US'))
async def about_cmd(ctx):
    await about.sendRegularMsg(ctx, bot, config, links, language, disnake, translator, python_version)

@bot.slash_command(name="about", description=translator.translate('command_description', 'about', 'en_US'))
async def about_scmd(ctx):
    await about.sendSlashMsg(ctx, bot, config, links, language, disnake, translator, python_version)

@bot.command(name="user", description=translator.translate('command_description', 'user', 'en_US'))
async def user_cmd(ctx, arg):
    await user.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg)

@bot.slash_command(name="user", description=translator.translate('command_description', 'user', 'en_US'))
async def user_scmd(ctx, member):
    await user.sendSlashMsg(ctx, bot, config, language, disnake, translator, member)

@bot.command(name="avatar", description=translator.translate('command_description', 'avatar', 'en_US'))
async def avatar_cmd(ctx, arg):
    await avatar.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg)

@bot.slash_command(name="avatar", description=translator.translate('command_description', 'avatar', 'en_US'))
async def avatar_scmd(ctx, member):
    await avatar.sendSlashMsg(ctx, bot, config, language, disnake, translator, member)

@bot.command(name="8ball", description=translator.translate('command_description', '8ball', 'en_US'))
async def eightball_cmd(ctx, arg):
    await eightball.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg)

@bot.slash_command(name="8ball", description=translator.translate('command_description', '8ball', 'en_US'))
async def eightball_scmd(ctx, question):
    await eightball.sendSlashMsg(ctx, bot, config, language, disnake, translator, question)

@bot.command(name="rngen", description=translator.translate('command_description', 'rngen', 'en_US'))
async def rngen_cmd(ctx, arg):
    await rngen.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg)

@bot.slash_command(name="rngen", description=translator.translate('command_description', 'rngen', 'en_US'))
async def rngen_scmd(ctx, range):
    await rngen.sendSlashMsg(ctx, bot, config, language, disnake, translator, range)

@bot.command(name="eval")
async def eval_cmd(ctx, arg):
    await eval.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg)

@bot.command(name="guild", description=translator.translate('command_description', 'guild', 'en_US'))
async def guild_cmd(ctx):
    await guild.sendRegularMsg(ctx, bot, config, language, disnake, translator)

@bot.slash_command(name="guild", description=translator.translate('command_description', 'guild', 'en_US'))
async def guild_scmd(ctx):
    await guild.sendSlashMsg(ctx, bot, config, language, disnake, translator)

@bot.command(name="calc", description=translator.translate('command_description', 'guild', 'en_US'))
async def calc_cmd(ctx, arg):
    await calc.sendRegularMsg(ctx, bot, config, language, disnake, translator, arg)

@bot.slash_command(name="calc", description=translator.translate('command_description', 'guild', 'en_US'))
async def calc_scmd(ctx, expression):
    await calc.sendSlashMsg(ctx, bot, config, language, disnake, translator, expression)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        if(ctx.message.content == '{0}help'.format(config['prefix'])):
            await help.sendRegularMsg(ctx, bot, config, links, language, disnake, translator)
        else:
            await help.sendCmdHelpWithoutArgs(ctx, bot, config, language, disnake, translator)
    elif isinstance(error, commands.CommandNotFound):
        pass
    else:
        error_list = []
        error_text = "".join(traceback.TracebackException.from_exception(error).format())
        if(config['bugs_ch'] > 0):
            await bugreporter.send(ctx, bot, config, language, disnake, translator, error_text)
        else:
            pass


bot.run(config['token'])
