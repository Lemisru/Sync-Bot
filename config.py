from vkbottle import API, BuiltinStateDispenser
from vkbottle.bot import BotLabeler

import configparser

config_parser = configparser.ConfigParser()
config_parser.read("config.ini")

API = API(config_parser["VK"]["Token"])
VK_PREFIXES = config_parser["VK"]["Prefixes"]
REPLY_TO = bool(int((config_parser["VK"]["Reply_to"])))

labeler = BotLabeler()
state_dispenser = BuiltinStateDispenser() #не разобрался для чегоы
