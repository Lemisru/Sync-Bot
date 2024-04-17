from vkbottle.bot import Message, BotLabeler
from vkbottle.dispatch.rules.base import CommandRule

if __name__ == "__main__":
    import os, sys
    project_directory = os.path.abspath(os.path.join(os.path.dirname(__file__), "..."))
    sys.path.append(project_directory)

from config import VK_PREFIXES, labeler
from isReplyTo import isReplyTo

reactions_labeler = BotLabeler()

@reactions_labeler.message(CommandRule("реакция", VK_PREFIXES))
async def reactions_handler(message: Message):
    await message.answer(sticker_id=1, reply_to=isReplyTo(message.id))
