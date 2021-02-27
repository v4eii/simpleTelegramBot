import random
import telebot
from telebot.types import Message
from telegram import ParseMode

unknown_sticker_set = ("CAACAgIAAxkBAAMxYDlil77mhgAB039EtvdMzGfeV6kdAAI0AwACEzmPEQ7-6IMS7E4GHgQ",
                       "CAACAgIAAxkBAAMzYDli4ePAI0LosSVz0gRCYaYwL5oAAjQDAAITOY8RDv7ogxLsTgYeBA",
                       "CAACAgIAAxkBAAM1YDli8jq1N2CrxwyWcrNzNqkySuUAAjMDAAITOY8RDWg_z_V_7LQeBA",
                       "CAACAgIAAxkBAAM3YDljHjNTSpmbJH4N2n0G1xmtNV0AAq0AA2iaXQxHbhn9BZwe4B4E",
                       "CAACAgIAAxkBAAM7YDljUJSlWNgDOO_pajfjuYIxmOsAAgcDAAITOY8RmyC1aplqaj0eBA",
                       "CAACAgQAAxkBAAIEGmA6OF-vse3l7y9tCf2YHlcuzPJXAAJGAgACcxpEBZYYxVdygfBiHgQ",
                       "CAACAgIAAxkBAAIEHWA6OKm0hJ50hsIuub3D-5Vol3XBAAIVAANoml0MdEY7iTyrMlAeBA",
                       "CAACAgIAAxkBAAIEIGA6OOh-LO-7-BbLvwgMYqW72A4hAAKlAQAC9xyXAuSCEFLNFOqTHgQ",
                       "CAACAgIAAxkBAAIEI2A6OQUv1po0C62SeXJjVHQf5oEqAAK3BgACEguhAuCKUqcR2elIHgQ")

help_text = """
Короче чо могу

    /stick_id - переключатель, если активирован я верну тебе id стикера который ты мне пришлешь, отключается так же
    /reg - приколюха типа "А кто ты такой?", зачем? По идее как для "регистрации", пока там хранятся персональные сохраненные ссылки
    /freg - быстрый аналог /reg, без лишних вопросов зарегает тебя
    /unreg - ну да, удалиться из списка. (Сохраненные ссылочки тоже слетят) 
    /users - показать всех пользователей прошедших /reg;/freg, зачем? Все еще хз
    /link - переключатель, если активирован то работает следующим оборазом
        Когда ты кидаешь мне ссылку с её обозначением, например: "Google https://google.com"; "https://gmail.com мыло", то я сохраню ссылки с данными ключами
        Если же ты не присылаешь мне никакой ссылки, а просто пишешь текст (а я жду от тебя как раз тех обозначений ссылок), то я ищу и отдаю тебе ссылку
        Ссылки персональные.
        Отключается той же командой
    /keyboard - вызывает клавиатуру с командами, пока забил на неё
        

А и всьо, чо думал я дохрена нейросеть? Не-а
"""


class User:
    name = ""
    surname = ""
    age = 0
    username = ""
    personal_links = {"": ""}

    def __init__(self, name, surname, age, username):
        self.name = name
        self.surname = surname
        self.age = age
        self.username = username

    def __str__(self):
        return self.name + " " + self.surname


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARK_CYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


bot = telebot.TeleBot("1523380614:AAG7DnONXtPhyt9YN735kI3-KHmfryerNWw")
keyboard = telebot.types.ReplyKeyboardMarkup(True, True)  # InlineKeyboardMarkup
keyboard.row("/reg", "/users", "/stick_id")


def get_random_sticker():
    return random.choice(unknown_sticker_set)


def get_name(message: Message, user: User):
    user.name = message.text
    bot.send_message(message.from_user.id, "Окей, какая у тебя фамилия?")
    bot.register_next_step_handler(message, get_surname, user)


def get_surname(message: Message, user: User):
    user.surname = message.text
    bot.send_message(message.from_user.id, "А, сколько тебе лет?")
    bot.register_next_step_handler(message, get_age, user)


def get_age(message: Message, user: User):
    age = 0
    while age == 0:
        try:
            age = int(message.text)
            user.age = age
            break
        except ValueError:
            bot.send_message(message.from_user.id, "Я только цифры знаю")
            bot.register_next_step_handler(message, get_age, user)
            return
    bot.send_message(message.from_user.id, f"Выходит ты {user.name} {user.surname} и тебе {user.age} ну крута чо. Я тебя запомню, не боись")
    user.username = message.from_user.username
    if message.from_user.first_name != user.name or message.from_user.last_name != user.surname:
        bot.send_message(message.from_user.id,
                         f'Хотя я то знаю что ты на самом деле {message.from_user.first_name} {message.from_user.last_name}, но так и быть, промолчу')
    user_list.append(user)


