from aiogram import types

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
find_leaks = types.KeyboardButton('🔍 Найти сливы 🔍')
help = types.KeyboardButton('👨🏼‍🔧 Тех. поддержка 👨🏼‍🔧')
# referals = types.KeyboardButton('🤑 Реферальная система 🤑')
examples = types.KeyboardButton('💡 Примеры 💡')
statistics = types.KeyboardButton('🌐 Статистика 🌐')
language = types.KeyboardButton('Bot language / Язык бота')
keyboard.row(find_leaks)
keyboard.row(help)
# keyboard.row(referals)
keyboard.row(examples, statistics)
keyboard.row(language)


keyboard_eng = types.ReplyKeyboardMarkup(resize_keyboard=True)
find_leaks = types.KeyboardButton('🔍 Find nudes 🔍')
examples = types.KeyboardButton('💡 Examples 💡')
statistics = types.KeyboardButton('🌐 Statistics 🌐')
keyboard_eng.row(find_leaks)
keyboard_eng.row(language)
# keyboard.row(examples, statistics)