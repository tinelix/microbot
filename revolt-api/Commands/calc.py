# Microbot Revolt bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

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
