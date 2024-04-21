from vkbottle.dispatch.rules.base import CommandRule
from vkbottle.bot import BotLabeler

from config import VK_PREFIXES
from vk_bot.isReplyTo import isReplyTo

others_labeler = BotLabeler()

@others_labeler.message(CommandRule("помощь", VK_PREFIXES))
async def others_handler(message):
    answer =  "⚙ Полный список команд доступен по ссылке: https://vk.com/@async_bot-commands"
    await message.answer(answer, reply_to=isReplyTo(message.id))

@others_labeler.message(CommandRule("пинг", VK_PREFIXES))
async def others_handler(message):
    await message.answer("понг", reply_to=isReplyTo(message.id))

@others_labeler.message(CommandRule("скажи", VK_PREFIXES, 1))
async def others_handler(message, *args: tuple):
    await message.answer(' '.join(args))