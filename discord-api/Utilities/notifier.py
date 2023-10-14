# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

import os
from disnake.ext import tasks
from itertools import cycle

async def getConnectionQualityPseudoGraph(bot):
    connection_quality = "N/A"
    if(round(bot.latency * 1000, 2) > 2000):
        connection_quality = "{0} ms [\033[91m....\033[0m]".format(round(bot.latency * 1000, 2))
    elif(round(bot.latency * 1000, 2) > 1500):
        connection_quality = "{0} ms [\033[91m|...\033[0m]".format(round(bot.latency * 1000, 2))
    elif(round(bot.latency * 1000, 2) > 1000):
        connection_quality = "{0} ms [\033[93m||..\033[0m]".format(round(bot.latency * 1000, 2))
    elif(round(bot.latency * 1000, 2) > 500):
        connection_quality = "{0} ms [\033[92m|||.\033[0m]".format(round(bot.latency * 1000, 2))
    else:
        connection_quality = "{0} ms [\033[92m||||\033[0m]".format(round(bot.latency * 1000, 2))

    return connection_quality

async def showWelcomeMessage(disnake, bot, config, version):
    if(os.name == 'nt'):
        clear_cmd = 'cls'
    else:
        clear_cmd = 'clear'
    os.system(clear_cmd)

    conn_quality = await getConnectionQualityPseudoGraph(bot)

    print('\n {0} {1}\n\033[92m Connected to {2}!\033[0m\n Copyright © 2023 Dmitry Tretyakov (aka. Tinelix)'
          '\n ─────────────────────────────────────────────────────── \n'
          ' L: {3} │ G: {4}'
          '\n ───────────────────────────────────────────────────────'
          .format(version['original_name'], version['version'], '{0} ({1})'
                  .format(bot.user.name, bot.user.global_name), conn_quality, len(bot.guilds)))
    statuses = ["{0} guilds".format(len(bot.guilds)), "{0}help".format(config['prefix']), "Version {0}".format(version['version'])]
    statuses_cycle = cycle(statuses)
    game = disnake.Game(statuses[0], type=disnake.ActivityType.watching)
    await bot.change_presence(status=disnake.Status.dnd, activity=game)
    @tasks.loop(seconds=10)
    async def autostatus():
        await bot.wait_until_ready()
        await bot.change_presence(status=disnake.Status.dnd, activity=disnake.Game(name=next(statuses_cycle)))
    autostatus.start()

async def updateWelcomeMessage(disnake, bot, config, versiom):
    if(os.name == 'nt'):
        clear_cmd = 'cls'
    else:
        clear_cmd = 'clear'
    os.system(clear_cmd)
    print('\n {0} {1}\n Connected to {2}!\n Copyright © 2023 Dmitry Tretyakov (aka. Tinelix)'
          '\n ─────────────────────────────────────────────────────── \n'
          ' L: {3} ms │ G: {4}\n ───────────────────────────────────────────────────────'
          .format(version['original_name'], version['version'], '{0} ({1})'
                  .format(bot.user.name, bot.user.global_name), getConnectionQualityPseudoGraph(bot), len(bot.guilds)))
