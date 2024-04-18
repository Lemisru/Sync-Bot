from vkbottle.bot import Bot
from config import REPLY_TO

def isReplyTo(id):
    if REPLY_TO:
        return id
    else:
        return None