# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

import re

name = 'user'
hidden = False

async def generateEmbed(ctx, bot, config, language, disnake, translator, user, member, tz):
    if(user == None):
        msg_embed = disnake.Embed(
            description=translator.translate('embed_description', 'error_unf', language),
            colour=config['accent_err'],
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'error', language)))
        return await ctx.send(embed=msg_embed)
    if(member != None and member.bot == True):
        msg_embed = disnake.Embed(
            colour=config['accent_def'],
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'user_bot', language)).format(user.name, user.discriminator))
    elif user.id == ctx.guild.owner_id:
        msg_embed = disnake.Embed(
            colour=config['accent_def'],
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'user_owner', language)).format(user.name, user.discriminator))
    else:
        msg_embed = disnake.Embed(
            colour=config['accent_def'],
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'user', language)).format(user.name, user.discriminator))

    msg_embed.set_thumbnail(url=user.display_avatar)

    if(member == None):
        nick = None
        status == None
    else:

        if(member.nick == None):
            nick = translator.translate('embed_fields', 'user_nickvn', language)
        else:
            nick = member.nick

        if(str(member.status) == 'online'):
            status = translator.translate('embed_fields', 'user_statusv', language)
        elif(str(member.status) == 'idle'):
            status = translator.translate('embed_fields', 'user_statusv2', language)
        elif(str(member.status) == 'dnd'):
            status = translator.translate('embed_fields', 'user_statusv3', language)
        else:
            status = translator.translate('embed_fields', 'user_statusv4', language)

        roles = ''

        for role in member.roles:
            if(str(role) != '@everyone'):
                if(member.roles.index(role) < int(len(member.roles) - 1)):
                    roles += '{0}, '.format(str(role))
                else:
                    roles += '{0}'.format(str(role))

        msg_embed.add_field(
            translator.translate('embed_fields', 'user_nickf', language), nick, inline=False
        )

    msg_embed.add_field(
        translator.translate('embed_fields', 'user_regdf', language), translator.translate('embed_fields', 'user_regdv', language).format(translator.formatDate(user.created_at.astimezone(tz), 'normal', language)), inline=False
    )
    if(member == None):
        pass
    else:
        msg_embed.add_field(
            translator.translate('embed_fields', 'user_joinf', language), translator.translate('embed_fields', 'user_joinv', language).format(translator.formatDate(member.joined_at.astimezone(tz), 'normal', language)), inline=False
        )
        msg_embed.add_field(
            translator.translate('embed_fields', 'user_statusf', language), status, inline=True
        )
        if(len(member.roles) - 1 > 0):
            msg_embed.add_field(
                translator.translate('embed_fields', 'user_rolesf', language).format(len(member.roles) - 1), roles, inline=True
            )
    msg_embed.set_footer(text='ID: {0}'.format(user.id))
    return msg_embed

async def sendSlashMsg(ctx, bot, config, language, disnake, translator, arg, tz):
    try:
        try:
            query = int(re.search(r'\d+', arg).group())
            user = bot.get_user(query)
            member = ctx.guild.get_member(query)
        except:
            search_result = await ctx.guild.query_members(arg)
            if(len(search_result) > 0):
                member = search_result[0]
                member = ctx.guild.get_member(member.id) # dummy disnake not showing online status in 'search_members' function
                user = bot.get_user(member.id)
            else:
                member = None
                user = None
        msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, user, member, tz)
        class AvatarByButton(disnake.ui.View):
            @disnake.ui.button(style=disnake.ButtonStyle.blurple, label=translator.translate('button', 'user_avatar', language))
            async def show_avatar(self, button: disnake.ui.Button, interaction: disnake.Interaction):
                avatar_embed = disnake.Embed(
                    colour=config['accent_def'],
                ).set_image(user.display_avatar.url).set_author(name=str(translator.translate('embed_title', 'avatar', language)).format(user.name, user.discriminator))
                await interaction.response.send_message(embed=avatar_embed)
        await ctx.response.send_message(embed=msg_embed, view=AvatarByButton())
    except:
        pass

async def sendRegularMsg(ctx, bot, config, language, disnake, translator, arg, tz):
    try:
        try:
            query = int(re.search(r'\d+', arg).group())
            user = bot.get_user(query)
            member = ctx.guild.get_member(query)
        except:
            search_result = await ctx.guild.query_members(arg)
            if(len(search_result) > 0):
                member = search_result[0]
                member = ctx.guild.get_member(member.id) # dummy disnake not showing online status in 'search_members' function
                user = bot.get_user(member.id)
            else:
                member = None
                user = None
        msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, user, member, tz)
        class AvatarByButton(disnake.ui.View):
            @disnake.ui.button(style=disnake.ButtonStyle.blurple, label=translator.translate('button', 'user_avatar', language))
            async def show_avatar(self, button: disnake.ui.Button, interaction: disnake.Interaction):
                avatar_embed = disnake.Embed(
                    colour=config['accent_def'],
                ).set_image(user.display_avatar.url).set_author(name=str(translator.translate('embed_title', 'avatar', language)).format(user.name, user.discriminator))
                await interaction.response.send_message(embed=avatar_embed)
        await ctx.reply(embed=msg_embed, view=AvatarByButton(), mention_author=False)
    except Exception as e:
        pass

async def sendHelpMsg(ctx, bot, config, language, disnake, translator):
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', language)).format('user'),
        description=str(translator.translate('command_description', 'avatar', language)),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', language), translator.translate('command_examples', 'user', language).format(config['prefix']), inline=False)
    await ctx.send(embed=msg_embed)
