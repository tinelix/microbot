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

def translate(where, str, language):
    try:
        if language == "ru_RU": # Russian
            if where == "embed_title":
                locale = {
                    'error': '❎ Ошибка',
                    'help': '❔ Справка',
                    'cmd_help': 'Команда `{0}`',
                    'bug_reporter': '🪲 Баг обнаружен!',
                    'about': '🤖 О боте',
                    'user': '👤 {0}',
                    'user_bot': '🤖 {0}',
                    'user_owner': '👑 {0}',
                    'avatar': '🖼 Аватар пользователя {0}',
                    'forbidden': '🚫 Доступ запрещен',
                    'eval': '⌨ Интерпретатор',
                    '8ball': '🎱 Генератор случайных ответов',
                    'rngen': '🎱 Генератор случайных чисел',
                    'calc': '🔢 Калькулятор',
                    'settings': '⚙ Настройки',
                    'msg_author': '📣 Публикация от {0}',
                    'ping': '🏓 Понг!',
                    'weather': '⛅ Погода',
                    'weather2': '⛅ {0}, {1}',
                    'wikipedia': '🌐 Википедия',
                    'codec': '🔡 Кодек'
                }
            elif where == "embed_description":
                locale = {
                    'help': '{0} - простейший и компактный бот для Revolt.\r\n[Пригласить]({1})',
                    'error_unf': '😔 Пользователь не найден. Попробуйте найти другого пользователя.',
                    'bug_reporter': '🪲 Да, у нас и такое случается. Но ничего страшного, сейчас отправим разработчикам на исправление этого бага.',
                    'forbidden': '🚫 Вы не имеете права пользоваться этой командой!',
                    'please_wait': '⌛ Подождите...',
                    'settings': '**Настройки сервера:** 🇷🇺',
                    'settings_done': '✅ Готово!',
                    'publish_isntcomm': '❌ Сервер не обладает функциями сообщества. Включите в настройках сервера.',
                    'publish_isntnewsch': '❌ Канал не является новостным каналом или каналом с объявлениями. Включите в настройках канала.',
                    'weather_conditions_200': '**⛈ Гроза с умеренным дождем**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
                    'weather_conditions_201': '**⛈ Гроза с дождем**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
                    'weather_conditions_202': '**⛈ Гроза с ливнем**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
                    'weather_conditions_300-321': '**🌨 Гололедица**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
                    'weather_conditions_500-501': '**🌧 Умеренный дождь**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
                    'weather_conditions_502': '**🌧 Дождь**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/) на_',
                    'weather_conditions_503-504': '**🌧 Ливень**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
                    'weather_conditions_511': '**🌧 Дождь**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
                    'weather_conditions_600-601': '**🌨 Снег**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
                    'weather_conditions_602': '**🌨 Метель**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
                    'weather_conditions_615-616': '**🌨 Дождь со снегом**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
                    'weather_conditions_800': '**☀ Солнечно**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
                    'weather_conditions_801': '**🌤 Малооблачно**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
                    'weather_conditions_802-803': '**⛅ Облачно**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
                    'weather_conditions_804': '**☁ Пасмурно**\r\n_по данным сервиса [OpenWeatherMap](https://openweathermap.org/)_',
                    'weather_sconditions_200': '⛈ Гроза с умеренным дождем',
                    'weather_sconditions_201': '⛈ Гроза с дождем',
                    'weather_sconditions_202': '⛈ Гроза с ливнем',
                    'weather_sconditions_300-321': '🌨 Гололедица',
                    'weather_sconditions_500-501': '🌧 Умеренный дождь',
                    'weather_sconditions_502': '🌧 Дождь',
                    'weather_sconditions_503-504': '🌧 Ливень',
                    'weather_sconditions_511': '🌧 Дождь',
                    'weather_sconditions_600-601': '🌨 Снег',
                    'weather_sconditions_602': '🌨 Метель',
                    'weather_sconditions_615-616': '🌨 Дождь со снегом',
                    'weather_sconditions_800': '☀ Солнечно',
                    'weather_sconditions_801': '🌤 Малооблачно',
                    'weather_sconditions_802-803': '⛅ Облачно',
                    'weather_sconditions_804': '☁ Пасмурно',
                    'query_notfound': '😔 К сожалению, мы ничего не нашли. Может, попробуете другой запрос?',
                    'wikipedia': '{0}\r\n[Подробнее...]({1})'
                }
            elif where == "embed_fields":
                locale = {
                    'help_preff': 'Префиксы',
                    'help_prefv': '`>` или `/`',
                    'help_cmdsf': 'Команды',
                    'help_cmdsv': '{0}',
                    'help_exampf': 'Пример',
                    'help_aliasf': 'Аналогичные названия',
                    'eval_codelf': 'Листинг',
                    'eval_resulf': 'Результат',
                    'about_versf': 'Версия',
                    'about_versv': '{0} ({1})',
                    'about_devsf': 'Разработчик',
                    'about_devsv': '`{0}`',
                    'about_regdf': 'Дата регистрации',
                    'about_regdv': '{0}',
                    'about_statsf': 'Статистика',
                    'about_statsv': '{0} серверов\r\n{1} пользователей',
                    'about_uptimef': 'Активен',
                    'about_uptimev': '{0}',
                    'about_basedf': 'Работает на базе',
                    'about_basedv': 'Python {0}\r\nVoltage {1}\r\nSQLite {2}',
                    'about_hardwf': 'Оборудование',
                    'about_hardwv': '**ЦП:** {0} ({1} МГц)\r\n**ОЗУ:** {2}\r\n**Платформа:** {3}',
                    'about_linksf': 'Ссылки',
                    'about_linksv': '[Пригласить]({0})',
                    'about_linksv2': '[Сайт]({0})',
                    'about_linksv3': '[Репозиторий]({0}) (Apache License 2.0 & AGPL 3.0+)',
                    'about_linksv4': '[Сервер поддержки]({0})',
                    'about_linksv5': '[Сайт]({0})',
                    'user_nickf': 'Псевдоним',
                    'user_nickv': '{0}',
                    'user_nickvn': '*Отсутствует*',
                    'user_regdf': 'Дата регистрации',
                    'user_regdv': '{0}',
                    'user_joinf': 'Дата входа на сервер',
                    'user_joinv': '{0}',
                    'user_statusf': 'Статус',
                    'user_statusv': 'Онлайн',
                    'user_statusv2': 'Отошел',
                    'user_statusv3': 'Не беспокоить',
                    'user_statusv4': 'Оффлайн',
                    'user_rolesf': 'Роли ({0})',
                    'user_rolesv': '{0}',
                    'guild_ownerf': 'Владелец',
                    'guild_ownerv': '`{0}`',
                    'guild_crtf': 'Дата создания',
                    'guild_crtv': '{0}',
                    'guild_blvlf': 'Уровень бустов',
                    'guild_blvlv': 'Уровень {0}',
                    'guild_mlvlf': 'Степень модерации',
                    'guild_mlvlv': 'Без ограничений',
                    'guild_mlvlv2': 'Только подтвержденный e-mail',
                    'guild_mlvlv3': 'Регистрация более 5 минут',
                    'guild_mlvlv4': 'Присутствие более 10 минут',
                    'guild_mlvlv5': 'Только подтвержденный телефон',
                    'guild_statsf': 'Статистика',
                    'guild_statsv': 'Всего {0} участников\r\n{1} человек ({2}%)\r\n{3} ботов ({4}%)\r\n{5} онлайн ({6}%)\r\n{7} каналов',
                    '8ball_answf': 'Ответ',
                    '8ball_answv': ['Да.', 'Нет.', 'Возможно.', 'Может быть.', 'Время покажет.', 'Поживем - увидим.', 'Навряд ли.', 'Конечно.', 'Да-да.', 'Неа.', 'Так и есть.', 'Понятия не имею.', 'Я не знаю.', 'Я хз.', 'Без понятия.', 'Наверное, да...', 'Наверное, нет...', 'Да фиг знает!', 'Я не понял ваш вопрос, можете повторить?', 'Попробуйте задать другой вопрос. Может быть, я что-то не понимаю?', 'Вероятно.', 'Ничего подобного.'],
                    'rngen_numbf': 'Число',
                    'rngen_numbv': '{0}',
                    'calc_resulf': 'Результат',
                    'calc_rlerrv': 'ОШИБКА: Попытка деления на ноль',
                    'calc_rlerrv2': 'ОШИБКА: Слишком большое число',
                    'calc_rlerrv3': 'ОШИБКА: Принимаются только числа',
                    'calc_rlerrv4': 'ОШИБКА: {0}',
                    'calc_asignf': 'Доступные знаки',
                    'calc_asignv': '[`+`] - сложение\r\n[`-`] - удаление\r\n[`/`], [`:`] - деление\r\n[`*`] - умножение',
                    'settings_availoptf': 'Доступные параметры',
                    'settings_availoptv': '🚩 Язык (Language)',
                    'ping_statisticsf': 'Статистика',
                    'ping_statisticsv': '**Задержка:** {0} мсек',
                    'ping_statisticsv2': '**Задержка:** {0} мсек\r\n**Время выполнения:** {1} мсек',
                    'weather_resultf': 'Результаты поиска ({0})',
                    'weather_resultv': '```{0}```',
                    'weather_tempf': 'Температура воздуха',
                    'weather_tempv': '**{0}°C**\r\nмин. {1}°C\r\nмакс. {2}°C',
                    'weather_pressuref': 'Давление',
                    'weather_pressurev': '{0} мм. рт. ст.',
                    'weather_humidityf': 'Влажность',
                    'weather_humidityv': '{0}%',
                    'weather_windspeedf': 'Скорость ветра',
                    'weather_windspeedv': '{0} м/сек',
                    'weather_selyc': 'Выберите город или населенный пункт',
                    'weather_upforecastsf': 'Ближайшие прогнозы',
                    'weather_upforecastsv': '```{0}```',
                    'codec_resulf': 'Результат',
                    'codec_resulv': '```{0}```',
                    'codec_algf': 'Алгоритм',
                    'codec_algv': '{0}',
                    'codec_algv2': 'Двоичный код',
                    'codec_derrv': 'Ошибка декодирования',
                    'codec_eerrv': 'Ошибка кодирования',
                }
            elif where == "embed_footer":
                locale = {
                    '8ball': 'Все совпадения случайны!'
                }
            elif where == "command_description":
                locale = {
                    'help': 'Показывает справочную информацию, включая список доступных команд.',
                    'about': 'Показывает описание бота, а также служебную информацию.',
                    'user': 'Показывает информацию о пользователе.',
                    'avatar': 'Показывает аватарки пользователя.',
                    '8ball': 'Генерирует для любого вопроса случайный ответ. Все совпадения случайны!',
                    'rngen': 'Генерирует случайное число в указанном диапазоне.',
                    'guild': 'Показывает информацию о гильдии (сервере)',
                    'calc': 'Простейший калькулятор.',
                    'settings': 'Настройки бота.',
                    'settings_lang': 'Смена языка.',
                    'publish': 'Публикует сообщения с новостного канала без лишнего клика по кнопке мыши.',
                    'ping': 'Пни меня.',
                    'weather': 'Отображает прогноз погоды на ближайшие 24 часа. Для этого используется сервис [OpenWeatherMap](https://openweathermap.org).',
                    'wiki': 'Показывает статью в Википедии в краткой форме.',
                    'codec': 'Расшифровка и зашифровка текста'
                }
            elif where == "command_examples":
                locale = {
                    'help': '```{0}help```',
                    'about': '```{0}about```',
                    'user': '```{0}user [@упоминание или ID участника]```',
                    'avatar': '```{0}avatar [@упоминание или ID участника]```',
                    '8ball': '```{0}8ball [вопрос]```',
                    'rngen': '```{0}rngen [начало диапазона]-[конец диапазона]```',
                    'guild': '```{0}guild```',
                    'settings': '```{0}settings [-L] [значение]\r\n{0}settings -L ru_RU```',
                    'settings_lang': '```{0}settings -L [en_US / ru_RU]\r\n{0}settings -L ru_RU```',
                    'publish': '```{0}publish Вот так выглядит публикация!```',
                    'ping': '```{0}ping```',
                    'weather': '```{0}weather Париж\r\n{0}weather Лондон\r\n{0}weather Санкт-Петербург\r\n{0}weather Барнаул```',
                    'wiki': '```{0}wiki Синус\r\n{0}wiki Android\r\n{0}wiki Кунсткамера\r\n{0}wiki Прокси-сервер\r\n{0}wiki Эмодзи```',
                    'codec': '```{0}codec -e base64 Base64 text encoding.\r\n{0}codec -e binary Это перевод текста в двоичный код.\r\n{0}codec -d base64 QmFzZTY0IHRleHQgZGVjb2RpbmcgZXhhbXBsZS4=```',
                    'calc': '```{0}calc [выражение]```',
                }
            elif where == "button":
                locale = {
                    'user_avatar': 'Показать аватар',
                    'rngen_retry': 'Повторить',
                }
            elif where == "numb_with_unit":
                locale = {
                    'bytes': '{0} байт',
                    'bytes2': '{0} / {1} байт',
                    'kilobytes': '{0} кБ',
                    'kilobytes2': '{0} / {1} кБ',
                    'megabytes': '{0} МБ',
                    'megabytes2': '{0} / {1} МБ',
                    'gigabytes': '{0} ГБ',
                    'gigabytes2': '{0} / {1} ГБ',
                }
            else:
                locale = {
                }
            if len(locale) == 0: # if string not found (variant #1)
                return "[{0}|{1}] Строка не найдена".format(str, where)
            else:
                return locale[str]
        else: # English, if not
            if where == "embed_title":
                locale = {
                    'error': '❎ Error',
                    'help': '❔ Help',
                    'cmd_help': '`{0}` command',
                    'about': '❔ About',
                    'user': '👤 {0}',
                    'user_bot': '🤖 {0}',
                    'user_owner': '👑 {0}',
                    'avatar': '🖼 {0}\'s avatar',
                    'bug_reporter': '🪲 Bug detected!',
                    'forbidden': '🚫 Access forbidden',
                    'eval': '⌨ Interpreter',
                    '8ball': '🎱 Random Answer Generator',
                    'rngen': '🎱 Random Number Generator',
                    'calc': '🔢 Calculator',
                    'settings': '⚙ Settings',
                    'msg_author': '📣 Post by {0}',
                    'ping': '🏓 Pong!',
                    'weather': '⛅ Weather',
                    'weather2': '⛅ {0}, {1}',
                    'wikipedia': '🌐 Wikipedia',
                    'codec': '🔡 Codec',
                }
            elif where == "embed_description":
                locale = {
                    'help': '{0} - is a simple and compact bot for Revolt.\r\n[Invite]({1})',
                    'error_unf': '😔 User not found. Try to find another user.',
                    'bug_reporter': '🪲 Yep, this happens to us too. But it\'s okay, now we\'ll send it to the developers to fix this bug.',
                    'forbidden': '🚫 You do not have the right to use this command!',
                    'please_wait': '⌛ Wait...',
                    'settings': '**Server settings:** 🇺🇸',
                    'settings_done': '✅ Done!',
                    'weather_conditions_200': '**⛈ Thunderstorm with moderate rain**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_conditions_201': '**⛈ Thunderstorm with rain**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_conditions_202': '**⛈ Thunderstorm with heavy rain**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_conditions_300-321': '**🌧 Rain**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_conditions_500-501': '**🌧 Moderate rain**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_conditions_502': '**🌧 Rain**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_conditions_503-504': '**🌧 Shower rain**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_conditions_511': '**🌧 Rain**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_conditions_600-601': '**🌨 Show**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_conditions_602': '**🌨 Snowstorm**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_conditions_615-616': '**🌨 Rain with snow**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_conditions_800': '**☀ Sunny**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_conditions_801': '**🌤 Partly cloudy**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_conditions_802-803': '**⛅ Cloudy**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_conditions_804': '**☁ Mainly cloudy**\r\n_data provided by [OpenWeatherMap](https://openweathermap.org/)_ service',
                    'weather_sconditions_200': '⛈ Thunderstorm with moderate rain',
                    'weather_sconditions_201': '⛈ Thunderstorm with rain',
                    'weather_sconditions_202': '⛈ Thunderstorm with heavy rain',
                    'weather_sconditions_300-321': '🌧 Rain',
                    'weather_sconditions_500-501': '🌧 Moderate rain',
                    'weather_sconditions_502': '🌧 Rain',
                    'weather_sconditions_503-504': '🌧 Shower rain',
                    'weather_sconditions_511': '🌧 Rain',
                    'weather_sconditions_600-601': '🌨 Show',
                    'weather_sconditions_602': '🌨 Snowstorm',
                    'weather_sconditions_615-616': '**🌨 Rain with snow',
                    'weather_sconditions_800': '☀ Sunny',
                    'weather_sconditions_801': '🌤 Partly cloudy',
                    'weather_sconditions_802-803': '⛅ Cloudy',
                    'weather_sconditions_804': '☁ Mainly cloudy',
                    'query_notfound': '😔 Sorry, we didn\'t find anything. Maybe try another query?',
                    'wikipedia': '{0}\r\n[More...]({1})'
                }
            elif where == "embed_fields":
                locale = {
                    'help_preff': 'Prefixes',
                    'help_prefv': '`>` or `/`',
                    'help_cmdsf': 'Commands',
                    'help_cmdsv': '{0}',
                    'help_exampf': 'Examples',
                    'help_aliasf': 'Aliases',
                    'eval_codelf': 'Code listing',
                    'eval_resulf': 'Result',
                    'about_versf': 'Version',
                    'about_versv': '{0} ({1})',
                    'about_devsf': 'Developer',
                    'about_devsv': '{0}',
                    'about_regdf': 'Registration date',
                    'about_regdv': '{0}',
                    'about_statsf': 'Statistics',
                    'about_statsv': '{0} servers\r\n{0} users',
                    'about_uptimef': 'Uptime',
                    'about_uptimev': '{0}',
                    'about_basedf': 'Powered by',
                    'about_basedv': 'Python {0}\r\nDisnake {1}\r\nSQLite {2}',
                    'about_hardwf': 'Hardware',
                    'about_hardwv': '**CPU:** {0} ({1} MHz)\r\n**RAM:** {2}\r\n**Platform:** {3}',
                    'about_linksf': 'Links',
                    'about_linksv': '[Invite]({0})',
                    'about_linksv2': '[Website]({0})',
                    'about_linksv3': '[Source code]({0}) (Apache License 2.0 & AGPL 3.0+)',
                    'about_linksv4': '[Support server]({0})',
                    'about_linksv': '{0}',
                    'user_nickf': 'Nickname',
                    'user_nickv': '{0}',
                    'user_nickvn': '*Missing*',
                    'user_regdf': 'Registration date',
                    'user_regdv': '{0}',
                    'user_joinf': 'Server join date',
                    'user_joinv': '{0}',
                    'user_statusf': 'Status',
                    'user_statusv': 'Online',
                    'user_statusv2': 'Idle',
                    'user_statusv3': 'DND',
                    'user_statusv4': 'Offline',
                    'user_rolesf': 'Roles ({0})',
                    'user_rolesv': '{0}',
                    'guild_ownerf': 'Owner',
                    'guild_ownerv': '{0}',
                    'guild_crtf': 'Date of creation',
                    'guild_crtv': '{0}',
                    'guild_mlvlf': 'Moderation degree',
                    'guild_mlvlv': 'Without limits',
                    'guild_mlvlv2': 'Only confirmed e-mail',
                    'guild_mlvlv3': 'Registration over 5 minutes',
                    'guild_mlvlv4': 'Presence over 10 minutes',
                    'guild_mlvlv5': 'Only confirmed phone',
                    'guild_blvlf': 'Boost level',
                    'guild_blvlv': 'Level {0}',
                    'guild_statsv': '{0} members total\r\n{1} people ({2}%)\r\n{3} bots ({4}%)\r\n{5} online ({6}%)\r\n{7} channels',
                    'guild_statsf': 'Statistics',
                    '8ball_answf': 'Answer',
                    '8ball_answv': ['Yes.', 'No.', 'Maybe.', 'Time will tell.', 'Wait and see.', 'Unlikely.', 'Of course.', 'Yep.', 'Nope.', 'And there is.', 'I have no idea.', 'I don\'t know', 'No idea.', 'Maybe yes...', 'Maybe no...', 'Who knows!', 'I didn\'t understand your question, can you repeat?', 'Try asking a different question. Maybe I don\'t understand something?', 'Probably.', 'Nothing like this.'],
                    'rngen_numbf': 'Number',
                    'rngen_numbv': '{0}',
                    'calc_resulf': 'Result',
                    'calc_rlerrv': 'ERROR: Attempt to divide by zero',
                    'calc_rlerrv2': 'ERROR: Number too large',
                    'calc_rlerrv3': 'ERROR: Only numbers are accepted',
                    'calc_rlerrv4': 'ERROR: {0}',
                    'calc_asignf': 'Available signs',
                    'calc_asignv': '[`+`] - addition\r\n[`-`] - deletion\r\n[`/`], [`:`] - division\r\n[`*`] - multiplication',
                    'settings_availoptf': 'Available options',
                    'settings_availoptv': '🚩 Язык (Language)',
                    'ping_statisticsf': 'Statistics',
                    'ping_statisticsv': '**Latency:** {0} msec',
                    'ping_statisticsv2': '**Latency:** {0} msec\r\n**Execution time:** {1} msec',
                    'weather_resultf': 'Search results ({0})',
                    'weather_resultv': '```{0}```',
                    'weather_tempf': 'Air temperature',
                    'weather_tempv': '**{0}°C**\r\nmin. {1}°C\r\nmax. {2}°C',
                    'weather_pressuref': 'Pressure',
                    'weather_pressurev': '{0} mmHg',
                    'weather_humidityf': 'Humidity',
                    'weather_humidityv': '{0}%',
                    'weather_windspeedf': 'Wind speed',
                    'weather_windspeedv': '{0} m/sec',
                    'weather_selyc': 'Select city or locality',
                    'weather_upforecastsf': 'Upcoming forecasts',
                    'weather_upforecastsv': '```{0}```',
                    'codec_resulf': 'Result',
                    'codec_resulv': '```{0}```',
                    'codec_algf': 'Algorithm',
                    'codec_algv': '{0}',
                    'codec_algv2': 'Binary code',
                }
            elif where == "command_description":
                locale = {
                    'help': 'Shows help information including a list of available commands.',
                    'about': 'Shows a description of the bot, as well as service information.',
                    'user': 'Shows user info.',
                    'avatar': 'Shows the user\'s avatars.',
                    '8ball': 'Generates a random answer for any question. All matches are random!',
                    'rngen': 'Generates a number in a specified range.',
                    'guild': 'Shows guild (server) info',
                    'calc': 'Simplest calculator.',
                    'settings': 'Bot settings.',
                    'settings_lang': 'Changing bot language.',
                    'publish': 'Publishes messages from news channel without extra clicks on the mouse button.',
                    'ping': 'Ping me.',
                    'weather': 'Displays the weather forecast for the next 24 hours. This is done using the [OpenWeatherMap](https://openweathermap.org) service.',
                    'weather2': 'Displays the weather forecast for the next 24 hours.',
                    'wiki': 'Displays a Wikipedia article in short form.',
                    'codec': 'Decoding and coding of text.'
                }
            elif where == "embed_footer":
                locale = {
                    '8ball': 'All matches are random!'
                }
            elif where == "command_examples":
                locale = {
                    'help': '```{0}help```',
                    'about': '```{0}about```',
                    'user': '```{0}user [@mention or member ID]```',
                    'avatar': '```{0}avatar [@mention or member ID]```',
                    '8ball': '```{0}8ball [question]```',
                    'rngen': '```{0}rngen [beginning of range]-[end of range]```',
                    'guild': '```{0}guild```',
                    'calc': '```{0}calc [expression]```',
                    'settings': '```{0}settings [-L] [value]\r\n{0}settings -L en_US```',
                    'settings_lang': '```{0}settings -L [en_US / ru_RU]\r\n{0}settings -L ru_RU```',
                    'publish': '```{0}publish This is what the post looks like!```',
                    'ping': '```{0}ping```',
                    'weather': '```{0}weather Paris\r\n{0}weather London\r\n{0}weather Saint-Petersburg\r\n{0}weather Barnaul```',
                    'wiki': '```{0}wiki Sinus\r\n{0}wiki Android\r\n{0}wiki Kunstkamera\r\n{0}wiki Proxy server\r\n{0}wiki Emoji```',
                    'codec': '```{0}codec -e base64 Base64 encoding text example.\r\n{0}codec -e binary Binary text decoding example.\r\n{0}codec -d base64 QmFzZTY0IHRleHQgZGVjb2RpbmcgZXhhbXBsZS4=```'
                }
            elif where == "button":
                locale = {
                    'user_avatar': 'Show avatar',
                    'rngen_retry': 'Retry',
                }
            elif where == "numb_with_unit":
                locale = {
                    'bytes': '{0} bytes',
                    'bytes2': '{0} / {1} bytes',
                    'kilobytes': '{0} kB',
                    'kilobytes2': '{0} / {1} kB',
                    'megabytes': '{0} MB',
                    'megabytes2': '{0} / {1} MB',
                    'gigabytes': '{0} GB',
                    'gigabytes2': '{0} / {1} GB',
                }
            else:
                locale = {
                }
            if len(locale) == 0: # if string not found (variant #1)
                return "[{0}|{1}] String not found".format(str, where)
            else:
                return locale[str]
    except:
            if language == "ru_RU": # if string not found (variant #2)
                return "[{0}|{1}] Строка не найдена".format(str, where)
            else:
                return "[{0}|{1}] String not found".format(str, where)

def getLanguages():
    languages = {'ru_RU': 'Russian', 'en_US': 'English'}
    return languages
