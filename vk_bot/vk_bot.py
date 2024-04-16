from vkbottle.bot import Bot, Message

TOKEN="vk1.a.dkCEjRRMYDPph6xGc5icm2sx_5ufoX_RKMF3GuJBfYQV1bDQnc5Qvm0OTD_qX-lT2brnPQ4Yq_lr7kJfAU_iq-8oeqcFfMQ1BCK_DmzZqRjCFq1stMwMTAachvzPkDSxyfvP-lm5RZwH8TxFTN-qZ9ljey4WmnQ3ZILwfJ2nXcWH4CrQ55suGB_oE9X6twpdTnB_I3xdRzzCFTdSWQZ19Q"
bot = Bot(token=TOKEN)

@bot.on.message(text="Привет")
async def hi_handler(message: Message):
    users_info = await bot.api.users.get(message.from_id)
    await message.answer("Привет, {}".format(users_info[0].first_name))

bot.run_forever()