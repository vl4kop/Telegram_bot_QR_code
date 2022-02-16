from config import TOKEN
import telebot
from MyQR import myqr
import os
import time
from random import choice

bot = telebot.TeleBot(TOKEN)

answers = ['Я понимаю только латиницу',
           'Напиши на латинице',
           'Получится только с латиницей',
           'Попробуй латиницу',
           'Не, лучше латиницей']


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_sticker(message.chat.id,
                     "CAACAgIAAxkBAAED8v9iDLuBsa8ezfThjzmkKUInSfPsyQAC0wADVp29CvUyj5fVEvk9IwQ")
    time.sleep(2)
    bot.send_message(message.chat.id, 'Привет. Напиши текст на латинице, а я сгенерирую QR код')


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    name_for_qr = str(time.time()).replace('.', '_') + '.png'
    name_of_dir = 'QRcodes'
    try:
        myqr.run(words=message.text, save_name=name_for_qr, save_dir=name_of_dir)
        bot.send_photo(message.chat.id, open(f'{name_of_dir}/{name_for_qr}', 'rb'))
        os.remove(f'{name_of_dir}/{name_for_qr}')
    except ValueError:
        bot.send_message(message.chat.id, choice(answers))


@bot.message_handler(
    content_types=['document', 'audio', 'photo', 'video', 'video_note', 'voice', 'location', 'contact',
                   'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo', 'delete_chat_photo',
                   'group_chat_created', 'supergroup_chat_created', 'channel_chat_created', 'migrate_to_chat_id',
                   'migrate_from_chat_id', 'pinned_message', 'sticker'])
def ignore_other_types(message):
    bot.send_sticker(message.chat.id,
                     "CAACAgIAAxkBAAED8vtiDLokWJo5vKjOhRDhZO7liMuzNgAC4wADVp29Cg_4Isytpgs3IwQ")
    time.sleep(2)
    bot.send_message(message.chat.id, 'Данный тип сообщений не поддерживается. Для получения QR кода \
введите сообщение на латинице')


bot.polling()
