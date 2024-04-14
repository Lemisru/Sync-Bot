from vkbottle.bot import Bot, Message

vk_bot = Bot("token")

vk_bot.on.private_message(text="<msg>")
async def echo_answer(ans: Message, msg):
    await ans.answer("Ты написал: %s"%(msg))

if __name__ == "__main__":
    vk_bot.run_forever()