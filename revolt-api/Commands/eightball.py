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

import random

name = '8ball'
hidden = False

async def generateEmbed(ctx, bot, config, language, voltage, translator, python_version):
    random_numb = random.randint(0, len(translator.translate('embed_fields', '8ball_answv', language)) - 1)
    msg_embed = voltage.SendableEmbed(
        title=str(translator.translate('embed_title', '8ball', language)),
        colour=config['accent_def'],
    )
    msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', '8ball_answf', language), translator.translate('embed_fields', '8ball_answv', language)[random_numb])
    msg_embed.description += '###### {0}'.format(translator.translate('embed_footer', '8ball', language))
    return msg_embed

async def sendSlashMsg(ctx, bot, config, language, voltage, translator, python_version):
    msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator, python_version)
    await ctx.response.send_message(embed=msg_embed)

async def sendRegularMsg(ctx, bot, config, language, voltage, translator, python_version):
    msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator, python_version)
    await ctx.reply(" ", embed=msg_embed)
