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

name = 'publish'
hidden = False

async def generateEmbed(ctx, bot, config, language, disnake, translator, arg):
    community = ""
    for guild_feature in ctx.message.guild.features:
        if guild_feature == "COMMUNITY":
            community = "COMMUNITY"
    if(community != "COMMUNITY"):
        msg_embed = disnake.Embed(
            colour=config['accent_err'],
            description=translator.translate('embed_description', 'publish_isntcomm', language)
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'error', language)))
    elif(str(ctx.message.channel.type) == "news"):
        if(len(ctx.message.attachments) >= 1):
            attachment_url = ctx.message.attachments[0].url
        else:
            attachment_url = None
        msg_embed = disnake.Embed(
            colour=config['accent_def'],
            description=arg
        )
        msg_embed.set_author(name=translator.translate('embed_title', 'msg_author', language).format(ctx.message.author.global_name, ctx.message.author.name))
        if(attachment_url != None):
            msg_embed.set_image(attachment_url)
    else:
        msg_embed = disnake.Embed(
            colour=config['accent_err'],
            description=translator.translate('embed_description', 'publish_isntnewsch', language)
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'error', language)))
    return msg_embed

async def generateSlashEmbed(ctx, bot, config, language, disnake, translator, arg):
    community = ""
    for guild_feature in ctx.guild.features:
        if guild_feature == "COMMUNITY":
            community = "COMMUNITY"
    if(community != "COMMUNITY"):
        msg_embed = disnake.Embed(
            colour=config['accent_err'],
            description=translator.translate('embed_description', 'publish_isntcomm', language)
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'error', language)))
    elif(str(ctx.channel.type) == "news"):
        msg_embed = disnake.Embed(
            colour=config['accent_def'],
            description=arg
        )
        msg_embed.set_author(name=translator.translate('embed_title', 'msg_author', language).format(ctx.author.global_name, ctx.author.name))
    else:
        msg_embed = disnake.Embed(
            colour=config['accent_err'],
            description=translator.translate('embed_description', 'publish_isntnewsch', language)
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'error', language)))
    return msg_embed

async def sendRegularMsg(ctx, bot, config, language, disnake, translator, arg):
    try:
        msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg)
        msg = await ctx.send(embed=msg_embed)
        community = ""
        for guild_feature in ctx.message.guild.features:
            if guild_feature == "COMMUNITY":
                community = "COMMUNITY"
        if(community == "COMMUNITY" and str(ctx.message.channel.type) == "news"):
            await msg.publish()
            await ctx.message.delete()
    except:
        pass

async def sendSlashMsg(ctx, bot, config, language, disnake, translator, arg):
    try:
        msg_embed = await generateSlashEmbed(ctx, bot, config, language, disnake, translator, arg)
        msg = await ctx.channel.send(embed=msg_embed)
        community = ""
        for guild_feature in ctx.guild.features:
            if guild_feature == "COMMUNITY":
                community = "COMMUNITY"
        if(community == "COMMUNITY" and str(ctx.channel.type) == "news"):
            await msg.publish()
        await ctx.send('✅', delete_after=5)
    except:
        pass

async def sendHelpMsg(ctx, bot, config, language, disnake, translator):
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format('user'),
        description=str(translator.translate('command_description', 'avatar', 'ru_RU')),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', 'ru_RU'), translator.translate('command_examples', 'user', 'ru_RU').format(config['prefix']), inline=False)
    await ctx.send(embed=msg_embed)
