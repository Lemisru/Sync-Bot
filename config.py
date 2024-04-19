from vkbottle import API
from vkbottle.bot import BotLabeler

import configparser

config_parser = configparser.ConfigParser()
labeler = BotLabeler()

config_parser.read("config.ini")

API = API(config_parser["VK"]["token"])
VK_PREFIXES = config_parser["VK"]["prefixes"]
REPLY_TO = bool(int((config_parser["VK"]["reply_to"])))
PROFESSIONS = config_parser["VK"]["professions"]
REACTIONS = config_parser["VK"]["reactions"]
ARTICLES = config_parser["VK"]["articles"]