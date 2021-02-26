import random

unknown_sticker_set = ("CAACAgIAAxkBAAMxYDlil77mhgAB039EtvdMzGfeV6kdAAI0AwACEzmPEQ7-6IMS7E4GHgQ",
                       "CAACAgIAAxkBAAMzYDli4ePAI0LosSVz0gRCYaYwL5oAAjQDAAITOY8RDv7ogxLsTgYeBA",
                       "CAACAgIAAxkBAAM1YDli8jq1N2CrxwyWcrNzNqkySuUAAjMDAAITOY8RDWg_z_V_7LQeBA",
                       "CAACAgIAAxkBAAM3YDljHjNTSpmbJH4N2n0G1xmtNV0AAq0AA2iaXQxHbhn9BZwe4B4E",
                       "CAACAgIAAxkBAAM7YDljUJSlWNgDOO_pajfjuYIxmOsAAgcDAAITOY8RmyC1aplqaj0eBA")

help_text = """
Короче чо могу

    /stick_id - переключатель, если активирован я верну тебе id стикера который ты мне пришлешь, отключается так же
    /reg - приколюха типа "А кто ты такой?", зачем? Незнаю. Может позже прикручу БД
    /users - показать всех пользователей прошедших /reg, зачем? Ах да, уже было

А и всьо, чо думал я дохрена нейросеть? Не-а
"""

user_list = list()


class User:
    name = ""
    surname = ""
    age = ""
    personal_links = {"": ""}

    def __str__(self):
        return self.name + " " + self.surname


def get_random_sticker():
    return random.choice(unknown_sticker_set)


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