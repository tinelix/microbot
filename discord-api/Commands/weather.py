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
import requests

name = 'settings'
hidden = False

cities_list = []

async def generateEmbed(ctx, inst, config, tokens, disnake, translator, arg):
    if(len(tokens['owm_api']) == 0):
        return print(" ERROR: OpenWeatherMap API token not found.")
    data = requests.get("http://api.openweathermap.org/data/2.5/find",
                 params={'q': arg, 'type': 'like', 'units': 'metric', 'APPID': tokens['owm_api']})
    search_result = data.json()
    cities = ""
    for city in search_result['list']:
        if(search_result['list'].index(city) < 10):
            cities += "{0: 2d}. {1}, {2}\r\n".format(search_result['list'].index(city) + 1, city['name'], city['sys']['country'])
            cities_list.append(disnake.SelectOption(label="{0: 2d}. {1}, {2}".format(search_result['list'].index(city) + 1, city['name'], city['sys']['country']), value=city['id']))
    if(len(cities_list) > 0):
        msg_embed = disnake.Embed(
            colour=config['accent_def'],
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'weather', inst.language)))
        msg_embed.add_field(translator.translate('embed_fields', 'weather_resultf', inst.language).format(len(cities_list)), translator.translate('embed_fields', 'weather_resultv', inst.language).format(cities))
    else:
        msg_embed = disnake.Embed(
            colour=config['accent_err'],
            description=translator.translate('embed_description', 'query_notfound', inst.language)
        )
        msg_embed.set_author(name=str(translator.translate('embed_title', 'error', inst.language)))
    return msg_embed

def getConditionsDescription(code, translator, language):
    conditions = ""
    if(code == 200):
        conditions = translator.translate('embed_description', 'weather_conditions_200', inst.language)
    elif(code == 201):
        conditions = translator.translate('embed_description', 'weather_conditions_201', inst.language)
    elif(code == 202):
        conditions = translator.translate('embed_description', 'weather_conditions_202', inst.language)
    elif(code >= 300 and code <= 321):
        conditions = translator.translate('embed_description', 'weather_conditions_300-321', inst.language)
    elif(code >= 500 and code <= 501):
        conditions = translator.translate('embed_description', 'weather_conditions_500-501', inst.language)
    elif(code == 502):
        conditions = translator.translate('embed_description', 'weather_conditions_502', inst.language)
    elif(code >= 503 and code <= 504):
        conditions = translator.translate('embed_description', 'weather_conditions_503-504', inst.language)
    elif(code == 511):
        conditions = translator.translate('embed_description', 'weather_conditions_511', inst.language)
    elif(code >= 600 and code <= 601):
        conditions = translator.translate('embed_description', 'weather_conditions_600-601', inst.language)
    elif(code == 602):
        conditions = translator.translate('embed_description', 'weather_conditions_602', inst.language)
    elif(code >= 615 and code <= 616):
        conditions = translator.translate('embed_description', 'weather_conditions_615-616', inst.language)
    elif(code == 800):
        conditions = translator.translate('embed_description', 'weather_conditions_800', inst.language)
    elif(code == 801):
        conditions = translator.translate('embed_description', 'weather_conditions_801', inst.language)
    elif(code >= 802 and code <= 803):
        conditions = translator.translate('embed_description', 'weather_conditions_802-803', inst.language)
    elif(code == 804):
        conditions = translator.translate('embed_description', 'weather_conditions_804', inst.language)

    return conditions

def getConditionsShortDescription(code, translator, language):
    conditions = ""
    if(code == 200):
        conditions = translator.translate('embed_description', 'weather_sconditions_200', inst.language)
    elif(code == 201):
        conditions = translator.translate('embed_description', 'weather_sconditions_201', inst.language)
    elif(code == 202):
        conditions = translator.translate('embed_description', 'weather_sconditions_202', inst.language)
    elif(code >= 300 and code <= 321):
        conditions = translator.translate('embed_description', 'weather_sconditions_300-321', inst.language)
    elif(code >= 500 and code <= 501):
        conditions = translator.translate('embed_description', 'weather_sconditions_500-501', inst.language)
    elif(code == 502):
        conditions = translator.translate('embed_description', 'weather_sconditions_502', inst.language)
    elif(code >= 503 and code <= 504):
        conditions = translator.translate('embed_description', 'weather_sconditions_503-504', inst.language)
    elif(code == 511):
        conditions = translator.translate('embed_description', 'weather_sconditions_511', inst.language)
    elif(code >= 600 and code <= 601):
        conditions = translator.translate('embed_description', 'weather_sconditions_600-601', inst.language)
    elif(code == 602):
        conditions = translator.translate('embed_description', 'weather_sconditions_602', inst.language)
    elif(code >= 615 and code <= 616):
        conditions = translator.translate('embed_description', 'weather_sconditions_615-616', inst.language)
    elif(code == 800):
        conditions = translator.translate('embed_description', 'weather_sconditions_800', inst.language)
    elif(code == 801):
        conditions = translator.translate('embed_description', 'weather_sconditions_801', inst.language)
    elif(code >= 802 and code <= 803):
        conditions = translator.translate('embed_description', 'weather_sconditions_802-803', inst.language)
    elif(code == 804):
        conditions = translator.translate('embed_description', 'weather_sconditions_804', inst.language)

    return conditions
def formatTemperature(temp):
    if(round(temp, 1) > 0.0):
        ftemp = "+{0}".format(round(temp, 1))
    elif(round(weather['main']['temp'], 1) == 0.0):
        ftemp = "±{0}".format(round(temp, 1))
    else:
        ftemp = "-{0}".format(round(temp, 1))

    return ftemp

