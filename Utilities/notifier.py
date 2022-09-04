# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

import os
from disnake.ext import tasks
from itertools import cycle

async def showWelcomeMessage(disnake, bot, config):
    if(os.name == 'nt'):
        clear_cmd = 'cls'
    else:
        clear_cmd = 'clear'
    os.system(clear_cmd)
    print('\n {0} {1}\n Connected to {2}!\n Copyright © 2022 Dmitry Tretyakov (aka. Tinelix) & Den4ik'
          '\n ──────────────────────────────────────────────────────────── \n'
          ' L: {3} ms │ G: {4}\n ────────────────────────────────────────────────────────────'.format(config['name'], config['version'], '{0}#{1}'.format(bot.user.name, bot.user.discriminator), round(bot.latency * 1000, 2), len(bot.guilds)))
    statuses = ["{0} guilds".format(len(bot.guilds)), "{0}help".format(config['prefix']), "Version {0}".format(config['version'])]
    statuses_cycle = cycle(statuses)
    game = disnake.Game(statuses[0], type=disnake.ActivityType.watching)
    await bot.change_presence(status=disnake.Status.online, activity=game)
    @tasks.loop(seconds=10)
    async def autostatus():
        await bot.wait_until_ready()
        await bot.change_presence(status=disnake.Status.online, activity=disnake.Game(name=next(statuses_cycle)))
    autostatus.start()

async def updateWelcomeMessage(disnake, bot, config):
    if(os.name == 'nt'):
        clear_cmd = 'cls'
    else:
        clear_cmd = 'clear'
    os.system(clear_cmd)
    print('\n {0} {1}\n Connected to {2}!\n Copyright © 2022 Dmitry Tretyakov (aka. Tinelix) & Den4ik'
          '\n ──────────────────────────────────────────────────────────── \n'
          ' L: {3} ms │ G: {4}\n ────────────────────────────────────────────────────────────'.format(config['name'], config['version'], '{0}#{1}'.format(bot.user.name, bot.user.discriminator), round(bot.latency * 1000, 2), len(bot.guilds)))
