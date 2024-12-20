
import re

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    '''
    checkout function
    '''
    if not isinstance(skus, str): return -1
    if len(skus) == 0: return 0


    (sku_count_map, 
    sku_price_map, 
    sku_discount_map, 
    sku_buy_two_get_one_free_map) = __create_checkout_maps()
    # #map to keep count of how many items are in the SKU string
    # sku_count_map: dict[str : int] = {
    #     'A': 0,
    #     'B': 0,
    #     'C': 0,
    #     'D': 0,
    #     'E': 0,
    #     'F': 0
    # }

    for sku_char in skus:
        if sku_char not in sku_count_map: return -1
        sku_count_map[sku_char] += 1

    # #map of normal prices for all SKUs
    # sku_price_map: dict[str : int] = {
    #     'A': 50,
    #     'B': 30,
    #     'C': 20,
    #     'D': 15,
    #     'E': 40,
    #     'F': 10
    # }

    # #discounts are in the format of (numbe_of_items, discount_price)
    # sku_discount_map: dict[str : list[tuple[int, int]]] = {
    #     'A': [(5, 200), (3, 130)],
    #     'B': [(2, 45)],
    #     'C': [],
    #     'D': [],
    #     'E': [],
    #     'F': []
    # }

    # sku_buy_two_get_one_free_map: dict[str : str] = {
    #     'A': None,
    #     'B': None,
    #     'C': None,
    #     'D': None,
    #     'E': ('B', 2),
    #     'F': ('F', 2)
    # }

    #calculate remaining count after buy one get one free discounts
    for sku in sku_buy_two_get_one_free_map:
        if sku_buy_two_get_one_free_map[sku] == None: continue
        free_item, number_bought = sku_buy_two_get_one_free_map[sku]
        sku_count_map = __calculate_buy_one_get_one_free(sku_count_map, sku, free_item, number_bought)

    #iterate through checkout prices and calculate discounts
    total_checkout_price = 0
    for sku in sku_count_map:
        total_checkout_price += __calculate_price_of_item_with_discounts(sku_count_map, sku_price_map, sku_discount_map[sku], sku)

    return total_checkout_price


def __calculate_buy_one_get_one_free(sku_count_map: dict[str : int], bought_item_sku: str, free_item_sku: str, multiple: int) -> dict[str : int]:
    '''
    calculates how many free items can be removed based on how many items were bought with buy two get one free discount
    '''
    amount_multiple = multiple + 1 if bought_item_sku == free_item_sku else multiple
    count_bought_item = sku_count_map[bought_item_sku]
    count_free_item = count_bought_item // amount_multiple
    sku_count_map[free_item_sku] = max(0, sku_count_map[free_item_sku] - count_free_item)
    
    return sku_count_map


def __calculate_price_of_item_with_discounts(sku_count_map: dict[str : int], sku_price_map: dict[str : int], discounts: list[tuple[int, int]], item: str) -> int:
    '''
    returns an new price with discount
    '''
    count_of_item = sku_count_map[item]

    total_price_item = 0

    for number, offer_price in discounts:
        total_price_item += (count_of_item // number) * offer_price
        count_of_item = count_of_item % number

    total_price_item += count_of_item * sku_price_map[item]

    return total_price_item


def __create_checkout_maps() -> tuple[dict[str : int], dict[str : int], dict[str : list[tuple[int, int]]], dict[str : str]]:
    '''
    reads in a table string and returns the 4x maps used in the checkout function
    the maps returned are in the following order (as a tuple):
        1) sku_count_map
        2) sku_price_map
        3) sku_discount_map
        4) sku_buy_two_get_one_free_map
    '''

    table = '''
    +------+-------+------------------------+
    | Item | Price | Special offers         |
    +------+-------+------------------------+
    | A    | 50    | 3A for 130, 5A for 200 |
    | B    | 30    | 2B for 45              |
    | C    | 20    |                        |
    | D    | 15    |                        |
    | E    | 40    | 2E get one B free      |
    | F    | 10    | 2F get one F free      |
    | G    | 20    |                        |
    | H    | 10    | 5H for 45, 10H for 80  |
    | I    | 35    |                        |
    | J    | 60    |                        |
    | K    | 80    | 2K for 150             |
    | L    | 90    |                        |
    | M    | 15    |                        |
    | N    | 40    | 3N get one M free      |
    | O    | 10    |                        |
    | P    | 50    | 5P for 200             |
    | Q    | 30    | 3Q for 80              |
    | R    | 50    | 3R get one Q free      |
    | S    | 30    |                        |
    | T    | 20    |                        |
    | U    | 40    | 3U get one U free      |
    | V    | 50    | 2V for 90, 3V for 130  |
    | W    | 20    |                        |
    | X    | 90    |                        |
    | Y    | 10    |                        |
    | Z    | 50    |                        |
    +------+-------+------------------------+
    '''
    sku_count_map: dict[str : int] = {}
    sku_price_map: dict[str : int] = {}
    sku_discount_map: dict[str : list[tuple[int, int]]] = {}
    sku_buy_two_get_one_free_map: dict[str : str] = {}

    for line in table.splitlines():
        match = re.match(r"\| (\w+) +\| (\d+) +\| (.*?) *\|", line)
        if match:
            sku = match.group(1)
            print(sku)
            price = int(match.group(2))
            offers = match.group(3).strip()

            sku_count_map[sku] = 0
            sku_price_map[sku] = price

            discounts = []
            if 'for' in offers:
                for discount in re.findall(r"(\d+)(\w) for (\d+)", offers):
                    quantity, item, discount_price = discount
                    if item == sku:
                        discounts.append((int(quantity), int(discount_price)))
            sorted_discounts = sorted(discounts, key=lambda x: x[1], reverse=True)
            sku_discount_map[sku] = sorted_discounts

            free_offer_match = re.search(r"(\d+)(\w) get one (\w) free", offers)
            if free_offer_match:
                quantity_required = int(free_offer_match.group(1)[:-1])
                target_sku = free_offer_match.group(3)
                sku_buy_two_get_one_free_map[sku] = (target_sku, quantity_required)
            else:
                sku_buy_two_get_one_free_map[sku] = None
    print(sku_count_map)
    return (sku_count_map, sku_price_map, sku_discount_map, sku_buy_two_get_one_free_map)











