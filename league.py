import requests


def get_league(league_type: str) -> str:
    response = requests.get("https://poe.ninja/api/data/getindexstate")

    for league in response.json()["economyLeagues"]:
        if league["url"] == league_type:
            return league["displayName"]


# for more league types
# see https://poe.ninja/api/data/getindexstate
league_type = "challenge"

league = get_league(league_type)
