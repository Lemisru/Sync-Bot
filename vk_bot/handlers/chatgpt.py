from vk_bot.AsyaCommandRule import AsyaCommandRule
from vkbottle.bot import BotLabeler

from config import Config
from vk_bot.isReplyTo import isReplyTo
import vk_bot.vk as vk

from g4f.client import Client

client = Client()

chatgpt_labeler = BotLabeler()

@chatgpt_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["запрос <text>"]))
async def chatgpt_handler(message, text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": text}]
    )

    answer = response.choices[0].message.content

    await message.answer(answer, reply_to=isReplyTo(message.id))


@chatgpt_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["история"]))
async def chatgpt_emoji_handler(message):
    global madlibs_history
    bot = vk.getBot()

    madlibs_history = [{"role": "user", "content": 
                      ("Давай поиграем в MadLibs на русском языке"
                       "Попроси написать для меня слова по списку, а ты по ним составишь большую интересную историю")}]
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=madlibs_history
    )
    answer = response.choices[0].message.content
    madlibs_history.append({"role": "assistant", "content": answer})

    await message.answer(answer, reply_to=isReplyTo(message.id))

@chatgpt_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["ответ <text>"]))
async def chatgpt_ladder_answer_handler(message, text):
    global madlibs_history
    madlibs_history.append({"role": "user", "content": text})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=madlibs_history
    )
    answer = response.choices[0].message.content
    await message.answer(answer, reply_to=isReplyTo(message.id))
    madlibs_history.append({"role": "assistant", "content": answer})