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
import time

name = 'ping'
hidden = False

async def generateEmbed(ctx, bot, config, language, disnake, translator, ping):
    msg_embed = disnake.Embed(
        colour=config['accent_def'],
    )
    shard_latency = round(bot.get_shard(ctx.guild.shard_id).latency * 1000, 2)
    msg_embed.set_author(name=str(translator.translate('embed_title', 'ping', language)))
    if(ping > 0):
        msg_embed.add_field(translator.translate('embed_fields', 'ping_statisticsf', language), translator.translate('embed_fields', 'ping_statisticsv2', language).format(round(bot.latency * 1000, 2), shard_latency, round(ping, 2)))
    else:
        msg_embed.add_field(translator.translate('embed_fields', 'ping_statisticsf', language), translator.translate('embed_fields', 'ping_statisticsv', language).format(round(bot.latency * 1000, 2), shard_latency))
    return msg_embed

async def sendSlashMsg(ctx, bot, config, language, disnake, translator):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, 0)
    await ctx.response.send_message(embed=msg_embed)

async def sendRegularMsg(ctx, bot, config, language, disnake, translator):
    before = time.monotonic()
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, 0)
    msg = await ctx.reply(embed=msg_embed, mention_author=False)
    # getting execution time
    ping = (time.monotonic() - before) * 1000
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, ping)
    await msg.edit(embed=msg_embed)
