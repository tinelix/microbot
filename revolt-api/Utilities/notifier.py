# Microbot Revolt bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

import os

async def showWelcomeMessage(voltage, bot, config):
    if(os.name == 'nt'):
        clear_cmd = 'cls'
    else:
        clear_cmd = 'clear'
    os.system(clear_cmd)
    print('\n {0} {1}\n Connected to {2}!\n Copyright © 2022 Dmitry Tretyakov (aka. Tinelix)'
          '\n ─────────────────────────────────────────────────────── \n'
          ' S: {3}\n ───────────────────────────────────────────────────────'.format(config['name'], config['version'], '{0}'.format(bot.user.name), len(bot.cache.servers)))
    await bot.set_status("{0} servers".format(len(bot.cache.servers)), voltage.PresenceType.busy)

async def refreshStatus(voltage, bot, config):
    await bot.set_status("{0} servers".format(len(bot.cache.servers)), voltage.PresenceType.busy)

async def updateWelcomeMessage(voltage, bot, config):
    if(os.name == 'nt'):
        clear_cmd = 'cls'
    else:
        clear_cmd = 'clear'
    os.system(clear_cmd)
    print('\n {0} {1}\n Connected to {2}!\n Copyright © 2022 Dmitry Tretyakov (aka. Tinelix)'
          '\n ─────────────────────────────────────────────────────── \n'
          ' S: {3}\n ───────────────────────────────────────────────────────'.format(config['name'], config['version'], '{0}'.format(bot.user.name), len(bot.cache.servers)))
