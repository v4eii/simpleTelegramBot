import telebot
from telebot import types

import state
import util

bot = telebot.TeleBot("1523380614:AAG7DnONXtPhyt9YN735kI3-KHmfryerNWw")
keyboard = telebot.types.ReplyKeyboardMarkup(True, True)  # InlineKeyboardMarkup
keyboard.row("/reg", "/users", "/stick_id")


@bot.message_handler(commands=['start'])
def start_message(message: types.Message):
    bot.send_message(message.chat.id, "Ну здарова. Можешь тыкнуть/написать /help")


@bot.edited_message_handler(func=lambda message: True)
def edited_message_response(message: types.Message):
    bot.reply_to(message, "Агаааа, редачеж")


@bot.message_handler(commands=['keyboard'])
def start_message(message: types.Message):
    bot.send_message(message.chat.id, "Ну допустим на", reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def print_help_info(message: types.Message):
    bot.send_message(message.chat.id, util.help_text)


@bot.message_handler(commands=['reg'])
def register(message: types.Message):
    bot.send_message(message.from_user.id, "Ну окей, как тебя звать?")
    bot.register_next_step_handler(message, get_name, util.User())


def get_name(message: types.Message, user: util.User):
    user.name = message.text
    bot.send_message(message.from_user.id, "Окей, какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_surname, user)


def get_surname(message: types.Message, user: util.User):
    user.surname = message.text
    bot.send_message(message.from_user.id, "А, сколько тебе лет?")
    bot.register_next_step_handler(message, get_age, user)


def get_age(message: types.Message, user: util.User):
    age = 0
    while age == 0:
        try:
            age = int(message.text)
            user.age = age
            break
        except Exception:
            bot.send_message(message.from_user.id, "Я только цифры знаю")
            bot.register_next_step_handler(message, get_age, user)
            return
    bot.send_message(message.from_user.id,
                     f"Выходит ты {user.name} {user.surname} и тебе {user.age} ну крута чо. Я тебя запомню, не боись")
    if message.from_user.first_name != user.name or message.from_user.last_name != user.surname:
        bot.send_message(message.from_user.id,
                         f'Хотя я то знаю что ты на самом деле {message.from_user.first_name} {message.from_user.last_name}, так и быть промолчу')
    util.user_list.append(user)


@bot.message_handler(commands=['users'])
def get_users_list(message: types.Message):
    if not util.user_list:
        bot.send_message(message.from_user.id, "А пользователей то нет, грустненько")
    else:
        bot.send_message(message.from_user.id, "Держи: \n" + str([x.__str__() for x in util.user_list]))


@bot.message_handler(commands=['stick_id'])
def change_show_sticker_id_flag(message: types.Message):
    state.is_print_sticker_id = not state.is_print_sticker_id
    if state.is_print_sticker_id:
        bot.send_message(message.chat.id,
                         "Распознавание стикеров активированно, пришли стикер и получишь его id, для отключения выполни комманду еще раз")
    else:
        bot.send_message(message.chat.id, "Распознавание стикеров отключено, а тебе оно вообще зачем надо было?")


@bot.message_handler(commands=['link'])
def change_read_write_links(message: types.Message):
    state.is_read_write_links = not state.is_read_write_links
    if state.is_read_write_links:
        bot.send_message(message.from_user.id,
                         "Чтение/запись ссылок активированно, для отключения выполни ту же комманду")
    else:
        bot.send_message(message.from_user.id, "Чтение/запись ссылок выключено")


@bot.message_handler(content_types=['text'])
def send_text_response(message: types.Message):
    if state.is_read_write_links:
        user = util.user_list[0]

    else:
        entities = message.entities
        print(message)
        minus_last_position = 0
        text = message.text
        for entity in entities:
            if entity.type == "url":
                offset = entity.offset - minus_last_position
                length = entity.length
                print(f"o {entity.offset}")
                print(f"l {entity.length}")
                if offset > 0:
                    print(text[:offset].strip())
                print(text[offset:offset + length].strip())    # Смотреть на offset, если он 0, то как то сабстрингать и делить по пробелам и брать первый элемент
                text = text[offset + length:].strip()
                minus_last_position = offset + length + 1

        if message.text.lower() == "hi" or message.text.lower() == "привет":
            bot.reply_to(message, f"Привет, {message.from_user.username}")
        elif message.text.lower() == "спасибо" or message.text.lower() == "хаха":
            bot.send_message(message.chat.id, "хе-хе")
        else:
            bot.send_sticker(message.chat.id, util.get_random_sticker())


@bot.message_handler(content_types=['sticker'])
def check_sticker_id(message: types.Message):
    if state.is_print_sticker_id:
        bot.send_message(message.chat.id, message.sticker.file_id)
        bot.send_message(message.chat.id, "Для отключения выполни /stick_id")


# @bot.message_handler(content_types=[''])


bot.polling()
