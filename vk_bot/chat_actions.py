from vk_bot.AsyaCommandRule import AsyaCommandRule
from vkbottle.dispatch.rules.base import ChatActionRule
from vkbottle.bot import BotLabeler

from config import VK_PREFIXES
from vk_bot.isReplyTo import isReplyTo

import random

chat_actions_labeler = BotLabeler()

@chat_actions_labeler.message(ChatActionRule("chat_invite_user"), ChatActionRule("chat_invite_user_by_link"))
async def user_join_handler(message):
    await message.answer("Ааа хохлы понаехали")

@chat_actions_labeler.message(ChatActionRule("chat_kick_user"))
async def user_kick_handler(message):
    await message.answer("Оооой, кого-то нахуй выкинули(((")