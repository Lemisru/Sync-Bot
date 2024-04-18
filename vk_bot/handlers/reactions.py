from vkbottle.dispatch.rules.base import CommandRule
from vkbottle.bot import BotLabeler

from config import VK_PREFIXES
from vk_bot.isReplyTo import isReplyTo

reactions_labeler = BotLabeler()

@reactions_labeler.message(CommandRule("реакция", VK_PREFIXES))
async def reactions_handler(message):
    await message.answer(sticker_id=2, reply_to=isReplyTo(message.id))
