import requests


def get_league(league_index: int) -> str:
    response = requests.get("https://poe.ninja/api/data/getindexstate")
    return response.json()["economyLeagues"][league_index]["displayName"]


# for more league types
# see https://poe.ninja/api/data/getindexstate
# the first entry is always SC Temp-league with index 0
# the second is always HC Temp-league with index 1 and so on
league_index = 0

league = get_league(league_index)
