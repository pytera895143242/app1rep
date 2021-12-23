from aiogram import types

keyboard = types.InlineKeyboardMarkup(1)
ru = types.InlineKeyboardButton('🇷🇺 Русский 🇷🇺', callback_data='ru')
eng = types.InlineKeyboardButton('🇬🇧 English 🇬🇧', callback_data='eng')
keyboard.add(ru,eng)
