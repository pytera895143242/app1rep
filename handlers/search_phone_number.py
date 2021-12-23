from loader import dp
from aiogram import types
from filters.is_phone_number import Is_Phone_Number
import json
from base_lang import cheack_lang
from keyboards import search_phone_number_keyboard,search_result_keyboard
import datetime
import asyncio
import random

@dp.message_handler(Is_Phone_Number())
async def search_phone_number(message: types.Message):
    with open('data/prices.json') as json_file:
        prices = json.load(json_file)
        price = prices['Phone_Number']
    number = message.text.split(' ')[0]
    if cheack_lang(message.chat.id) == 'ru' :
        text = f'''<b>⚙ Пользователь:\n\n💬 Номер {number}\n\n</b>➖➖➖➖➖➖➖➖➖➖➖\n\n<i>🔞 Приватные фотографии пользователя: ?\n⛔ Скрытые данные пользователя: ?\n👥 Соцсети пользователя: ?</i>\n\n<b>💰 Стоимость проверки: {price} RUB💳</b>'''
        await message.answer(text, reply_markup=search_phone_number_keyboard.keyboard)
    else:
        start_date = datetime.date(2020, 1, 1)
        end_date = datetime.date(2020, 2, 1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days=random_number_of_days)
        loading = await message.answer('<b>A search is underway... 🔎</b>')
        await asyncio.sleep(2)
        await loading.edit_text('<b>Checking our hacks... ♻️</b>')
        await asyncio.sleep(2)
        await loading.edit_text('<b>Checking our plums... ♻️</b>')
        await asyncio.sleep(2)
        await loading.delete()
        text = f'''<b>Hacking found ✅</b>\n\n<b>Phone number: </b>{number}\n<b>Date of hacking: </b>{random_date}\n<b>Intimate photos: </b>In stock ✅\n<b>Sex videos: </b>In stock ✅'''
        text2 = f'''<b>{number}</b> |<b>25.00 💵USD</b>\n\n<b>🗂The archive of the hacked page has already been formed. All dialogs and page attachments are ready to be sent.</b>'''
        await message.answer(text)
        await message.answer(text2, reply_markup=search_result_keyboard.keyboard_eng)