from vkbottle.bot import BotLabeler

from vk_bot.AsyaCommandRule import AsyaCommandRule
from config import VK_PREFIXES
from vk_bot.isReplyTo import isReplyTo

others_labeler = BotLabeler()

@others_labeler.message(AsyaCommandRule(VK_PREFIXES, ["помощь", "команды"]))
async def others_handler(message):
    answer =  "⚙ Полный список команд доступен по ссылке: https://vk.com/@async_bot-commands"
    await message.answer(answer, reply_to=isReplyTo(message.id))

@others_labeler.message(AsyaCommandRule(VK_PREFIXES, "пинг"))
async def others_handler(message):
    await message.answer("понг", reply_to=isReplyTo(message.id))

@others_labeler.message(AsyaCommandRule(VK_PREFIXES, ["скажи <text>","повтори <text>"]))
async def others_handler(message, text):
    await message.answer(text)