cls
@echo off
echo Enter discord bot token
set /p token=">>> "
echo Enter OpenWeatherMap token
set /p openweathermap=">>> "
set DISCORD_TOKEN=token
set OPENWEATHERMAP_TOKEN=openweathermap
cd discord-api
py ./bot.py
cd ..
