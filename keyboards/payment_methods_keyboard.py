from aiogram import types

keyboard = types.InlineKeyboardMarkup(1)
qiwi = types.InlineKeyboardButton('🥝 QIWI | 💳 Карта', callback_data='method_qiwi')
#yoo = types.InlineKeyboardButton('YOOMONEY | 💳 Карта', callback_data='method_yoo')
pay_pal = types.InlineKeyboardButton('PAYPAL', callback_data='method_palka')
back = types.InlineKeyboardButton('Назад', callback_data='cancel_payment')
keyboard.add(qiwi,pay_pal,back)