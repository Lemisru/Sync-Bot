from vkbottle import API
from vkbottle.bot import BotLabeler

from environs import Env

env = Env()
env.read_env()

labeler = BotLabeler()

class Config:
    VK_API = API(env('VK_TOKEN'))
    DB_FILE = env("DATABASE")
    VK_PREFIXES = env('VK_PREFIXES')

    REPLY_TO = bool(int(env('REPLY_TO')))
    config_change_lvl = env('config_change_level')
    professions_add_level = env('professions_add_level')

    def __str__(self):
        result = (
            f"Конфиг\n"
            f"  Изменение конфига: {self.config_change_lvl}-й лвл\n"
            f"Профессии\n"
            f"  Добавление профессий: {self.professions_add_level}-й лвл\n"

        )
        return result
    
