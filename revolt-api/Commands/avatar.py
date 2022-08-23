# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

import re

name = 'avatar'
hidden = False

async def generateEmbed(ctx, bot, config, language, voltage, translator, arg):
    if(arg.startswith("<@") and arg.endswith(">")):
        query = "".join(arg).replace("<@", "").replace(">", "")
    else:
        query = arg
    user = bot.get_user(query)
    member = ctx.server.get_member(query)
    msg_embed = voltage.SendableEmbed(
        title=str(translator.translate('embed_title', 'avatar', language)).format(user.name),
        colour=config['accent_def'],
        media=user.display_avatar.url
    )
    return msg_embed

async def sendSlashMsg(ctx, bot, config, language, voltage, translator, arg):
    msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator, arg)
    await ctx.response.send_message(embed=msg_embed)

async def sendRegularMsg(ctx, bot, config, language, voltage, translator, arg):
    msg_embed = await generateEmbed(ctx, bot, config, language, voltage, translator, arg)
    await ctx.reply(" ", embed=msg_embed)

async def sendHelpMsg(ctx, bot, config, language, voltage, translator):
    msg_embed = voltage.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format('avatar'),
        description=str(translator.translate('command_description', 'avatar', language)),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', 'avatar', language).format(config['prefix']), inline=False)
    await ctx.reply(" ", embed=msg_embed)
