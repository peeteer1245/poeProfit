#!/usr/bin/env python3
import util


def main():
    upgrade_sets = [
        # [Blessing, original, upgraded],
        [
            "Blessing of Chayula",
            "Chayula's Breachstone",
            "Chayula's Flawless Breachstone",
        ],
        ["Blessing of Chayula", "Eye of Chayula", "Presence of Chayula"],
        ["Blessing of Chayula", "Severed in Sleep", "United in Dream"],
        ["Blessing of Chayula", "Skin of the Loyal", "Skin of the Lords"],
        ["Blessing of Chayula", "The Blue Dream", "The Blue Nightmare"],
        ["Blessing of Chayula", "The Green Dream", "The Green Nightmare"],
        ["Blessing of Chayula", "The Red Dream", "The Red Nightmare"],
        ["Blessing of Esh", "Esh's Breachstone", "Esh's Flawless Breachstone"],
        ["Blessing of Esh", "Esh's Mirror", "Esh's Visage"],
        ["Blessing of Esh", "Hand of Thought and Motion", "Hand of Wisdom and Action"],
        ["Blessing of Esh", "Voice of the Storm", "Choir of the Storm"],
        ["Blessing of Tul", "The Halcyon", "The Pandemonius"],
        ["Blessing of Tul", "The Snowblind Grace", "The Perfect Form"],
        ["Blessing of Tul", "Tulborn", "Tulfall"],
        ["Blessing of Tul", "Tul's Breachstone", "Tul's Flawless Breachstone"],
        ["Blessing of Uul-Netol", "The Anticipation", "The Surrender"],
        ["Blessing of Uul-Netol", "The Infinite Pursuit", "The Red Trail"],
        [
            "Blessing of Uul-Netol",
            "Uul-Netol's Breachstone",
            "Uul-Netol's Flawless Breachstone",
        ],
        ["Blessing of Uul-Netol", "Uul-Netol's Kiss", "Uul-Netol's Embrace"],
        ["Blessing of Xoph", "The Formless Flame", "The Formless Inferno"],
        ["Blessing of Xoph", "Xoph's Breachstone", "Xoph's Flawless Breachstone"],
        ["Blessing of Xoph", "Xoph's Heart", "Xoph's Blood"],
        ["Blessing of Xoph", "Xoph's Inception", "Xoph's Nurture"],
    ]

    priced_upgrade_sets = util.price_upgrade_sets(upgrade_sets)

    util.print_upgrade_sets(priced_upgrade_sets)


if __name__ == "__main__":
    main()