def split_links_and_name_and_save(message: Message, user: User):
    entities = message.entities
    text = message.text
    for entity in entities:
        if entity.type == "url":
            offset = entity.offset - (len(message.text) - len(text))
            length = entity.length
            link_name = ""
            link = ""
            # print(f"o {entity.offset}")
            # print(f"l {entity.length}")
            if offset > 0:
                link_name = text[:offset].strip()
                link = text[offset:offset + length].strip()
                text = text[offset + length:].strip()
            elif offset == 0:
                link = text[:length].strip()
                word_list = text.split(" ")
                link_name = word_list[1]
                text = text[offset + length + len(word_list[1]) + 1:].strip()
            if user is None:
                bot.send_message(message.chat.id,
                                    "Я тебя не знаю, пройди /reg, потом поговорим (сначала выключи /link)")
                break
            else:
                user.personal_links[link_name.lower()] = link
                bot.send_message(
                    chat_id=message.chat.id,
                    text=f"Добавил значение *{link_name}* для *{message.from_user.username}*, для получения ссылки введи указанное название",
                    parse_mode=ParseMode.MARKDOWN_V2
                )


def get_user_by_message(t_user):
    try:
        return filter(lambda x: x.username == t_user.username, user_list).__next__()
    except StopIteration:
        return User("", "", 0, "")


user_list = list()
# user_list.append(User("Вячеслав", "Евтеев", 21, "v4eii"))
user_list.append(User("Вячеслав", "SD", 21, "vds"))

# {
#    "content_type":"sticker",
#    "id":551,
#    "message_id":551,
#    "from_user":{
#       "id":494449240,
#       "is_bot":false,
#       "first_name":"Vyacheslav",
#       "username":"v4eii",
#       "last_name":"Evteev",
#       "language_code":"ru",
#       "can_join_groups":"None",
#       "can_read_all_group_messages":"None",
#       "supports_inline_queries":"None"
#    },
#    "date":1614378964,
#    "chat":{
#       "id":494449240,
#       "type":"private",
#       "title":"None",
#       "username":"v4eii",
#       "first_name":"Vyacheslav",
#       "last_name":"Evteev",
#       "photo":"None",
#       "bio":"None",
#       "description":"None",
#       "invite_link":"None",
#       "pinned_message":"None",
#       "permissions":"None",
#       "slow_mode_delay":"None",
#       "sticker_set_name":"None",
#       "can_set_sticker_set":"None",
#       "linked_chat_id":"None",
#       "location":"None"
#    },
#    "forward_from":"None",
#    "forward_from_chat":"None",
#    "forward_from_message_id":"None",
#    "forward_signature":"None",
#    "forward_sender_name":"None",
#    "forward_date":"None",
#    "reply_to_message":"None",
#    "edit_date":"None",
#    "media_group_id":"None",
#    "author_signature":"None",
#    "text":"None",
#    "entities":"None",
#    "caption_entities":"None",
#    "audio":"None",
#    "document":"None",
#    "photo":"None",
#    "sticker":{
#       "file_id":"CAACAgQAAxkBAAICJ2A5d9QeGrHQnRIKJofQ0YXkOIO_AAJOAgACcxpEBeniUUTkAAEyqh4E",
#       "file_unique_id":"AgADTgIAAnMaRAU",
#       "width":437,
#       "height":512,
#       "thumb":<telebot.types.PhotoSize object at 0x000002073C6084F0>,
#       "emoji":"☺️",
#       "set_name":"PepeTheFrogByAliZare",
#       "mask_position":"None",
#       "file_size":17570,
#       "is_animated":false
#    },
#    "video":"None",
#    "video_note":"None",
#    "voice":"None",
#    "caption":"None",
#    "contact":"None",
#    "location":"None",
#    "venue":"None",
#    "animation":"None",
#    "dice":"None",
#    "new_chat_member":"None",
#    "new_chat_members":"None",
#    "left_chat_member":"None",
#    "new_chat_title":"None",
#    "new_chat_photo":"None",
#    "delete_chat_photo":"None",
#    "group_chat_created":"None",
#    "supergroup_chat_created":"None",
#    "channel_chat_created":"None",
#    "migrate_to_chat_id":"None",
#    "migrate_from_chat_id":"None",
#    "pinned_message":"None",
#    "invoice":"None",
#    "successful_payment":"None",
#    "connected_website":"None",
#    "reply_markup":"None",
#    "json":{
#       "message_id":551,
#       "from":{
#          "id":494449240,
#          "is_bot":false,
#          "first_name":"Vyacheslav",
#          "last_name":"Evteev",
#          "username":"v4eii",
#          "language_code":"ru"
#       },
#       "chat":{
#          "id":494449240,
#          "first_name":"Vyacheslav",
#          "last_name":"Evteev",
#          "username":"v4eii",
#          "type":"private"
#       },
#       "date":1614378964,
#       "sticker":{
#          "width":437,
#          "height":512,
#          "emoji":"☺️",
#          "set_name":"PepeTheFrogByAliZare",
#          "is_animated":false,
#          "thumb":{
#             "file_id":"AAMCBAADGQEAAgInYDl31B4asdCdEgomh9DRheQ4g78AAk4CAAJzGkQF6eJRROQAATKqutZyMAAEAQAHbQADkyEAAh4E",
#             "file_unique_id":"AQADutZyMAAEkyEAAg",
#             "file_size":3680,
#             "width":109,
#             "height":128
#          },
#          "file_id":"CAACAgQAAxkBAAICJ2A5d9QeGrHQnRIKJofQ0YXkOIO_AAJOAgACcxpEBeniUUTkAAEyqh4E",
#          "file_unique_id":"AgADTgIAAnMaRAU",
#          "file_size":17570
#       }
#    }
# }
