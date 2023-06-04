import league
import multiprocessing

try:
    import requests
except ImportError:
    print("you need the requests library for this script to work")
    quit()


def json_downloader(url: str) -> dict:
    r = requests.get(url)
    r.raise_for_status()
    return r.json()


def ninja_get_data(league: str) -> dict:
    baseURL = "https://poe.ninja/api/data/{}Overview?league={}&type={}"
    ninjaCurrencyTypes = ["Fragment", "Currency"]
    ninjaItemTypes = [
        "UniqueAccessory",
        "UniqueArmour",
        "UniqueFlask",
        "UniqueJewel",
        "UniqueWeapon",
        "Vial",
    ]

    urls_to_download = []
    for itemType in ninjaItemTypes:
        urls_to_download.append(baseURL.format("Item", league, itemType))
    for currencyType in ninjaCurrencyTypes:
        urls_to_download.append(baseURL.format("Currency", league, currencyType))

    dataCollection = []
    with multiprocessing.Pool(processes=len(urls_to_download)) as pool:
        for itemCategoryList in pool.imap_unordered(json_downloader, urls_to_download):
            dataCollection.extend(itemCategoryList["lines"])

    translatedItems = {}
    for item in dataCollection:
        referenceNinjaItemName = "name" if "name" in item else "currencyTypeName"
        referencePriceName = "chaosValue" if "chaosValue" in item else "chaosEquivalent"
        translatedItems[item[referenceNinjaItemName]] = item[referencePriceName]
    return translatedItems


def find_maximum_col_lengths_of_table(table: list, padding=0) -> list:
    # initialize list with n elements
    longest_column_length = [0] * len(table[0])

    for row in table:
        for column in range(len(row)):
            if len(str(row[column])) > longest_column_length[column]:
                longest_column_length[column] = len(str(row[column]))

    for i in range(len(longest_column_length)):
        longest_column_length[i] += padding

    return longest_column_length


def price_upgrade_sets(upgradeSets: list) -> list:
    ninjaItems = ninja_get_data(league.league)

    profitTable = [
        # format:
        # [investment, profit, upgrade_item, price, original, price, upgraded, price],
    ]

    for group in upgradeSets:
        upgrade_item = group[0]
        original = group[1]
        upgraded = group[2]

        try:
            investment = ninjaItems[upgrade_item] + ninjaItems[original]
            profit = ninjaItems[upgraded] - investment
        except KeyError as e:
            # item not found in ninja items
            continue

        profitTable.append(
            [
                round(profit, 2),
                round(investment, 2),
                upgrade_item,
                round(ninjaItems[upgrade_item], 2),
                original,
                round(ninjaItems[original], 2),
                upgraded,
                round(ninjaItems[upgraded], 2),
            ]
        )
    return profitTable


def print_upgrade_sets(profitTable: list) -> None:

    # sort with best profitability at the top
    _sort = lambda x: x[0]
    profitTable.sort(key=_sort, reverse=True)

    profitTable.append(
        [
            "profit",
            "investment",
            "upgrade item",
            "upgrade price",
            "original",
            "original price",
            "upgraded",
            "upgraded price",
        ]
    )

    longest_column_length = find_maximum_col_lengths_of_table(profitTable, padding=1)

    # inserting the header separator (making a markdown table)
    profitTable.insert(
        -1,
        [((len - 1) * "-") + " " for len in longest_column_length]
    )

    # reorder with best profitability at the bottom and the header at the top
    profitTable.reverse()

    for row in profitTable:
        print("| ", end="")
        for i in range(len(row)):
            endText = "| " if i != len(row) - 1 else ""
            print(
                "{0:{width}}".format(str(row[i]), width=longest_column_length[i]),
                end=endText,
            )
        print("|")