async def generateWeatherEmbed(ctx, inst, config, tokens, disnake, translator, city_id):
    if(len(tokens['owm_api']) == 0):
        return print(" ERROR: OpenWeatherMap API token not found.")
    if(inst.language == "ru_RU"):
        data = requests.get("http://api.openweathermap.org/data/2.5/weather",
                        params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': tokens['owm_api']})
        forecast_data = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                        params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': tokens['owm_api']})
    else:
        data = requests.get("http://api.openweathermap.org/data/2.5/weather",
                        params={'id': city_id, 'units': 'metric', 'lang': 'en', 'APPID': tokens['owm_api']})
        forecast_data = requests.get("http://api.openweathermap.org/data/2.5/forecast",
                        params={'id': city_id, 'units': 'metric', 'lang': 'en', 'APPID': tokens['owm_api']})

    weather = data.json()
    forecast = forecast_data.json()

    current_conditions = getConditionsDescription(weather['weather'][0]['id'], translator, language)

    msg_embed = disnake.Embed(
        colour=config['accent_def'],
        description=current_conditions
    )

    current_temp = formatTemperature(weather['main']['temp'])
    current_min_temp = formatTemperature(weather['main']['temp_min'])
    current_max_temp = formatTemperature(weather['main']['temp_max'])

    day7_forecast = ""

    for day in forecast['list']:
        if(forecast['list'].index(day) < 7):
            conditions = getConditionsShortDescription(day['weather'][0]['id'], translator, inst.language)
            temp = formatTemperature(day['main']['temp'])
            min_temp = formatTemperature(day['main']['temp_min'])
            max_temp = formatTemperature(day['main']['temp_max'])
            day7_forecast += "{0} | {1}°C\r\n{2}\r\n".format(day['dt_txt'], temp, conditions)

    msg_embed.set_author(name=str(translator.translate('embed_title', 'weather2', language)).format(weather['name'], weather['sys']['country']))
    msg_embed.add_field(translator.translate('embed_fields', 'weather_tempf', inst.language), translator.translate('embed_fields', 'weather_tempv', inst.language).format(current_temp, current_min_temp, current_max_temp), inline=False)
    msg_embed.add_field(translator.translate('embed_fields', 'weather_pressuref', inst.language), translator.translate('embed_fields', 'weather_pressurev', inst.language).format(round(weather['main']['pressure'] * 0.75006)))
    msg_embed.add_field(translator.translate('embed_fields', 'weather_humidityf', inst.language), translator.translate('embed_fields', 'weather_humidityv', inst.language).format(weather['main']['humidity']))
    msg_embed.add_field(translator.translate('embed_fields', 'weather_windspeedf', inst.language), translator.translate('embed_fields', 'weather_windspeedv', inst.language).format(round(weather['wind']['speed'], 1)))
    msg_embed.add_field(translator.translate('embed_fields', 'weather_upforecastsf', inst.language), translator.translate('embed_fields', 'weather_upforecastsv', inst.language).format(day7_forecast), inline=False)
    return msg_embed

async def sendSlashMsg(ctx, inst, config, tokens, disnake, translator, arg):
    msg_embed = await generateEmbed(ctx, inst, config, tokens, disnake, translator, arg)
    if(len(cities_list) > 0):
        select = disnake.ui.Select(
                    placeholder=translator.translate('embed_fields', 'weather_selyc', inst.language),
                    options=cities_list,
                )
        async def response(interaction):
            id = int(re.search(r'\d+', select.values[0]).group())
            if(id > 0):
                msg_embed = await generateWeatherEmbed(ctx, bot, config, tokens, inst.language, disnake, translator, id)
                await interaction.send(embed=msg_embed)

        select.callback = response

        view = disnake.ui.View()
        view.add_item(select)
        await ctx.response.send_message(embed=msg_embed, view=view)
        cities_list.clear()
    else:
        await ctx.response.send_message(embed=msg_embed)

async def sendRegularMsg(ctx, inst, config, tokens, disnake, translator, arg):
    msg_embed = await generateEmbed(ctx, inst, config, tokens, disnake, translator, arg)
    if(len(cities_list) > 0):
        select = disnake.ui.Select(
                    placeholder=translator.translate('embed_fields', 'weather_selyc', inst.language),
                    options=cities_list,
                )
        async def response(interaction):
            id = int(re.search(r'\d+', select.values[0]).group())
            if(id > 0):
                msg_embed = await generateWeatherEmbed(ctx, inst, config, tokens, disnake, translator, id)
                await interaction.send(embed=msg_embed)

        select.callback = response

        view = disnake.ui.View()
        view.add_item(select)
        await ctx.reply(embed=msg_embed, view=view, mention_author=False)
        cities_list.clear()
    else:
        await ctx.reply(embed=msg_embed, mention_author=False)

async def sendHelpMsg(ctx, bot, config, language, disnake, translator):
    msg_embed = disnake.Embed(
        title=str(translator.translate('embed_title', 'cmd_help', inst.language)).format('weather'),
        description=str(translator.translate('command_description', 'weather', inst.language)),
        colour=config['accent_def'],
    )
    msg_embed.add_field(translator.translate('embed_fields', 'help_exampf', inst.language), translator.translate('command_examples', 'weather', inst.language).format(config['prefix']), inline=False)
    await ctx.reply(embed=msg_embed, mention_author=False)
