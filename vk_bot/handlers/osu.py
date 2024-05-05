from vk_bot.AsyaCommandRule import AsyaCommandRule
from vkbottle.bot import BotLabeler

from config import Config
from vk_bot.isReplyTo import isReplyTo

from ossapi import Ossapi, Scope

osu_labeler = BotLabeler()

client_id = 31861
client_secret = "VdJ30mY0o98t0InF5T9MyCbysRQoIi9SNLX03MbT"

scopes = [Scope.PUBLIC]
api = Ossapi(client_id, client_secret, scopes=scopes)

@osu_labeler.message(AsyaCommandRule(Config().VK_PREFIXES, ['топ <count:int> <id> +<mods>', 'топ <count:int> <id>']))
async def professions_add_handler(message, count: int, id: str, mods: str=None):
    if "http" in id:
        id = id.split("/")[-1]

    beatmap_info = api.beatmap(id)
    beatmapset = beatmap_info._beatmapset
    beatmap_scores = api.beatmap_scores(id, mods=mods, limit=count+1)

    answer = (f"Топ {count} на карте: \n"
              f"{beatmapset.artist} - {beatmapset.title} [{beatmap_info.version}] by {beatmapset.creator} +{mods}\n\n"
    )

    for num, score in enumerate(beatmap_scores.scores[1::]):
        answer += (
            f"#{num+1} {score._user.username} | {score.score} | "
            f"{score.max_combo}x/{beatmap_info.max_combo}x | {round(score.accuracy*100, 2)}% | "
            f"{score.statistics.count_miss} misses | {round(score.pp, 2)}pp +{score.mods} | "
            f"{score.created_at.strftime('%H:%M:%S %d.%m.%Y')}\n"
        )

    await message.answer(answer, reply_to=isReplyTo(message.id))

#top = api.beatmap_scores(847313, mode=GameMode.OSU, mods="EZDT", limit=1)
