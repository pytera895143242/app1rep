from aiogram import types

keyboard = types.InlineKeyboardMarkup(1)
ru = types.InlineKeyboardButton('๐ท๐บ ะ ัััะบะธะน ๐ท๐บ', callback_data='ru')
eng = types.InlineKeyboardButton('๐ฌ๐ง English ๐ฌ๐ง', callback_data='eng')
keyboard.add(ru,eng)
