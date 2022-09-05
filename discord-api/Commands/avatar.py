# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

import re

name = 'avatar'
hidden = False

async def generateEmbed(ctx, bot, config, language, disnake, translator, arg):
    try:
        query = int(re.search(r'\d+', arg).group())
        user = bot.get_user(query)
        member = ctx.guild.get_member(query)
    except:
        search_result = await ctx.guild.search_members(arg)
        if(len(search_result) > 0):
            member = search_result[0]
            user = bot.get_user(member.id)
        else:
            member = None
            user = None
    if(user != None):
        msg_embed = disnake.Embed(
            colour=config['accent_def'],
        ).set_image(user.display_avatar.url)
        msg_embed.set_author(name=str(translator.translate('embed_title', 'avatar', language)).format(user.name, user.discriminator))
    else:
        msg_embed = disnake.Embed(
            description=translator.translate('embed_description', 'error_unf', language),
            colour=config['accent_err'],
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'error', language)))
    return msg_embed

async def sendSlashMsg(ctx, bot, config, language, disnake, translator, arg):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg)
    await ctx.response.send_message(embed=msg_embed)

async def sendRegularMsg(ctx, bot, config, language, disnake, translator, arg):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg)
    await ctx.reply(embed=msg_embed, mention_author=False)

async def sendHelpMsg(ctx, bot, config, language, disnake, translator):
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format('avatar'),
        description=str(translator.translate('command_description', 'avatar', language)),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', 'avatar', language).format(config['prefix']), inline=False)
    await ctx.reply(embed=msg_embed, mention_author=False)
