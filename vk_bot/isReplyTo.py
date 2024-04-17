from vkbottle.bot import Bot

if __name__ == "__main__":
    import os, sys
    project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    sys.path.append(project_directory)

from config import REPLY_TO

def isReplyTo(id):
    if REPLY_TO:
        return id
    else:
        return None