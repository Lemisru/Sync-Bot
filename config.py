from vkbottle import API
from vkbottle.bot import BotLabeler

from environs import Env

env = Env()
env.read_env()

labeler = BotLabeler()

class Config():
    """Class for managing configuration settings.
    
    Parameters
    ----------
    VK_API (API): VK Bot API token.
    DB_FILE (str): Database file path.
    VK_PREFIXES (str): Prefixes for VK Bot commands.
    REPLY_TO (bool): Will the bot respond to messages.
    permissions (dict): Dictionary of permissions levels for different actions.
        'config_change' (int): Level for changing configuration settings.
        'professions' (dict): Dictionary of permissions for module professions.
            'add' (int): Add a profession.

    Methods
    ----------
    str: Returns the permissions tree string
    """
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
    
