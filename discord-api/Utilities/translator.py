# Microbot Discord bot
# Repo: https://github.com/tinelix/microbot
# Licensed under Apache License v2.0 & GNU Affero General Public License v3.0 and higher

def translate(where, str, language):
    try:
        if language == "ru_RU": # Russian
            if where == "message":
                locale = {
                    'prefix': '**Префикс:** `{0}`\r\nПоддерживаются также слэш-команды.'
                }
            elif where == "embed_title":
                locale = {
                    'error': '❎ Ошибка',
                    'help': '❔ Справка',
                    'cmd_help': 'Команда `{0}`',
                    'fatalerr_reporter': '🛠 У нас что-то сломалось!',
                    'about': '🤖 О боте',
                    'user': '👤 {0} / {1}',
                    'user2': '👤 {0}',
                    'user_bot': '🤖 {0} / {1}',
                    'user_bot2': '🤖 {0}',
                    'user_owner': '👑 {0} / {1}',
                    'user_owner2': '👑 {0}',
                    'avatar': '🖼 Аватар пользователя {0}',
                    'forbidden': '🚫 Доступ запрещен',
                    'eval': '⌨ Интерпретатор',
                    '8ball': '🎱 Генератор случайных ответов',
                    'rngen': '🎱 Генератор случайных чисел',
                    'calc': '🔢 Калькулятор',
                    'settings': '⚙ Настройки',
                    'msg_author': '📣 Публикация от {0} / _`{1}`_',
                    'ping': '🏓 Понг!',
                    'weather': '⛅ Погода',
                    'weather2': '⛅ {0}, {1}',
                    'wikipedia': '🌐 Википедия',
                    'codec': '🔡 Кодек',
                    'timers': '⏲️ Таймеры',
                }
            elif where == "embed_description":
                locale = {
                    'help': '**{0}** - простейший и компактный бот для Discord.\r\nХотите узнать, для чего нужны команды? Вбейте `{1}help [имя команды]`.\r\n[Пригласить]({2})',
                    'error_unf': '😔 Пользователь не найден. Попробуйте найти другого пользователя.',
                    'fatalerr_reporter': '🪲 Да, у нас и такое случается. Но ничего страшного, скоро мы это отремонтируем.',
                    'forbidden': '🚫 Вы не имеете права пользоваться этой командой!',
                    'please_wait': '⌛ Подождите...',
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
                    'wikipedia': '{0}\r\n[Подробнее...]({1})',
                    'timers': '⏲️ Тут ничего нет, но вы можете создать хоть один таймер.',
                    'timers_created': '✅ Таймер создан.',
                    'timers_deleted': '✅ Таймер удален.',
                    'timers_invelapsdt': '❌ Указанная дата должна быть не позднее сегодняшней!',
                    'timers_invupcomdt': '❌ Указанная дата должна быть не раньше сегодняшней!',
                    'tz_invalidabbr': '❌ Вы ввели неверное обозначение часового пояса. Смотрите [по ссылке](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) (столбец Notes) для подробной информации.',
                    'invalid_cmd_usage': 'Вы используете эту команду неправильно или не указали одно из требуемых параметров. Смотрите её синтаксис и пример.',
                }
            elif where == "embed_fields":
                locale = {
                    'help_preff': 'Префиксы',
                    'help_prefv': '{0} или `/`',
                    'help_cmdsf': 'Команды',
                    'help_cmdsv': '{0}',
                    'help_exampf': 'Пример',
                    'help_aliasf': 'Аналогичные названия',
                    'eval_codelf': 'Листинг',
                    'eval_resulf': 'Результат',
                    'about_versf': 'Версия',
                    'about_versf2': 'На основе {0}',
                    'about_versv': '{0} ({1})',
                    'about_devsf': 'Разработчик',
                    'about_devsv': '{0} / _`{1}`_',
                    'about_regdf': 'Дата регистрации',
                    'about_regdv': '{0}',
                    'about_statsf': 'Статистика',
                    'about_statsv': '{0} серверов\r\n{1} пользователей',
                    'about_uptimef': 'Активен',
                    'about_uptimev': '{0}',
                    'about_basedf': 'Работает на базе',
                    'about_basedv': 'Python {0}\r\nDisnake {1}\r\nSQLite {2}',
                    'about_hardwf': 'Оборудование',
                    'about_hardwv': '**ЦП:** {0} ({1} МГц)\r\n**ОЗУ:** {2}\r\n**Платформа:** {3}',
                    'about_linksf': 'Ссылки',
                    'about_linksv': '[Пригласить]({0})',
                    'about_linksv2': '[Сайт]({0})',
                    'about_linksv3': '[Исходный код]({0})',
                    'about_linksv4': '[Сервер поддержки]({0})',
                    'about_linksv5': '[Донат]({0})',
                    'about_licensesf': 'О лицензиях',
                    'about_licensesv': 'Это свободное программное обеспечение с открытым исходным кодом, предназначенное для работы с сетевыми API и распространяемое в соответствии с условиями [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) и [GNU Affero GPL 3.0 (или выше)](https://www.gnu.org/licenses/agpl-3.0.html).',
                    'user_nickf': 'Псевдоним',
                    'user_nickv': '{0}',
                    'user_nickvn': '*Отсутствует*',
                    'user_regdf': 'Дата регистрации',
                    'user_regdv': '{0}',
                    'user_joinf': 'Дата входа на сервер',
                    'user_joinv': '{0}',
                    'user_statusf': 'Статус',
                    'user_statusv': '<:online:1012294415731146765> Онлайн',
                    'user_statusv2': '<:idle:1012294411020947457> Отошел',
                    'user_statusv3': '<:dnd:1012294408412082186> Не беспокоить',
                    'user_statusv4': '<:offline:1012294452246753300> Оффлайн',
                    'user_rolesf': 'Роли ({0})',
                    'user_rolesv': '{0}',
                    'guild_ownerf': 'Владелец',
                    'guild_ownerv': '{0}\r\n({1} / _`{2}`_)',
                    'guild_crtf': 'Дата создания',
                    'guild_crtv': '{0}',
                    'guild_blvlf': 'Уровень бустов',
                    'guild_blvlv': '_Пока еще нет бустов_',
                    'guild_blvlv2': 'Уровень {0} / {1} бустов',
                    'guild_mlvlf': 'Уровень модерации',
                    'guild_mlvlv': 'Нет ограничений',
                    'guild_mlvlv2': 'Только подтвержденный e-mail',
                    'guild_mlvlv3': 'Регистрация более 5 минут',
                    'guild_mlvlv4': 'Присутствие более 10 минут',
                    'guild_mlvlv5': 'Только подтвержденный телефон',
                    'guild_statsf': 'Статистика',
                    'guild_statsv': '**Всего {0} участников**\r\n<:users:1014484889732653066> {1} ({2}%)\r\n<:bots:1014484886515630080> {3} ({4}%)\r\n<:online:1012294415731146765> {5} ({6}%)\r\n<:channels:1012296573364998196> {7}',
                    'guild_rulesf': 'Правила',
                    'guild_rulesv': '{0}',
                    'guild_featurf': 'Функции',
                    'guild_featurv': 'Автомодерация',
                    'guild_featurv2': 'Сообщество',
                    'guild_featurv3': 'Новости',
                    'guild_featurv4': 'Чаты в голосовых каналах',
                    'guild_featurv5': 'Экран приветствия',
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
                    'settings_gsettf': 'Настройки сервера',
                    'settings_gsettv': 'Язык: 🇷🇺 Русский\r\nПрефикс: {0}',
                    'settings_usettf': 'Настройки пользователя',
                    'settings_usettv': 'Часовой пояс: {0}',
                    'settings_availoptf': 'Доступные параметры',
                    'settings_availoptv': '🚩 Язык (Language)\r\n🪄 Префикс\r\n🕒 Часовой пояс',
                    'ping_statisticsf': 'Статистика',
                    'ping_statisticsv': '**Задержка:** {0} мсек\r\n**Задержка веб-сокета:** {1} мсек\r\n',
                    'ping_statisticsv2': '**Задержка:** {0} мсек\r\n**Задержка веб-сокета:** {1} мсек\r\n**Время выполнения:** {2} мсек',
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
                    'timers_dcr': 'Осталось {0} дн. {1} ч. {2} мин. {3} сек.',
                    'timers_dce': 'Прошло {0} дн. {1} ч. {2} мин. {3} сек.',
                    'timers_dco': 'Время закончилось',
                }
            elif where == "embed_footer":
                locale = {
                    '8ball': 'Все совпадения случайны!',
                    'help': 'Версия {0}',
                    'help2': 'На основе Microbot версии {0}',
                }
            elif where == "command_categories":
                locale = {
                    'main': '🤖 Главное',
                    'fun': '🎭 Развлечения',
                    'interactivity': '🌐 Интерактивность',
                    'personalization': '🎨 Персонализация',
                    'other': '*️⃣ Другое'
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
                    'codec': 'Расшифровка и зашифровка текста',
                    'timers': 'Создание и управление таймерами в прошедшее и оставшиеся времени.',
                }
            elif where == "command_examples":
                locale = {
                    'help': '```{0}help```',
                    'about': '```{0}about```',
                    'user': '```{0}user [@упоминание | ID участника | юзернейм]```',
                    'avatar': '```{0}avatar [@упоминание | ID участника | юзернейм]```',
                    '8ball': '```{0}8ball [вопрос]```',
                    'rngen': '```{0}rngen [начало диапазона]-[конец диапазона]```',
                    'guild': '```{0}guild```',
                    'settings': '```{0}settings [-L] [значение]\r\n{0}settings -L en_US```',
                    'settings_lang': '```{0}settings -L [en_US / ru_RU]\r\n{0}settings -L en_US```',
                    'settings_prefix': '```{0}settings -P [префикс]\r\n{0}settings -P m!```',
                    'settings_tz': '```{0}settings -tz [обозначение часового пояса]\r\n{0}settings -tz Europe/Moscow\r\n{0}settings -tz Asia/Barnaul```',
                    'publish': '```{0}publish [текст]\r\n{0}publish Вот так выглядит публикация!```',
                    'ping': '```{0}ping```',
                    'weather': '```{0}weather [город или населенный пункт]\r\n{0}weather Париж\r\n{0}weather Лондон\r\n{0}weather Санкт-Петербург\r\n{0}weather Барнаул```',
                    'wiki': '```{0}wiki [полное название страницы]\r\n{0}wiki Синус\r\n{0}wiki Android (операционная система)\r\n{0}wiki Кунсткамера\r\n{0}wiki Прокси-сервер\r\n{0}wiki Эмодзи```',
                    'codec': '```{0}codec [-d / -e] [алгоритм] [содержимое]\r\n{0}codec -e base64 Base64 text encoding.\r\n{0}codec -e binary Это перевод текста в двоичный код.\r\n{0}codec -d base64 QmFzZTY0IHRleHQgZGVjb2RpbmcgZXhhbXBsZS4=```',
                    'calc': '```{0}calc [выражение]```',
                    'timers': '```{0}timers```',
                    'timers_create': '```{0}timers [-Cr / -Ce] [имя таймера] -t [ГГГГ-ММ-ДД ЧЧ:ММ:СС] -e [эмодзи]\r\n{0}timers -Cr Новый год -t 2024-01-01 00:00:00 -e 🎄\r\n{0}timers -Ce Начало карьеры -t 2016-03-27 00:00:00 -e 📹```',
                    'timers_delete': '```{0}timers -D [имя таймера]\r\n{0}timers -D Начало карьеры```',
                }
            elif where == "button":
                locale = {
                    'user_avatar': 'Показать аватар',
                    'rngen_retry': 'Повторить',
                    'timers_create': 'Создать',
                    'timers_delete': 'Удалить',
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
            if where == "message":
                locale = {
                    'prefix': '**Prefix:** `{0}`\r\nSlash commands are also supported.'
                }
            elif where == "embed_title":
                locale = {
                    'error': '❎ Error',
                    'help': '❔ Help',
                    'cmd_help': '`{0}` command',
                    'about': '❔ About',
                    'user': '👤 {0} / {1}',
                    'user2': '👤 {0}',
                    'user_bot': '🤖 {0} / {1}',
                    'user_bot2': '🤖 {0}',
                    'user_owner': '👑 {0} / {1}',
                    'user_owner2': '👑 {0}',
                    'avatar': '🖼 {0}\'s avatar',
                    'fatalerr_reporter': '🛠 We\'ve got something broken!',
                    'forbidden': '🚫 Access forbidden',
                    'eval': '⌨ Interpreter',
                    '8ball': '🎱 Random Answer Generator',
                    'rngen': '🎱 Random Number Generator',
                    'calc': '🔢 Calculator',
                    'settings': '⚙ Settings',
                    'msg_author': '📣 Post by {0} / _`{1}`_',
                    'ping': '🏓 Pong!',
                    'weather': '⛅ Weather',
                    'weather2': '⛅ {0}, {1}',
                    'wikipedia': '🌐 Wikipedia',
                    'codec': '🔡 Codec',
                    'timers': '⏲️ Timers',
                }
            elif where == "embed_description":
                locale = {
                    'help': '**{0}** - is a simple and compact bot for Discord.\r\nWant to know what the commands is for? Type `{1}help [command name]`.\r\n[Invite]({2})',
                    'error_unf': '😔 User not found. Try to find another user.',
                    'fatalerr_reporter': '🪲 Yes, this happens to us too. But don\'t worry, we\'ll fix it soon.',
                    'forbidden': '🚫 You do not have the right to use this command!',
                    'please_wait': '⌛ Wait...',
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
                    'wikipedia': '{0}\r\n[More...]({1})',
                    'timers': '⏲️ There\'s nothing there, but you can create at least one timer.',
                    'timers_created': '✅ Timer created.',
                    'timers_deleted': '✅ Timer deleted.',
                    'timers_invelapsdt': '❌ The specified date must be no later than today!',
                    'timers_invupcomdt': '❌ The specified date must not be earlier than today!',
                    'tz_invalidabbr': '❌ You have entered an invalid timezone alias. See [link](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones#List) (Notes column) for details.',
                    'invalid_cmd_usage': 'You are using this command incorrectly, or you have not provided one of the required parameters. See its syntax and example.',
                }
            elif where == "embed_fields":
                locale = {
                    'help_preff': 'Prefixes',
                    'help_prefv': '{0} or `/`',
                    'help_cmdsf': 'Commands',
                    'help_cmdsv': '{0}',
                    'help_exampf': 'Examples',
                    'help_aliasf': 'Aliases',
                    'eval_codelf': 'Code listing',
                    'eval_resulf': 'Result',
                    'about_versf': 'Version',
                    'about_versf2': 'Based on {0}',
                    'about_versv': '{0} ({1})',
                    'about_devsf': 'Developer',
                    'about_devsv': '{0} / _`{1}`_',
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
                    'about_linksv3': '[Source code]({0})',
                    'about_linksv4': '[Support server]({0})',
                    'about_linksv5': '[Donate]({0}) (for RU/BY)',
                    'about_licensesf': 'About licenses',
                    'about_licensesv': 'This is free software with open source, designed to work with network APIs and distributed under the terms of the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) и [GNU Affero GPL 3.0 (or higher)](https://www.gnu.org/licenses/agpl-3.0.html).',
                    'user_nickf': 'Nickname',
                    'user_nickv': '{0}',
                    'user_nickvn': '*Missing*',
                    'user_regdf': 'Registration date',
                    'user_regdv': '{0}',
                    'user_joinf': 'Server join date',
                    'user_joinv': '{0}',
                    'user_statusf': 'Status',
                    'user_statusv': '<:online:1012294415731146765> Online',
                    'user_statusv2': '<:idle:1012294411020947457> Idle',
                    'user_statusv3': '<:dnd:1012294408412082186> DND',
                    'user_statusv4': '<:offline:1012294452246753300> Offline',
                    'user_rolesf': 'Roles ({0})',
                    'user_rolesv': '{0}',
                    'guild_ownerf': 'Owner',
                    'guild_ownerv': '{0} ({1} / _`{2}`_)',
                    'guild_crtf': 'Creation date',
                    'guild_crtv': '{0}',
                    'guild_mlvlf': 'Moderation level',
                    'guild_mlvlv': 'No limits',
                    'guild_mlvlv2': 'Only confirmed e-mail',
                    'guild_mlvlv3': 'Registration over 5 minutes',
                    'guild_mlvlv4': 'Presence over 10 minutes',
                    'guild_mlvlv5': 'Only confirmed phone',
                    'guild_blvlf': 'Boost level',
                    'guild_blvlv': '_No boosts yet_',
                    'guild_blvlv2': 'Level {0} / {1} boosts',
                    'guild_statsf': 'Statistics',
                    'guild_statsv': '**{0} members total**\r\n<:users:1014484889732653066> {1} ({2}%)\r\n<:bots:1014484886515630080> {3} ({4}%)\r\n<:online:1012294415731146765> {5} ({6}%)\r\n<:channels:1012296573364998196> {7}',
                    'guild_rulesf': 'Rules',
                    'guild_rulesv': '{0}',
                    'guild_featurf': 'Features',
                    'guild_featurv': 'Automod',
                    'guild_featurv2': 'Community',
                    'guild_featurv3': 'News',
                    'guild_featurv4': 'Text in voice ch.',
                    'guild_featurv5': 'Welcome screen',
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
                    'settings_gsettf': 'Guild settings',
                    'settings_gsettv': 'Language: 🇺🇸  English\r\nPrefix: {0}',
                    'settings_usettf': 'User settings',
                    'settings_usettv': 'Timezone: {0}',
                    'settings_availoptf': 'Available options',
                    'settings_availoptv': '🚩 Язык (Language)\r\n🪄 Prefix\r\n🕒 Timezone',
                    'ping_statisticsf': 'Statistics',
                    'ping_statisticsv': '**Latency:** {0} msec\r\n**WebSocket latency:** {1} msec',
                    'ping_statisticsv2': '**Latency:** {0} msec\r\n**WebSocket latency:** {1} msec\r\n**Execution time:** {2} msec',
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
                    'timers_dcr': '{0} d. {1} h. {2} min. {3} sec. remaining',
                    'timers_dce': '{0} d. {1} h. {2} min. {3} sec. elapsed',
                    'timers_dco': 'Time is over',
                }
            elif where == "embed_footer":
                locale = {
                    '8ball': 'All matches are random!',
                    'help': 'Version {0}',
                    'help2': 'Based on Microbot ver. {0}',
                }
            elif where == "command_categories":
                locale = {
                    'main': '🤖 Main',
                    'fun': '🎭 Fun',
                    'interactivity': '🌐 Interactivity',
                    'personalization': '🎨 Personization',
                    'other': '*️⃣ Other'
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
                    'codec': 'Decoding and coding of text.',
                    'timers': 'Creating and managing timers in elapsed and remaining time.',
                }
            elif where == "command_examples":
                locale = {
                    'help': '```{0}help```',
                    'about': '```{0}about```',
                    'user': '```{0}user [@mention | member ID | username]```',
                    'avatar': '```{0}avatar [@mention | member ID | username]```',
                    '8ball': '```{0}8ball [question]```',
                    'rngen': '```{0}rngen [beginning of range]-[end of range]```',
                    'guild': '```{0}guild```',
                    'calc': '```{0}calc [expression]```',
                    'settings': '```{0}settings [-L / -P / -tz] [value]\r\n{0}settings -L ru_RU```',
                    'settings_lang': '```{0}settings -L [en_US / ru_RU]\r\n{0}settings -L ru_RU```',
                    'settings_prefix': '```{0}settings -P [prefix]\r\n{0}settings -P m!```',
                    'settings_tz': '```{0}settings -tz [timezone designation]\r\n{0}settings -tz Europe/Moscow\r\n{0}settings -tz Asia/Barnaul```',
                    'publish': '```{0}publish [text]\r\n{0}publish This is what the post looks like!```',
                    'ping': '```{0}ping```',
                    'weather': '```{0}weather [city]\r\n{0}weather Paris\r\n{0}weather London\r\n{0}weather Saint-Petersburg\r\n{0}weather Barnaul```',
                    'wiki': '```{0}wiki [full page name]\r\n{0}wiki Sinus\r\n{0}wiki Android (operating system)\r\n{0}wiki Kunstkamera\r\n{0}wiki Proxy server\r\n{0}wiki Emoji```',
                    'codec': '```{0}codec [-d / -e] [standard] [content]\r\n{0}codec -e base64 Base64 encoding text example.\r\n{0}codec -e binary Binary text decoding example.\r\n{0}codec -d base64 QmFzZTY0IHRleHQgZGVjb2RpbmcgZXhhbXBsZS4=```',
                    'timers': '```{0}timers```',
                    'timers_create': '```{0}timers [-Cr / -Ce] [timer name] -t [YYYY-MM-DD HH:MM:SS] -e [emoji]\r\n{0}timers -Cr New Year -t 2024-01-01 00:00:00 -e 🎄\r\n{0}timers -Ce Carier start -t 2016-03-27 00:00:00 -e 📹```',
                    'timers_delete': '```{0}timers -D [timer name]\r\n{0}timers -D Carier start```',
                }
            elif where == "button":
                locale = {
                    'user_avatar': 'Show avatar',
                    'rngen_retry': 'Retry',
                    'timers_create': 'Create',
                    'timers_delete': 'Delete',
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

def formatDate(datetime, size, language):
    if(language == 'ru_RU'):
        if(size == 'full'):
            days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
            months = ['', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']
            return f'{days_of_week[datetime.weekday()]}, {datetime.day} {months[datetime.month]} {datetime.year} г. в {datetime.hour:02d}:{datetime.minute:02d}:{datetime.second:02d}'
        elif(size == 'normal'):
            days_of_week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
            months = ['', 'янв.', 'фев.', 'мар.', 'апр.', 'мая', 'июн.', 'июл.', 'авг.', 'сен.', 'окт.', 'ноя.', 'дек.']
            return f'{days_of_week[datetime.weekday()]}, {datetime.day} {months[datetime.month]} {datetime.year} г. в {datetime.hour:02d}:{datetime.minute:02d}:{datetime.second:02d}'
        elif(size == 'compact'):
            days_of_week = ['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс']
            months = ['', 'янв.', 'фев.', 'мар.', 'апр.', 'мая', 'июн.', 'июл.', 'авг.', 'сен.', 'окт.', 'ноя.', 'дек.']
            return f'{days_of_week[datetime.weekday()]}, {datetime.day} {months[datetime.month]} {datetime.year} г.'
    else:
        if(size == 'full'):
            days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
            months = ['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'September', 'November', 'December']
            return f'{days_of_week[datetime.weekday()]}, {months[datetime.month]} {datetime.day}, {datetime.year} at {datetime.hour:02d}:{datetime.minute:02d}:{datetime.second:02d}'
        elif(size == 'normal'):
            days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            return f'{days_of_week[datetime.weekday()]}, {months[datetime.month]} {datetime.day}, {datetime.year} at {datetime.hour:02d}:{datetime.minute:02d}:{datetime.second:02d}'
        elif(size == 'compact'):
            days_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
            months = ['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            return f'{days_of_week[datetime.weekday()]}, {months[datetime.month]} {datetime.day}, {datetime.year}'
