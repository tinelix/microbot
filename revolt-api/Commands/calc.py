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

import numexpr

async def generateEmbed(ctx, bot, config, language, voltage, translator, arg):
    try:
        result = str(numexpr.evaluate(arg.replace(':', '/')))
        msg_embed = voltage.SendableEmbed(
            title=str(translator.translate('embed_title', 'calc', language)),
            colour=config['accent_def'],
        )
        msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'calc_resulf', language), '```{0}```'.format(result))
        msg_embed.description += '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'calc_asignf', language), translator.translate('embed_fields', 'calc_asignv', language))
    except Exception as e:
        msg_embed = voltage.SendableEmbed(
            title=str(translator.translate('embed_title', 'calc', language)),
            colour=config['accent_err'],
        )
        if(str(e) == 'division by zero'):
            msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'calc_resulf', language), '```{0}```'.format(translator.translate('embed_fields', 'calc_rlerrv', language)))
        elif(str(e) == 'Python int too large to convert to C long'):
            msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'calc_resulf', language), '```{0}```'.format(translator.translate('embed_fields', 'calc_rlerrv2', language)))
        elif(str(e) == '\'VariableNode\' object has no attribute'):
            msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'calc_resulf', language), '```{0}```'.format(translator.translate('embed_fields', 'calc_rlerrv3', language)))
        else:
            msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'calc_resulf', language), '```{0}```'.format(translator.translate('embed_fields', 'calc_rlerrv3', language).format(str(e))))
        msg_embed.description += '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'calc_asignf', language), translator.translate('embed_fields', 'calc_asignv', language))
    return msg_embed

async def sendRegularMsg(ctx, bot, config, language, voltage, translator, arg):
    msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator, arg)
    await ctx.reply(" ", embed=msg_embed)

async def sendSlashMsg(ctx, bot, config, language, voltage, translator, arg):
    msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator, arg)
    await ctx.send(embed=msg_embed)
