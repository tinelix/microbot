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

import datetime
import time
import re

name = 'timers'
hidden = False

async def generateEmbed(ctx, inst, config, disnake, translator, arg, db):
    msg_embed = disnake.Embed(
        colour=config['accent_def'],
    )
    msg_embed.set_author(name=translator.translate('embed_title', 'timers', inst.language))
    args = arg.split(' ')

    if(len(args) >= 1):
        author_id = ctx.message.author.id
        current_dt = datetime.datetime.now()
        if(args[0] == '-Cr'):
            try:
                timer_name = re.search('-Cr (.+?) -t', arg).group(1)
                timer_action_date = re.search('-t (.+?) -e', arg).group(1)
                timer_actiondt = datetime.datetime.strptime(timer_action_date, "%Y-%m-%d %H:%M:%S")
                remaining_time = timer_actiondt.astimezone(tz) - current_dt.astimezone(inst.tz)
                if(remaining_time.total_seconds() >= 0):
                    emoji = re.search('-e (.+?)', arg).group(1)
                    await db.add_timer_value(inst.database, author_id, emoji, timer_name, timer_action_date, 'remaining', inst.cursor)
                    msg_embed.description = translator.translate('embed_description', 'timers_created', inst.language)
                else:
                    msg_embed = disnake.Embed(
                        colour=config['accent_err'],
                        description=translator.translate('embed_description', 'timers_invupcomdt', inst.language).format(config['prefix'])
                    )
                    msg_embed.set_author(name=translator.translate('embed_title', 'error', inst.language))
            except Exception as ex:
                print(ex)
                msg_embed = disnake.Embed(
                    colour=config['accent_err'],
                    description='{0}\r\n{1}'.format(translator.translate('embed_description', 'invalid_cmd_usage', inst.language), translator.translate('command_examples', 'timers_create', inst.language).format(config['prefix']))
                )
                msg_embed.set_author(name=translator.translate('embed_title', 'timers', language))
        elif(args[0] == '-Ce'):
            try:
                timer_name = re.search('-Ce (.+?) -t', arg).group(1)
                timer_action_date = re.search('-t (.+?) -e', arg).group(1)
                timer_actiondt = datetime.datetime.strptime(timer_action_date, "%Y-%m-%d %H:%M:%S")
                elapsed_time = current_dt.astimezone(tz) - timer_actiondt.astimezone(tz)
                if(elapsed_time.total_seconds() >= 0):
                    emoji = re.search('-e (.+?)', arg).group(1)
                    await db.add_timer_value(inst.database, author_id, emoji, timer_name, timer_action_date, 'elapsed', inst.cursor)
                    msg_embed.description = translator.translate('embed_description', 'timers_created', inst.language).format(config['prefix'])
                else:
                    msg_embed = disnake.Embed(
                        colour=config['accent_err'],
                        description=translator.translate('embed_description', 'timers_invelapsdt', inst.language).format(config['prefix'])
                    )
                    msg_embed.set_author(name=translator.translate('embed_title', 'error', inst.language))
            except Exception as ex:
                print(ex)
                msg_embed = disnake.Embed(
                    colour=config['accent_err'],
                    description='{0}\r\n{1}'.format(translator.translate('embed_description', 'invalid_cmd_usage', inst.language), translator.translate('command_examples', 'timers_create', inst.language).format(config['prefix']))
                )
                msg_embed.set_author(name=translator.translate('embed_title', 'timers', language))
        elif(args[0] == '-D'):
            if(len(args) >= 2):
                timer_name = " ".join(args[1:])
                await db.delete_timer(database, cursor, timer_name, author_id)
                msg_embed.description = translator.translate('embed_description', 'timers_deleted', inst.language).format(config['prefix'])
            else:
                msg_embed.description = translator.translate('command_examples', 'timers_delete', inst.language).format(config['prefix'])
        else:
            return await generateTimersEmbed(ctx, inst, config, disnake, translator, db)
    return msg_embed

