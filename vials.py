#!/usr/bin/env python3
import argparse
import util
import league


def main():
    parser = argparse.ArgumentParser()
    league.add_parser_league_arguments(parser)
    args = parser.parse_args()
    if args.league_index is None:
        # set default league to temp softcore
        args.league_index = 0

    league_name = league.get_league(args.league_index)

    print(f"League: {league_name}")
    print()

    upgrade_sets = [
        # [vial, original, upgraded],
        ["test", "entry", ":)"],
        ["Vial of Awakening", "Apep's Slumber", "Apep's Supremacy"],
        ["Vial of Consequence", "Coward's Chains", "Coward's Legacy"],
        ["Vial of Dominance", "Architect's Hand", "Slavedriver's Hand"],
        ["Vial of Fate", "Story of the Vaal", "Fate of the Vaal"],
        [
            "Vial of Summoning",
            "Mask of the Spirit Drinker",
            "Mask of the Stitched Demon",
        ],
        ["Vial of the Ritual", "Dance of the Offered", "Omeyocan"],
        ["Vial of Transcendence", "Tempered Spirit", "Transcendent Spirit"],
        ["Vial of Transcendence", "Tempered Mind", "Transcendent Mind"],
        ["Vial of Transcendence", "Tempered Flesh", "Transcendent Flesh"],
        ["Vial of Sacrifice", "Sacrificial Heart", "Zerphi's Heart"],
        ["Vial of the Ghost", "Soul Catcher", "Soul Ripper"],
    ]

    priced_upgrade_sets = util.price_upgrade_sets(upgrade_sets, league)

    util.print_upgrade_sets(priced_upgrade_sets)


if __name__ == "__main__":
    main()
