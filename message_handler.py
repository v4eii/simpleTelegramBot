import telegram
import state
from telebot.types import *
from util import *


@bot.message_handler(commands=['start'])
def start_message(message: Message):
    bot.send_message(message.chat.id, "Ну здарова. Можешь тыкнуть/написать /help")


@bot.message_handler(commands=['keyboard'])
def start_message(message: Message):
    bot.send_message(message.chat.id, "Ну допустим на", reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def print_help_info(message: Message):
    bot.send_message(message.chat.id, help_text)


@bot.message_handler(commands=['reg'])
def register(message: Message):
    t_user = message.from_user
    if t_user.username == get_user_by_message(t_user).username:
        bot.send_message(message.chat.id, "А ты уже зареган, ничего не знаю")
    else:
        bot.send_message(t_user.id, "Ну окей, как тебя звать?")
        bot.register_next_step_handler_by_chat_id(t_user.id, get_name, User("", "", 0, ""))


@bot.message_handler(commands=['freg'])
def fast_register(message: Message):
    t_user = message.from_user
    if t_user.username == get_user_by_message(t_user).username:
        bot.send_message(message.chat.id, "А ты уже зареган, ничего не знаю")
    else:
        user_list.append(User(t_user.first_name, t_user.last_name, 0, t_user.username))
        bot.send_message(t_user.id, f"Ладно, давай по-быстренькому, зарегал тебя как {t_user.first_name} {t_user.last_name}")


@bot.message_handler(commands=['unreg'])
def unreg(message: Message):
    user = get_user_by_message(message.from_user)
    if user.username != "":
        user_list.remove(user)
        bot.send_message(message.chat.id, f"Ну и не сильно то хотелось, пока {user.name} {user.surname}")
    else:
        bot.send_message(message.chat.id, f"То что мертво - умереть не может (ты и не зареган)")


@bot.message_handler(commands=['users'])
def get_users_list(message: Message):
    if not user_list:
        bot.send_message(message.chat.id, "А пользователей то нет, грустненько")
    else:
        def to_str(x):
            return x.__str__() if x.username != message.from_user.username else "<b>" + x.__str__() + " - Вы</b>"
        bot.send_message(
            chat_id=message.chat.id,
            text="Держи: \n" + str([to_str(x) for x in user_list]),
            parse_mode=telegram.ParseMode.HTML
        )


@bot.message_handler(commands=['stick_id'])
def change_show_sticker_id_flag(message: Message):
    state.is_print_sticker_id = not state.is_print_sticker_id
    if state.is_print_sticker_id:
        bot.send_message(message.chat.id,
                         "Распознавание стикеров активированно, пришли стикер и получишь его id, для отключения выполни команду еще раз")
    else:
        bot.send_message(message.chat.id, "Распознавание стикеров отключено, а тебе оно вообще зачем надо было?")


@bot.message_handler(commands=['link'])
def change_read_write_links(message: Message):
    state.is_read_write_links = not state.is_read_write_links
    if state.is_read_write_links:
        bot.send_message(message.chat.id,
                         "Чтение/запись ссылок активированно, для отключения выполни ту же команду")
    else:
        bot.send_message(message.chat.id, "Чтение/запись ссылок выключено")


@bot.message_handler(content_types=['text'])
def send_text_response(message: Message):
    if state.is_read_write_links:
        t_user = message.from_user
        user = get_user_by_message(t_user)
        if t_user.username == user.username:
            if message.entities is not None:
                split_links_and_name_and_save(message, user)
            else:
                try:
                    bot.send_message(message.chat.id, user.personal_links[message.text.lower()])
                except KeyError:
                    bot.send_message(message.chat.id, "Ой-иооой, а я не нахожу такого значения, точно правильно пишешь? Или это я глупый?")
        else:
            bot.send_message(message.chat.id, "А я тебя не знаю, пройди /reg or /freg и потом возвращайся")
    else:
        if message.text.lower() == "hi" or message.text.lower() == "привет":
            bot.reply_to(message, f"Привет, {message.from_user.username}")
        elif message.text.lower() == "спасибо" or message.text.lower() == "хаха":
            bot.send_message(message.chat.id, "хе-хе")
        else:
            bot.send_sticker(message.chat.id, get_random_sticker())


@bot.message_handler(content_types=['sticker'])
def check_sticker_id(message: Message):
    if state.is_print_sticker_id:
        bot.send_message(message.chat.id, message.sticker.file_id)
        bot.send_message(message.chat.id, "Для отключения выполни /stick_id")


@bot.edited_message_handler(func=lambda message: True)
def edited_message_response(message: Message):
    bot.reply_to(message, "Агаааа, редачеж")

# @bot.message_handler(content_types=[''])


bot.polling()
