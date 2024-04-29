from config import Config

def isReplyTo(id):
    if Config().REPLY_TO:
        return id
    else:
        return None