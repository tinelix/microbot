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

import numexpr
import pytz

name = 'settings'
hidden = False

async def generateEmbed(ctx, bot, config, language, disnake, translator, arg, db, database, cursor, guild_data, user_data, msg_type):
    guild_id = ctx.message.guild.id
    author_id = ctx.message.author.id
    if(msg_type == "slash"):
        guild_id = ctx.guild.id
        author_id = ctx.author.id
    else:
        guild_id = ctx.message.guild.id
        author_id = ctx.message.author.id
    if(len(arg) >= 2):
        if(arg[0] == '-L' and (arg[1] == 'en_US' or arg[1] == 'ru_RU')):
            if ctx.author.guild_permissions.administrator:
                await db.update_value(ctx, database, cursor, 'guilds', 'language', '\'{0}\''.format(arg[1]), guild_id)
                msg_embed = disnake.Embed(
                    description=str(translator.translate('embed_description', 'settings_done', arg[1])),
                    colour=config['accent_def']
                )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'settings', arg[1])))
            else:
                msg_embed = disnake.Embed(
                    description=str(translator.translate('embed_description', 'forbidden', language)),
                    colour=config['accent_err']
                )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'forbidden', language)))
        elif(arg[0] == '-P'):
            if(msg_type == "slash"):
                guild_id = ctx.guild.id
            if ctx.author.guild_permissions.administrator:
                await db.update_value(ctx, database, cursor, 'guilds', 'prefix', '\'{0}\''.format(arg[1]), guild_id)
                msg_embed = disnake.Embed(
                    description=str(translator.translate('embed_description', 'settings_done', language)),
                    colour=config['accent_def']
                )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
            else:
                msg_embed = disnake.Embed(
                    description=str(translator.translate('embed_description', 'forbidden', language)),
                    colour=config['accent_err']
                )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'forbidden', language)))
        elif(arg[0] == '-tz'):
            try:
                tz = pytz.timezone(arg[1])
                await db.update_value(ctx, database, cursor, 'users', 'timezone', '\'{0}\''.format(arg[1]), author_id)
                msg_embed = disnake.Embed(
                    description=str(translator.translate('embed_description', 'settings_done', language)),
                    colour=config['accent_def']
                )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
            except pytz.UnknownTimeZoneError as ex:
                msg_embed = disnake.Embed(
                    description=str(translator.translate('embed_description', 'tz_invalidabbr', language)),
                    colour=config['accent_err']
                )
                msg_embed.set_author(name=str(translator.translate('embed_title', 'error', language)))
        else:
            msg_embed = disnake.Embed(
                description=str(translator.translate('embed_description', 'settings', language)),
                colour=config['accent_def'],
            )
            msg_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
            msg_embed.add_field(translator.translate('embed_fields', 'settings_availoptf', language),
                                translator.translate('embed_fields', 'settings_availoptv', language), inline=False)
    else:
        msg_embed = disnake.Embed(
            colour=config['accent_def'],
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
        msg_embed.add_field(translator.translate('embed_fields', 'settings_gsettf', language),
                            translator.translate('embed_fields', 'settings_gsettv', language).format(f'`{guild_data[3]}`'), inline=False)
        msg_embed.add_field(translator.translate('embed_fields', 'settings_usettf', language),
                            translator.translate('embed_fields', 'settings_usettv', language).format(f'`{user_data[5]}`'), inline=False)
        msg_embed.add_field(translator.translate('embed_fields', 'settings_availoptf', language),
                            translator.translate('embed_fields', 'settings_availoptv', language), inline=False)
    return msg_embed

async def sendRegularMsg(ctx, bot, config, language, disnake, translator, arg, db, database, cursor, guild_data, user_data):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg, db,
                                    database, cursor, guild_data, user_data, 'default')
    class SettingsByButton(disnake.ui.View):
        @disnake.ui.button(style=disnake.ButtonStyle.blurple, label='🚩')
        async def show_changing_language_embed(self, button: disnake.ui.Button, interaction: disnake.Interaction):
            language_embed = disnake.Embed(
                colour=config['accent_def'],
            )
            language_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
            language_embed.add_field(translator.translate('embed_fields', 'help_exampf', language),
                                     translator.translate('command_examples', 'settings_lang', language).format(config['prefix']),
                                     inline=False)
            await interaction.response.send_message(embed=language_embed)
        @disnake.ui.button(style=disnake.ButtonStyle.blurple, label='🪄')
        async def show_changing_prefix_embed(self, button: disnake.ui.Button, interaction: disnake.Interaction):
            language_embed = disnake.Embed(
                colour=config['accent_def'],
            )
            language_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
            language_embed.add_field(translator.translate('embed_fields', 'help_exampf', language),
                                     translator.translate('command_examples', 'settings_prefix', language).format(config['prefix']),
                                     inline=False)
            await interaction.response.send_message(embed=language_embed)
        @disnake.ui.button(style=disnake.ButtonStyle.blurple, label='🕒')
        async def show_changing_tz_embed(self, button: disnake.ui.Button, interaction: disnake.Interaction):
            language_embed = disnake.Embed(
                colour=config['accent_def'],
            )
            language_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
            language_embed.add_field(translator.translate('embed_fields', 'help_exampf', language),
                                     translator.translate('command_examples', 'settings_tz', language).format(config['prefix']),
                                     inline=False)
            await interaction.response.send_message(embed=language_embed)
    if(len(arg) >= 2):
        if(arg[0] == '-L' and (arg[1] == 'en_US' or arg[1] == 'ru_RU')):
            await ctx.reply(embed=msg_embed, mention_author=False)
        elif(arg[0] == '-P'):
            await ctx.reply(embed=msg_embed, mention_author=False)
        elif(arg[0] == '-tz'):
            await ctx.reply(embed=msg_embed, mention_author=False)
        else:
            await ctx.reply(embed=msg_embed, view=SettingsByButton(), mention_author=False)
    else:
        await ctx.reply(embed=msg_embed, view=SettingsByButton(), mention_author=False)

