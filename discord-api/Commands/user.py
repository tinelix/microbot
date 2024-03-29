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

import re

name = 'user'
hidden = False

async def generateEmbed(ctx, inst, config, disnake, translator, user, member):
    if(user == None):
        msg_embed = disnake.Embed(
            description=translator.translate('embed_description', 'error_unf', inst.language),
            colour=config['accent_err'],
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'error', inst.language)))
        return await ctx.send(embed=msg_embed)
    if(member != None and member.bot == True):
        msg_embed = disnake.Embed(
            colour=config['accent_def'],
        )
        if(user.global_name != None):
            msg_embed.set_author(name=str(translator.translate('embed_title', 'user_bot', inst.language)).format(user.global_name, user.name))
        else:
            msg_embed.set_author(name=str(translator.translate('embed_title', 'user_bot2', inst.language)).format(user.name))
    elif user.id == ctx.guild.owner_id:
        msg_embed = disnake.Embed(
            colour=config['accent_def'],
        )
        if(user.global_name != None):
            msg_embed.set_author(name=str(translator.translate('embed_title', 'user_owner', inst.language)).format(user.global_name, user.name))
        else:
            msg_embed.set_author(name=str(translator.translate('embed_title', 'user_owner2', inst.language)).format(user.name))
    else:
        msg_embed = disnake.Embed(
            colour=config['accent_def'],
        )
        if(user.global_name != None):
            msg_embed.set_author(name=str(translator.translate('embed_title', 'user', inst.language)).format(user.global_name, user.name))
        else:
            msg_embed.set_author(name=str(translator.translate('embed_title', 'user2', inst.language)).format(user.name))

    msg_embed.set_thumbnail(url=user.display_avatar)

    if(member == None):
        nick = None
        status == None
    else:
        if(member.nick == None):
            nick = translator.translate('embed_fields', 'user_nickvn', inst.language)
        else:
            nick = member.nick

        if(str(member.status) == 'online'):
            status = translator.translate('embed_fields', 'user_statusv', inst.language)
        elif(str(member.status) == 'idle'):
            status = translator.translate('embed_fields', 'user_statusv2', inst.language)
        elif(str(member.status) == 'dnd'):
            status = translator.translate('embed_fields', 'user_statusv3', inst.language)
        else:
            status = translator.translate('embed_fields', 'user_statusv4', inst.language)

        roles = ''

        for role in member.roles:
            if(str(role) != '@everyone'):
                if(member.roles.index(role) < int(len(member.roles) - 1)):
                    roles += '<@&{0}>, '.format(role.id)
                else:
                    roles += '<@&{0}>'.format(role.id)

        msg_embed.add_field(
            translator.translate('embed_fields', 'user_nickf', inst.language), nick, inline=False
        )

    msg_embed.add_field(
        translator.translate('embed_fields', 'user_regdf', inst.language), translator.translate('embed_fields', 'user_regdv', inst.language).format(translator.formatDate(user.created_at.astimezone(inst.tz), 'normal', inst.language)), inline=False
    )
    if(member == None):
        pass
    else:
        msg_embed.add_field(
            translator.translate('embed_fields', 'user_joinf', inst.language), translator.translate('embed_fields', 'user_joinv', inst.language).format(translator.formatDate(member.joined_at.astimezone(inst.tz), 'normal', inst.language)), inline=False
        )
        msg_embed.add_field(
            translator.translate('embed_fields', 'user_statusf', inst.language), status, inline=True
        )
        if(len(member.roles) - 1 > 0):
            msg_embed.add_field(
                translator.translate('embed_fields', 'user_rolesf', inst.language).format(len(member.roles) - 1), roles, inline=True
            )
    msg_embed.set_footer(text='ID: {0}'.format(user.id))
    return msg_embed

async def sendSlashMsg(ctx, inst, config, language, disnake, translator, arg):
    try:
        try:
            query = int(re.search(r'\d+', arg).group())
            user = inst.bot.get_user(query)
            member = ctx.guild.get_member(query)
        except:
            search_result = await ctx.guild.query_members(arg)
            if(len(search_result) > 0):
                member = search_result[0]
                member = ctx.guild.get_member(member.id) # dummy disnake not showing online status in 'search_members' function
                user = inst.bot.get_user(member.id)
            else:
                member = None
                user = None
        msg_embed = await generateEmbed(ctx, inst, config, disnake, translator, user, member)
        class AvatarByButton(disnake.ui.View):
            @disnake.ui.button(style=disnake.ButtonStyle.blurple, label=translator.translate('button', 'user_avatar', inst.language))
            async def show_avatar(self, button: disnake.ui.Button, interaction: disnake.Interaction):
                avatar_embed = disnake.Embed(
                    colour=config['accent_def'],
                ).set_image(user.display_avatar.url).set_author(name=str(translator.translate('embed_title', 'avatar', inst.language)).format(user.name))
                await interaction.response.send_message(embed=avatar_embed)
        await ctx.response.send_message(embed=msg_embed, view=AvatarByButton())
    except:
        pass

async def sendRegularMsg(ctx, inst, config, disnake, translator, arg):
    try:
        try:
            query = int(re.search(r'\d+', arg).group())
            user = inst.bot.get_user(query)
            member = ctx.guild.get_member(query)
        except:
            search_result = await ctx.guild.query_members(arg)
            if(len(search_result) > 0):
                member = search_result[0]
                member = ctx.guild.get_member(member.id) # dummy disnake not showing online status in 'search_members' function
                user = inst.bot.get_user(member.id)
            else:
                member = None
                user = None
        msg_embed = await generateEmbed(ctx, inst, config, disnake, translator, user, member)
        class AvatarByButton(disnake.ui.View):
            @disnake.ui.button(style=disnake.ButtonStyle.blurple, label=translator.translate('button', 'user_avatar', inst.language))
            async def show_avatar(self, button: disnake.ui.Button, interaction: disnake.Interaction):
                avatar_embed = disnake.Embed(
                    colour=config['accent_def'],
                ).set_image(user.display_avatar.url).set_author(name=str(translator.translate('embed_title', 'avatar', inst.language)).format(user.name))
                await interaction.response.send_message(embed=avatar_embed)
        await ctx.reply(embed=msg_embed, view=AvatarByButton(), mention_author=False)
    except Exception as e:
        pass

async def sendHelpMsg(ctx, bot, config, disnake, translator):
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format('user'),
        description=str(translator.translate('command_description', 'avatar', language)),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', 'user', language).format(config['prefix']), inline=False)
    await ctx.send(embed=msg_embed)
