# Copyright © 2023 Dmitry Tretyakov (aka. Tinelix)
#
# This program is free software: you can redistribute it and/or modify it under the terms of
# the GNU Affero General Public License 3 (or any later version) and/or Apache License 2
# See the following files in this directory for the precise terms and conditions of either
# license:
#
#     LICENSE.APACHE
#     LICENSE.AGPL
#
# Please see each file in the implementation for copyright and licensing
# information, (in the opening comment of each file).

import cpuinfo # for install 'pip install py-cpuinfo'
import psutil
import platform
import traceback
from datetime import date

name = 'eval'
hidden = True

async def generateEmbed(ctx, bot, config, language, disnake, translator, arg):
    if(ctx.message.author.id == config['dev_id']):  # only bot owner!
        try:
            msg_embed = disnake.Embed(
                colour=config['accent_def'],
            )
            msg_embed.set_author(name=str(translator.translate('embed_title', 'eval', language)))
            if(arg == 'guilds'): # guild list for statistical data
                eval_r = ''
                for guild in bot.guilds:
                    online = 0
                    for member in guild.members:
                        if(str(member.status) == 'online' or str(member.status) == 'idle' or str(member.status) == 'dnd'):
                            online += 1
                    eval_r += '{0:03d}. {1}\r\n└────┤ {2: 4d} members │ {3: 4d} online │\r\n'.format(bot.guilds.index(guild) + 1, guild.name, guild.member_count, online)
            elif("token" in arg):
                eval_r = 'https://www.youtube.com/watch?v=2bXP5VNukmY'
            else:
                if(len(str(eval(arg))) > 1000):
                    eval_r = 'Content is too large (> 1000 symbols)'
                else:
                    eval_r = str(eval(arg))
            if(arg == 'guilds'):
                pass
            else:
                msg_embed.add_field(translator.translate('embed_fields', 'eval_codelf', language), '```py\r\n{0}```'.format(arg), inline=False)
            msg_embed.add_field(translator.translate('embed_fields', 'eval_resulf', language), '```py\r\n{0}```'.format(eval_r), inline=False)
        except Exception as e:
            msg_embed = disnake.Embed(
                colour=config['accent_err'],
            )
            msg_embed.set_author(name=str(translator.translate('embed_title', 'eval', language)))
            msg_embed.add_field(translator.translate('embed_fields', 'eval_resulf', language), '```py\r\n{0}```'.format("".join(traceback.TracebackException.from_exception(e).format())), inline=False)
    else:
        msg_embed = disnake.Embed(
            description=str(translator.translate('embed_description', 'forbidden', language)),
            colour=config['accent_err']
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'forbidden', language)))
    return msg_embed

async def sendRegularMsg(ctx, bot, config, language, disnake, translator, arg):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg)
    await ctx.reply(embed=msg_embed, mention_author=False)

async def sendGoodbyeMsg(ctx, bot, config, language, disnake, translator):
    if(ctx.message.author.id == config['dev_id']):  # only bot owner!
        now = date.today()
        current_dt = now.strftime("%y-%m-%d %H:%M:%S")
        print(" [{0}] Bot is shutting down...\r\n", current_dt)
        await ctx.reply(":wave:", mention_author=False)
        await ctx.bot.close()