async def sendSlashMsg(ctx, bot, config, language, disnake, translator, arg, db, database, cursor, guild_data, user_data):
    msg_embed = await generateEmbed(ctx, bot, config, language, disnake, translator, arg, db, database, cursor, guild_data,
                                    user_data, 'slash')
    class SettingsByButton(disnake.ui.View):
        @disnake.ui.button(style=disnake.ButtonStyle.blurple, label='🚩')
        async def show_changing_language_embed(self, button: disnake.ui.Button, interaction: disnake.Interaction):
            language_embed = disnake.Embed(
                colour=config['accent_def'],
            )
            language_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
            language_embed.add_field(translator.translate('embed_fields', 'help_exampf', language),
                                     translator.translate('command_examples', 'settings_lang2', language).format("/"),
                                     inline=False)
            await interaction.response.send_message(embed=language_embed)
        @disnake.ui.button(style=disnake.ButtonStyle.blurple, label='🪄')
        async def show_changing_prefix_embed(self, button: disnake.ui.Button, interaction: disnake.Interaction):
            language_embed = disnake.Embed(
                colour=config['accent_def'],
            )
            language_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
            language_embed.add_field(translator.translate('embed_fields', 'help_exampf', language),
                                     translator.translate('command_examples', 'settings_pref2', language).format("/"),
                                     inline=False)
            await interaction.response.send_message(embed=language_embed)
        @disnake.ui.button(style=disnake.ButtonStyle.blurple, label='🕒')
        async def show_changing_tz_embed(self, button: disnake.ui.Button, interaction: disnake.Interaction):
            language_embed = disnake.Embed(
                colour=config['accent_def'],
            )
            language_embed.set_author(name=str(translator.translate('embed_title', 'settings', language)))
            language_embed.add_field(translator.translate('embed_fields', 'help_exampf', language),
                                     translator.translate('command_examples', 'settings_tz2', language).format("/"),
                                     inline=False)
            await interaction.response.send_message(embed=language_embed)
    if(len(arg) >= 2):
        if(arg[0] == '-L' and (arg[1] == 'en_US' or arg[1] == 'ru_RU')):
            await ctx.send(embed=msg_embed)
        elif(arg[0] == '-P'):
            await ctx.send(embed=msg_embed)
        elif(arg[0] == '-tz'):
            await ctx.send(embed=msg_embed)
        else:
            await ctx.send(embed=msg_embed, view=SettingsByButton())
    else:
        await ctx.send(embed=msg_embed, view=SettingsByButton())
