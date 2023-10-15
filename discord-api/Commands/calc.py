#   Tinelix Microbot
#   -------------------------------------------------------------------------------------------
#   Copyright © 2023 Dmitry Tretyakov (aka. Tinelix)
#
#   This program is free software: you can redistribute it and/or modify it under the terms of
#   the GNU Affero General Public License 3 (or any later version) and/or Apache License 2
#   See the following files in this directory for the precise terms and conditions of either
#   license:
#
#       LICENSE.APACHE
#       LICENSE.AGPL
#
#   Please see each file in the implementation for copyright and licensing
#   information, (in the opening comment of each file).

import numexpr

name = 'calc'
hidden = False

async def generateEmbed(ctx, bot, config, language, disnake, translator, arg):
    try:
        result = str(numexpr.evaluate(arg.replace(':', '/')))
        msg_embed = disnake.Embed(
            colour=config['accent_def'],
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'calc', language)))
        msg_embed.add_field(translator.translate('embed_fields', 'calc_resulf', language), '```py\r\n{0}```'.format(result), inline=False)
        msg_embed.add_field(translator.translate('embed_fields', 'calc_asignf', language), translator.translate('embed_fields', 'calc_asignv', language), inline=False)
    except Exception as e:
        msg_embed = disnake.Embed(
            title=str(translator.translate('embed_title', 'calc', language)),
            colour=config['accent_err'],
        )
        if(str(e) == 'division by zero'):
            msg_embed.add_field(translator.translate('embed_fields', 'calc_resulf', language), '```{0}```'.format(translator.translate('embed_fields', 'calc_rlerrv', language)), inline=False)
        elif(str(e) == 'Python int too large to convert to C long'):
            msg_embed.add_field(translator.translate('embed_fields', 'calc_resulf', language), '```{0}```'.format(translator.translate('embed_fields', 'calc_rlerrv2', language)), inline=False)
        elif(str(e) == '\'VariableNode\' object has no attribute'):
            msg_embed.add_field(translator.translate('embed_fields', 'calc_resulf', language), '```{0}```'.format(translator.translate('embed_fields', 'calc_rlerrv3', language)), inline=False)
        else:
            msg_embed.add_field(translator.translate('embed_fields', 'calc_resulf', language), '```{0}```'.format(translator.translate('embed_fields', 'calc_rlerrv3', language).format(str(e))), inline=False)
        msg_embed.add_field(translator.translate('embed_fields', 'calc_asignf', language), translator.translate('embed_fields', 'calc_asignv', language), inline=False)
    return msg_embed

async def sendRegularMsg(ctx, bot, config, language, disnake, translator, arg):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg)
    await ctx.reply(embed=msg_embed, mention_author=False)

async def sendSlashMsg(ctx, bot, config, language, disnake, translator, arg):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg)
    await ctx.send(embed=msg_embed)
