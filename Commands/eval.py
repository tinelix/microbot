# Den4ik Bot
# Created by tretdm (aka. tinelix) at 2022-08-18 from Den4ik
# Repo: https://github.com/den4ikbot/den4ikbot
# Based on Microbot Discord bot: https://github.com/tinelix/microbot.
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

import cpuinfo # for install 'pip install py-cpuinfo'
import psutil
import platform

name = 'eval'
hidden = True

async def generateEmbed(ctx, bot, config, language, disnake, translator, arg):
    if(ctx.message.author.id == config['dev_id'] or ctx.message.author.id == config['codev_id']):  # only bot owner!
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
