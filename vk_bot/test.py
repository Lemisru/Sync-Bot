from ossapi import Ossapi, UserLookupKey, GameMode, RankingType, Scope
from datetime import timedelta

client_id = 31861
client_secret = "VdJ30mY0o98t0InF5T9MyCbysRQoIi9SNLX03MbT"

scopes = [Scope.PUBLIC]
api = Ossapi(client_id, client_secret, scopes=scopes)

beatmap_id = 181255

beatmap_info = api.beatmap(beatmap_id)

map_message = (
    f"[Server: Bancho]\n"
    f"<{str(beatmap_info.status)}> {beatmap_info._beatmapset.artist} - {beatmap_info._beatmapset.title} [{beatmap_info.version}] by {beatmap_info._beatmapset.creator}\n"
    f"{timedelta(seconds=beatmap_info.total_length)} | AR:{beatmap_info.ar} CS:{beatmap_info.cs} OD:{beatmap_info.accuracy} HP:{beatmap_info.drain} BPM:{beatmap_info.bpm} | {beatmap_info.difficulty_rating}✩\n\n"

    f"Max Combo: {beatmap_info.max_combo}x({beatmap_info.count_circles}|{beatmap_info.count_sliders}|{beatmap_info.count_spinners})\n"
    #f"FC: 291.52 ⯈ SS: 420.58\n"

    f"Beatmap: {beatmap_info.url}\n"
    f"tags: {beatmap_info._beatmapset.tags}"
)

print(map_message)