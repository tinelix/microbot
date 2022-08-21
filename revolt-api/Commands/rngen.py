# Microbot Revolt bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

import random

async def generateEmbed(ctx, bot, config, language, voltage, translator, arg):
    random_numb = random.randint(int(arg.split('-')[0]), int(arg.split('-')[1]))
    msg_embed = voltage.SendableEmbed(
        str(translator.translate('embed_title', 'rngen', language)),
        colour=config['accent_def'],
    )
    msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'rngen_numbf', language), random_numb)
    return msg_embed

async def sendSlashMsg(ctx, bot, config, language, voltage, translator, arg):
    try:
        msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator, arg)
        await ctx.response.send_message(embed=msg_embed)
    except:
        await sendHelpMsg(ctx, bot, config, language, voltage, translator)

async def sendRegularMsg(ctx, bot, config, language, voltage, translator, arg):
    try:
        if(len(arg.split('-')) == 2):
            msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator, arg)
            await ctx.reply(" ", embed=msg_embed)
        else:
            await sendHelpMsg(ctx, bot, config, language, voltage, translator)
    except:
        await sendHelpMsg(ctx, bot, config, language, voltage, translator)

async def sendHelpMsg(ctx, bot, config, language, voltage, translator):
    msg_embed = voltage.SendableEmbed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format('rngen'),
        description=str(translator.translate('command_description', 'rngen', language)),
        colour=config['accent_def'],
    )
    msg_embed.description = '### {0}\r\n{1}\r\n'.format(translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', 'rngen', language).format(config['prefix']))
    await ctx.send(embed=msg_embed)
