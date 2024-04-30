from vkbottle import API
from vkbottle.bot import BotLabeler

from environs import Env

env = Env()
env.read_env()

labeler = BotLabeler()

class Config():
    VK_API = API(env('VK_TOKEN'))
    DB_FILE = env("DATABASE")
    VK_PREFIXES = env('VK_PREFIXES')

    REPLY_TO = bool(int(env('REPLY_TO')))

    permissions = {
        'config_change' : int(env('config_change_level')),
        'professions' : {
            'add': int(env('professions_add_level'))
        }
    }

    def __str__(self):
        nums = ["\u0031\u20E3", "\u0032\u20E3", 
                "\u0033\u20E3", "\u0034\u20E3", "\u0035\u20E3"]
        result = (
            f"🗓 Дерево Разрешений\n"
            f"⚙️▶ Изменение разрешений: {nums[self.permissions['config_change']-1]}\n"
            f"🗂️* Профессии\n"
            f"⚙️▶ Добавление профессий: {nums[self.permissions['professions']['add']-1]}\n"
        )

        return result
    
