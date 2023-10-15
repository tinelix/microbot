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

import cpuinfo # for install 'pip install py-cpuinfo'
import psutil
import platform
import traceback

async def generateEmbed(ctx, bot, config, language, voltage, translator, arg):
    if(ctx.message.author.id == config['dev_id']):  # only bot owner!
        try:
            msg_embed = voltage.SendableEmbed(
                str(translator.translate('embed_title', 'eval', language)),
                colour=config['accent_def'],
            )
            if(arg == 'guilds'): # server list for statistical data
                eval_r = ''
                for server in bot.servers:
                    online = 0
                    for member in server.members:
                        if(member.status.presence == voltage.PresenceType.online or member.status.presence == voltage.PresenceType.idle or member.status.presence == voltage.PresenceType.busy):
                            online += 1
                    eval_r += '{0:03d}. {1}\r\n└────┤ {2: 4d} members │ {3: 4d} online │\r\n'.format(bot.servers.index(server) + 1, server.name, len(server.members), online)

            else:
                if(len(str(eval(arg))) > 1000):
                    eval_r = 'Content is too large (> 1000 symbols)'
                else:
                    eval_r = str(eval(arg))
            if(arg == 'guilds'):
                pass
            elif("token" in arg):
                eval_r = 'https://www.youtube.com/watch?v=2bXP5VNukmY'
            else:
                msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'eval_codelf', language), '``\r\n{0}\r\n``'.format(arg))
            if(msg_embed.description == None):
                msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'eval_resulf', language), '```\r\n{0}\r\n```'.format(eval_r))
            else:
                msg_embed.description += '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'eval_resulf', language), '```\r\n{0}\r\n```'.format(eval_r))
        except Exception as e:
            msg_embed = msg_embed = voltage.SendableEmbed(
                title=str(translator.translate('embed_title', 'eval', language)),
                description='```\r\nERROR: {0}\r\n```'.format("".join(traceback.TracebackException.from_exception(e).format())),
                colour=config['accent_err']
            )
    else:
        msg_embed = msg_embed = voltage.SendableEmbed(
            title=str(translator.translate('embed_title', 'forbidden', language)),
            description=str(translator.translate('embed_description', 'forbidden', language)),
            colour=config['accent_err']
        )
    return msg_embed

async def sendRegularMsg(ctx, bot, config, language, voltage, translator, arg):
    msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator, arg)
    await ctx.reply(" ", embed=msg_embed)
