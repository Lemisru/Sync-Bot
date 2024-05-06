import vk_bot.handlers.admin as admin

import vk_bot.handlers.reactions as reactions
import vk_bot.handlers.articles as articles
import vk_bot.handlers.professions as professions
import vk_bot.handlers.others as others
import vk_bot.handlers.chat_actions as chat_actions
#import vk_bot.handlers.chatgpt as chatgpt
import vk_bot.handlers.osu as osu

from config import labeler

labeler.load(admin.admin_labeler)

labeler.load(reactions.reactions_labeler)
labeler.load(professions.professions_labeler)
labeler.load(articles.articles_labeler)
labeler.load(others.others_labeler)
labeler.load(chat_actions.chat_actions_labeler)
#labeler.load(chatgpt.chatgpt_labeler)
labeler.load(osu.osu_labeler)