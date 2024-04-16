from vkbottle.bot import Bot, Message

vk_bot = Bot(token="vk1.a.dkCEjRRMYDPph6xGc5icm2sx_5ufoX_RKMF3GuJBfYQV1bDQnc5Qvm0OTD_qX-lT2brnPQ4Yq_lr7kJfAU_iq-8oeqcFfMQ1BCK_DmzZqRjCFq1stMwMTAachvzPkDSxyfvP-lm5RZwH8TxFTN-qZ9ljey4WmnQ3ZILwfJ2nXcWH4CrQ55suGB_oE9X6twpdTnB_I3xdRzzCFTdSWQZ19Q")

@vk_bot.on.private_message()
async def echo_answer(message: Message):
    if message.text.lower() == "начать":
        await message.answer("Здарова")

if __name__ == "__main__":
    vk_bot.run_forever()