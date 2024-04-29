from vkbottle.bot import BotLabeler

from vk_bot.AsyaCommandRule import AsyaCommandRule
from config import Config
from data import database
from vk_bot.isReplyTo import isReplyTo

import random

others_labeler = BotLabeler()

@others_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["помощь", "команды"]))
async def help_handler(message):
    answer =  "⚙ Полный список команд доступен по ссылке: https://vk.com/@async_bot-commands"
    await message.answer(answer, reply_to=isReplyTo(message.id))

@others_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["ник <name>", "имя <name>"]))
async def nick_handler(message, name):
   database.update_user(message.from_id, name=name)
   await message.answer(f"Ник успешно изменён на {name}! Урааааа", reply_to=isReplyTo(message.id))

@others_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, "пинг"))
async def pong_handler(message):
    await message.answer("понг", reply_to=isReplyTo(message.id))

@others_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["скажи <text>","повтори <text>"]))
async def say_handler(message, text):
    await message.answer(text)

@others_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["сделай русским <text>","русский <text>"]))
async def zov_handler(message, text):
    new_text = text.replace('з', 'Z')
    new_text = new_text.replace('в', 'V')
    new_text = new_text.replace('З', 'Z')
    new_text = new_text.replace('В', 'V')

    await message.answer(new_text, reply_to=isReplyTo(message.id))

@others_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["данет <text>","магический шар <text>"]))
async def magic_ball_handler(message, text):
   phrases = ["Вероятно да", "Вероятно нет", "Да", "Нет", "Возможно", "Скорее всего нет",
              "Скорее всего да", "Маловероятно","Шансы есть","Шансов нет","Повтори позже"]
   
   await message.answer(random.choice(phrases), reply_to=isReplyTo(message.id))

@others_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["данет <text>","магический шар <text>"]))
async def magic_ball_handler(message, text):
   phrases = ["Вероятно да", "Вероятно нет", "Да", "Нет", "Возможно", "Скорее всего нет",
              "Скорее всего да", "Маловероятно","Шансы есть","Шансов нет","Повтори позже"]
   
   await message.answer(f"🎲{random.choice(phrases)}", reply_to=isReplyTo(message.id))

@others_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["выбери число от <num1:int> до <num2:int>", "число от <num1:int> до <num2:int>"]))
async def random_number_handler(message, num1, num2):
   new_number = random.randint(num1,num2)
   await message.answer(f"🎲Число: {new_number}", reply_to=isReplyTo(message.id))

@others_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["выбери из <text>", "фраза из <text>",
                                                      "выбери слово из <text>", "выбери из перечисленного: <text>"]))
async def phrase_choice_handler(message, text):
   new_text = text.split(",")
   await message.answer(f"Я выберу: {random.choice(new_text)}", reply_to=isReplyTo(message.id))

@others_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ["<action>ть из <text>", "фраза из <text>",
                                                      "выбери слово из <text>", "выбери из перечисленного: <text>"]))
async def phrase_choice_handler(message, text):
   new_text = text.split(",")
   await message.answer(f"Я выберу: {random.choice(new_text)}", reply_to=isReplyTo(message.id))






