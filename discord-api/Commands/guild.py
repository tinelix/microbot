# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

import re

async def generateEmbed(ctx, bot, config, language, disnake, translator):
    guild = ctx.guild
    try:
        guild_pr = await bot.fetch_guild_preview(ctx.guild.id)
    except:
        guild_pr = None
    owner = bot.get_user(guild.owner_id)

    msg_embed = disnake.Embed(
        colour=config['accent_def'],
    )
    if(guild_pr == None):
        pass
    else:
        msg_embed.set_thumbnail(url=guild_pr.icon)

    msg_embed.set_author(name=ctx.guild.name)

    if(guild.verification_level == disnake.VerificationLevel.none):
        verif_lvl = translator.translate('embed_fields', 'guild_mlvlv', language)
    elif(guild.verification_level == disnake.VerificationLevel.low):
        verif_lvl = translator.translate('embed_fields', 'guild_mlvlv2', language)
    elif(guild.verification_level == disnake.VerificationLevel.medium):
        verif_lvl = translator.translate('embed_fields', 'guild_mlvlv3', language)
    elif(guild.verification_level == disnake.VerificationLevel.high):
        verif_lvl = translator.translate('embed_fields', 'guild_mlvlv4', language)
    elif(guild.verification_level == disnake.VerificationLevel.highest):
        verif_lvl = translator.translate('embed_fields', 'guild_mlvlv5', language)

    people = 0
    bots = 0
    online = 0

    for member in guild.members:
        if(member.bot == True):
            bots += 1
        else:
            people += 1
        if(str(member.status) == 'online' or str(member.status) == 'idle' or str(member.status) == 'dnd'):
            online += 1

    msg_embed.add_field(
        translator.translate('embed_fields', 'guild_ownerf', language), translator.translate('embed_fields', 'guild_ownerv', language).format(owner.name, owner.discriminator), inline=True
    )
    msg_embed.add_field(
        translator.translate('embed_fields', 'guild_crtf', language), translator.translate('embed_fields', 'guild_crtv', language).format(guild.created_at.strftime("%Y-%m-%d %H:%M:%S")), inline=True
    )
    msg_embed.add_field(
        translator.translate('embed_fields', 'guild_blvlf', language), translator.translate('embed_fields', 'guild_blvlv', language).format(guild.premium_tier), inline=True
    )
    msg_embed.add_field(
        translator.translate('embed_fields', 'guild_mlvlf', language), verif_lvl, inline=False
    )
    msg_embed.add_field(
        translator.translate('embed_fields', 'guild_statsf', language), translator.translate('embed_fields', 'guild_statsv', language).format(guild.member_count, people, round(people / (guild.member_count * 0.01), 2), bots, round(bots / (guild.member_count * 0.01), 2), online, round(online / (guild.member_count * 0.01), 2), len(guild.channels)), inline=False
    )

    msg_embed.set_footer(text='ID: {0}'.format(guild.id))
    return msg_embed

async def sendSlashMsg(ctx, bot, config, language, disnake, translator):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator)
    await ctx.response.send_message(embed=msg_embed)

async def sendRegularMsg(ctx, bot, config, language, disnake, translator):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator)
    await ctx.reply(embed=msg_embed, mention_author=False)

async def sendHelpMsg(ctx, bot, config, language, disnake, translator):
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format('user'),
        description=str(translator.translate('command_description', 'avatar', 'ru_RU')),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', 'ru_RU'), translator.translate('command_examples', 'user', 'ru_RU').format(config['prefix']), inline=False)
    await ctx.send(embed=msg_embed)