async def generateTimersEmbed(ctx, inst, config, disnake, translator, db):
    msg_embed = disnake.Embed(
        colour=config['accent_def'],
    )
    msg_embed.set_author(name=translator.translate('embed_title', 'timers', inst.language))
    timers = await db.get_timers_by_user(inst.database, inst.cursor, ctx.message.author.id)
    if(len(timers) > 0):
        current_dt = datetime.datetime.now()
        for timer in timers:
            timer_actiondt = datetime.datetime.strptime(timer[3], "%Y-%m-%d %H:%M:%S")
            if(timer[4] == 'remaining'):
                remaining_time = timer_actiondt.astimezone(inst.tz) - current_dt.astimezone(inst.tz)
                if(remaining_time.total_seconds() >= 0):
                    remaining_hours = (remaining_time.seconds // 3600) % 24
                    remaining_minutes = (remaining_time.seconds % 3600) // 60
                    msg_embed.add_field('{0} {1}'.format(timer[2], timer[0]), translator.translate('embed_fields', 'timers_dcr', inst.language).format(remaining_time.days, remaining_hours, remaining_minutes, remaining_time.seconds % 60), inline=False)
                else:
                    msg_embed.add_field('{0} {1}'.format(timer[2], timer[0]), translator.translate('embed_fields', 'timers_dco', inst.language), inline=False)
            elif(timer[4] == 'elapsed'):
                elapsed_time = current_dt.astimezone(inst.tz) - timer_actiondt.astimezone(inst.tz)
                if(elapsed_time.total_seconds() >= 0):
                    elapsed_hours = (elapsed_time.seconds // 3600) % 24
                    elapsed_minutes = (elapsed_time.seconds % 3600) // 60
                    msg_embed.add_field('{0} {1}'.format(timer[2], timer[0]), translator.translate('embed_fields', 'timers_dce', inst.language).format(elapsed_time.days, elapsed_hours, elapsed_minutes, elapsed_time.seconds % 60), inline=False)
                else:
                    msg_embed.add_field('{0} {1}'.format(timer[2], timer[0]), translator.translate('embed_fields', 'timers_dco', inst.language), inline=False)
    else:
        msg_embed.description = translator.translate('embed_description', 'timers', inst.language)
    return msg_embed

async def sendRegularMsgWithoutArgs(ctx, inst, config, disnake, translator, db):
    msg_embed = await generateTimersEmbed(ctx, inst, config, disnake, translator, db)
    class TimerByButtons(disnake.ui.View):
        @disnake.ui.button(style=disnake.ButtonStyle.green, label=translator.translate('button', 'timers_create', inst.language))
        async def create_timer(self, button: disnake.ui.Button, interaction: disnake.Interaction):
            timers_creating_embed = disnake.Embed(
                colour=config['accent_def'],
                description=translator.translate('command_examples', 'timers_create', inst.language).format(config['prefix'])
            )
            timers_creating_embed.set_author(name=translator.translate('embed_title', 'timers', inst.language))
            await interaction.response.send_message(embed=timers_creating_embed)
        @disnake.ui.button(style=disnake.ButtonStyle.red, label=translator.translate('button', 'timers_delete', inst.language))
        async def delete_timer(self, button: disnake.ui.Button, interaction: disnake.Interaction):
            timers_creating_embed = disnake.Embed(
                colour=config['accent_def'],
                description=translator.translate('command_examples', 'timers_delete', inst.language).format(config['prefix'])
            )
            timers_creating_embed.set_author(name=translator.translate('embed_title', 'timers', inst.language))
            await interaction.response.send_message(embed=timers_creating_embed)
    await ctx.reply(embed=msg_embed, view=TimerByButtons(), mention_author=False)

async def sendRegularMsg(ctx, inst, config, disnake, translator, arg, db):
    msg_embed = await generateEmbed(ctx, inst, config, disnake, translator, arg, db)
    await ctx.reply(embed=msg_embed, mention_author=False)

