from aiogram import types

def make_keyboard(url: str, type: str, pref = ''):
    keyboard = types.InlineKeyboardMarkup(1)
    link = types.InlineKeyboardButton('💳 Перейти к оплате', callback_data='procced_payment', url=url)
    check = types.InlineKeyboardButton('🔄 Проверить оплату', callback_data=f'{pref}check_payment_{type}')
    cancel = types.InlineKeyboardButton('❌ Отменить', callback_data='cancel_payment')
    keyboard.add(link, check, cancel)
    return keyboard


def make_paypal():
    keyboard = types.InlineKeyboardMarkup(1)
    link = types.InlineKeyboardButton('💳 Go to payment', url = 'paypal.me/GlavBot')
    check = types.InlineKeyboardButton('🔄 Check payment', callback_data= 'naebka')
    cancel = types.InlineKeyboardButton('❌ Cancel', callback_data='cancel_payment')
    keyboard.add(link, check, cancel)
    return keyboard