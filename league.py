import argparse
import requests


def get_league(league_index: int) -> str:
    # for more league types
    # see https://poe.ninja/api/data/getindexstate
    # the first entry is always SC Temp-league with index 0
    # the second is always HC Temp-league with index 1 and so on
    response = requests.get("https://poe.ninja/api/data/getindexstate")
    return response.json()["economyLeagues"][league_index]["displayName"]


def add_parser_league_arguments(
    parser: argparse.ArgumentParser,
) -> argparse.ArgumentParser:
    league_group = parser.add_argument_group("league selector")

    league_group.add_argument(
        "--standard", action="store_const", dest="league_index", const=4
    )
    league_group.add_argument(
        "--hardcore", action="store_const", dest="league_index", const=5
    )
    league_group.add_argument(
        "--temp", action="store_const", dest="league_index", const=0
    )
    league_group.add_argument(
        "--temp-hc", action="store_const", dest="league_index", const=1
    )
