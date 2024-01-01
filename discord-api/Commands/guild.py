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

import re

name = 'guild'
hidden = False

async def generateEmbed(ctx, inst, config, disnake, translator):
    guild = ctx.guild
    try:
        guild_pr = await inst.bot.fetch_guild_preview(ctx.guild.id)
    except:
        guild_pr = None
    owner = inst.bot.get_user(guild.owner_id)

    badges = ''

    for guild_feature in guild.features:
        if(guild.features.index(guild_feature) == 0):
            if guild_feature == "AUTO_MODERATION":
                badges += '`{0}`'.format(translator.translate('embed_fields', 'guild_featurv', inst.language))
            elif guild_feature == "COMMUNITY":
                badges += '`{0}`'.format(translator.translate('embed_fields', 'guild_featurv2', inst.language))
            elif guild_feature == "NEWS":
                badges += '`{0}`'.format(translator.translate('embed_fields', 'guild_featurv3', inst.language))
            elif guild_feature == "TEXT_IN_VOICE_ENABLED":
                badges += '`{0}`'.format(translator.translate('embed_fields', 'guild_featurv4', inst.language))
            elif guild_feature == "WELCOME_SCREEN_ENABLED":
                badges += '`{0}`'.format(translator.translate('embed_fields', 'guild_featurv5', inst.language))
        else:
            if guild_feature == "AUTO_MODERATION":
                badges += '\r\n`{0}`'.format(translator.translate('embed_fields', 'guild_featurv', inst.language))
            elif guild_feature == "COMMUNITY":
                badges += '\r\n`{0}`'.format(translator.translate('embed_fields', 'guild_featurv2', inst.language))
            elif guild_feature == "NEWS":
                badges += '\r\n`{0}`'.format(translator.translate('embed_fields', 'guild_featurv3', inst.language))
            elif guild_feature == "TEXT_IN_VOICE_ENABLED":
                badges += '\r\n`{0}`'.format(translator.translate('embed_fields', 'guild_featurv4', inst.language))
            elif guild_feature == "WELCOME_SCREEN_ENABLED":
                badges += '\r\n`{0}`'.format(translator.translate('embed_fields', 'guild_featurv5', inst.language))

    msg_embed = disnake.Embed(
        colour=config['accent_def'],
    )

    if(guild_pr):
        msg_embed.set_thumbnail(url=guild_pr.icon)

    msg_embed.set_author(name='🏠 {0}'.format(ctx.guild.name))

    if(guild.description):
        msg_embed.description = guild.description.replace('_', '\_').replace('`', '\`').replace('*', '\*').replace('~', '\~').replace('|', '\|').replace('>', '\>')

    if(guild.verification_level == disnake.VerificationLevel.none):
        verif_lvl = translator.translate('embed_fields', 'guild_mlvlv', inst.language)
    elif(guild.verification_level == disnake.VerificationLevel.low):
        verif_lvl = translator.translate('embed_fields', 'guild_mlvlv2', inst.language)
    elif(guild.verification_level == disnake.VerificationLevel.medium):
        verif_lvl = translator.translate('embed_fields', 'guild_mlvlv3', inst.language)
    elif(guild.verification_level == disnake.VerificationLevel.high):
        verif_lvl = translator.translate('embed_fields', 'guild_mlvlv4', inst.language)
    elif(guild.verification_level == disnake.VerificationLevel.highest):
        verif_lvl = translator.translate('embed_fields', 'guild_mlvlv5', inst.language)

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
        translator.translate('embed_fields', 'guild_ownerf', inst.language), translator.translate('embed_fields', 'guild_ownerv', inst.language).format('<@{0}>'.format(owner.id), owner.global_name, owner.name), inline=True
    )
    msg_embed.add_field(
        translator.translate('embed_fields', 'guild_crtf', inst.language), translator.translate('embed_fields', 'guild_crtv', inst.language).format(translator.formatDate(guild.created_at.astimezone(inst.tz), 'normal', inst.language)), inline=True
    )
    if(guild.premium_tier == 0):
        msg_embed.add_field(
            translator.translate('embed_fields', 'guild_blvlf', inst.language), translator.translate('embed_fields', 'guild_blvlv', inst.language).format(guild.premium_tier), inline=True
        )
    else:
        msg_embed.add_field(
            translator.translate('embed_fields', 'guild_blvlf', inst.language), translator.translate('embed_fields', 'guild_blvlv2', inst.language).format(guild.premium_tier, guild.premium_subscription_count), inline=True
        )
    msg_embed.add_field(
        translator.translate('embed_fields', 'guild_mlvlf', language), verif_lvl, inline=False
    )
    msg_embed.add_field(
        translator.translate('embed_fields', 'guild_statsf', language), translator.translate('embed_fields', 'guild_statsv', language).format(guild.member_count, people, round(people / (guild.member_count * 0.01), 2), bots, round(bots / (guild.member_count * 0.01), 2), online, round(online / (guild.member_count * 0.01), 2), len(guild.channels)), inline=True
    )

    if(len(badges) > 0):
        msg_embed.add_field(
            translator.translate('embed_fields', 'guild_featurf', inst.language), badges, inline=True
        )

    if(guild.rules_channel != None):
        msg_embed.add_field(
            translator.translate('embed_fields', 'guild_rulesf', inst.language), translator.translate('embed_fields', 'guild_rulesv', inst.language).format(f'<#{guild.rules_channel.id}>'), inline=False
        )

    msg_embed.set_footer(text='ID: {0}'.format(guild.id))
    return msg_embed

async def sendSlashMsg(ctx, inst, config, disnake, translator):
    msg_embed = await generateEmbed(ctx, inst, config, disnake, translator)
    await ctx.response.send_message(embed=msg_embed)

async def sendRegularMsg(ctx, inst, config, disnake, translator):
    msg_embed = await generateEmbed(ctx, inst, config, disnake, translator)
    await ctx.reply(embed=msg_embed, mention_author=False)

async def sendHelpMsg(ctx, inst, config, disnake, translator):
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', inst.language)).format('user'),
        description=str(translator.translate('command_description', 'avatar', inst.language)),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', inst.language), translator.translate('command_examples', 'user', inst.language).format(config['prefix']), inline=False)
    await ctx.send(embed=msg_embed)
