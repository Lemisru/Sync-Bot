from config import Config
from data import database

def isReplyTo(id):
    if Config().REPLY_TO:
        return id
    else:
        return None
    
def getPing(message, user):
    user = database.users.get_chat_user_info(message.chat_id, message.from_id)
    if user is None:
        name = f"{user[0].first_name} {user[0].last_name}"
    else:
        name = user.name
    return f"[id{message.from_id}|{name}]"
    