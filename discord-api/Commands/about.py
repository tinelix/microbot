# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License 2.0 & GNU Affero General Public License v3.0 and higher

import cpuinfo # for install 'pip install py-cpuinfo'
import psutil
import os
import sys
import platform
import sqlite3

name = 'about'
hidden = False

async def generateEmbed(ctx, inst, config, links, disnake, translator, python_version, version, uptime):
    msg_embed = disnake.Embed(
        description=translator.translate('embed_description', 'please_wait', inst.language),
        colour=config['accent_def'],
    )
    msg_embed.set_author(name=str(translator.translate('embed_title', 'about', inst.language)))
    return msg_embed

async def editEmbed(ctx, inst, config, links, disnake, translator, python_version, version, uptime):
    try:
        dev = inst.bot.get_user(config['dev_id'])
    except:
        dev = None

    plt_system = platform.system()
    plt_version = platform.version()

    if(plt_system == 'Windows'):
        if plt_version.startswith('10.0') and int(plt_version.split('.')[2]) >= 22000:
            os_ver = 'Windows 11 ({0})'.format(plt_version)
        elif plt_version.startswith('10.0') and int(plt_version.split('.')[2]) >= 10240:
            os_ver = 'Windows 10 ({0})'.format(plt_version)
        elif plt_version.startswith('6.3') and int(plt_version.split('.')[2]) >= 9600:
            os_ver = 'Windows 8.1 ({0})'.format(plt_version)
        elif plt_version.startswith('6.2') and int(plt_version.split('.')[2]) >= 9200:
            os_ver = 'Windows 8 ({0})'.format(plt_version)
        elif plt_version.startswith('6.1') and int(plt_version.split('.')[2]) >= 7601:
            os_ver = 'Windows 7 ({0})'.format(plt_version)
        elif plt_version.startswith('6.0') and int(plt_version.split('.')[2]) >= 6000:
            os_ver = 'Windows Vista ({0})'.format(plt_version)
        elif plt_version.startswith('5.2') and int(plt_version.split('.')[2]) >= 3790:
            os_ver = 'Windows XP x64 / Server 2003 ({0})'.format(plt_version)
        elif plt_version.startswith('5.1') and int(plt_version.split('.')[2]) >= 2600:
            os_ver = 'Windows XP ({0})'.format(plt_version)
        else:
            os_ver = 'Windows ({0})'.format(plt_version)
    else:
        os_ver = '{0} {1}'.format(platform.system(), platform.release())

    if psutil.virtual_memory().available < 1024 or psutil.virtual_memory().total < 1024:
        ram = translator.translate('numb_with_unit', 'kilobytes2', inst.language).format(round(psutil.virtual_memory().used / 1024, 2), round(psutil.virtual_memory().total / 1024, 2))
    elif (psutil.virtual_memory().available < 1048576 and psutil.virtual_memory().available >= 1024) or (psutil.virtual_memory().total < 1048576 and psutil.virtual_memory().total >= 1024):
        ram = translator.translate('numb_with_unit', 'megabytes2', inst.language).format(round(psutil.virtual_memory().used / 1024 / 1024, 2), round(psutil.virtual_memory().total / 1024 / 1024, 2))
    else:
        ram = translator.translate('numb_with_unit', 'gigabytes2', inst.language).format(round(psutil.virtual_memory().used / 1024 / 1024 / 1024, 2), round(psutil.virtual_memory().total / 1024 / 1024 / 1024, 2))

    msg_embed = disnake.Embed(
        colour=config['accent_def']
    )
    msg_embed.set_author(name=str(translator.translate('embed_title', 'about', inst.language)))
    license = ''
    if(config['license'] == 1):
        license = 'AGPLv3+ & Apache 2.0 Edition'
    elif(config['license'] == 2):
        license = 'AGPLv3+ Edition'
    else:
        license = 'Apache 2.0 Edition'
    if(config['name'] == 'Microbot'):
        msg_embed.add_field(
            translator.translate('embed_fields', 'about_versf', inst.language), translator.translate('embed_fields', 'about_versv', inst.language).format(version['version'], version['version_date']) + "\r\n_" + license + "_", inline=True
        )
    else:
       msg_embed.add_field(
            translator.translate('embed_fields', 'about_versf2', inst.language).format(version['original_name']), translator.translate('embed_fields', 'about_versv', inst.language).format(version['version'], version['version_date']) + "\r\n_" + license + "_", inline=True
       )
    if(dev == None):
        pass
    else:
        msg_embed.add_field(
            translator.translate('embed_fields', 'about_devsf', inst.language), translator.translate('embed_fields', 'about_devsv', inst.language).format(dev.global_name, dev.name), inline=True
        )
    msg_embed.add_field(
        translator.translate('embed_fields', 'about_regdf', inst.language), translator.translate('embed_fields', 'about_regdv', inst.language).format(translator.formatDate(inst.bot.user.created_at.astimezone(inst.tz), 'normal', inst.language)), inline=True
    )
    msg_embed.add_field(
        translator.translate('embed_fields', 'about_statsf', inst.language), translator.translate('embed_fields', 'about_statsv', inst.language).format(len(inst.bot.guilds), len(inst.bot.users)), inline=True
    )
    msg_embed.add_field(
        translator.translate('embed_fields', 'about_uptimef', inst.language), translator.translate('embed_fields', 'about_uptimev', inst.language).format(uptime), inline=True
    )
    msg_embed.add_field(
        translator.translate('embed_fields', 'about_basedf', inst.language), translator.translate('embed_fields', 'about_basedv', inst.language).format(python_version(), disnake.__version__, sqlite3.sqlite_version), inline=True
    )
    try:
        msg_embed.add_field(
            translator.translate('embed_fields', 'about_hardwf', inst.language), translator.translate('embed_fields', 'about_hardwv', inst.language).format(cpuinfo.get_cpu_info()['brand_raw'], round(cpuinfo.get_cpu_info()['hz_advertised'][0] / 1000000, 2), ram, os_ver), inline=False
        )
    except:
        msg_embed.add_field(
            translator.translate('embed_fields', 'about_hardwf', inst.language), translator.translate('embed_fields', 'about_hardwv', inst.language).format(cpuinfo.get_cpu_info()['brand_raw'], "?", ram, os_ver), inline=False
        )

    links_str = ''

    if(len(links['invite']) > 0):
        links_str += "{0}\r\n".format(translator.translate('embed_fields', 'about_linksv', inst.language).format(links['invite']))
    if(len(links['website']) > 0):
        links_str += "{0}\r\n".format(translator.translate('embed_fields', 'about_linksv2', inst.language).format(links['website']))
    if(len(links['repo']) > 0):
        links_str += "{0}\r\n".format(translator.translate('embed_fields', 'about_linksv3', inst.language).format(links['repo']))
        msg_embed.add_field(
            translator.translate('embed_fields', 'about_licensesf', inst.language), translator.translate('embed_fields', 'about_licensesv', inst.language), inline=False
        )
    if(len(links['support']) > 0):
        links_str += "{0}\r\n".format(translator.translate('embed_fields', 'about_linksv4', inst.language).format(links['support']))
    if(len(links['donate']) > 0):
        links_str += "{0}\r\n".format(translator.translate('embed_fields', 'about_linksv5', inst.language).format(links['donate']))
    if(len(links_str) > 0):
        msg_embed.add_field(
            translator.translate('embed_fields', 'about_linksf', inst.language), links_str, inline=True
        )


    msg_embed.set_footer(text='Copyright © 2023 Dmitry Tretyakov (aka. Tinelix)')
    return msg_embed

async def sendSlashMsg(ctx, inst, config, links, version, disnake, translator, python_version, uptime):
    await ctx.response.defer()
    msg_embed = await editEmbed(ctx, inst, config, links, disnake, translator, python_version, version)
    await ctx.send(embed=msg_embed)

async def sendRegularMsg(ctx, inst, config, links, disnake, translator, python_version, version, uptime):
    msg_embed = await generateEmbed(ctx, inst, config, links, disnake, translator, python_version, version, uptime)
    msg = await ctx.reply(embed=msg_embed, mention_author=False)
    msg_embed_2 = await editEmbed(ctx, inst, config, links, disnake, translator, python_version, version, uptime)
    await msg.edit(embed=msg_embed_2)
