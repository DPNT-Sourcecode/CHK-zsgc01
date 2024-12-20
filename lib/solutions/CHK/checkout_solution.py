

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    '''
    checkout function
    '''
    if not isinstance(skus, str): return -1
    if len(skus) == 0: return 0

    #map to keep count of how many items are in the SKU string
    sku_count_map: dict[str : int] = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0,
        'F': 0
    }

    for sku_char in skus:
        if sku_char not in sku_count_map: return -1
        sku_count_map[sku_char] += 1

    #map of normal prices for all SKUs
    sku_price_map: dict[str : int] = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15,
        'E': 40,
        'F': 10
    }

    #discounts are in the format of (numbe_of_items, discount_price)
    sku_discount_map: dict[str : list[tuple[int, int]]] = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'C': [],
        'D': [],
        'E': [],
        'F': []
    }

    sku_buy_two_get_one_free_map: dict[str : str] = {
        'A': '',
        'B': '',
        'C': '',
        'D': '',
        'E': 'B',
        'F': 'F'
    }

    #calculate remaining count after buy one get one free discounts
    for sku in sku_buy_two_get_one_free_map:
        if len(sku_buy_two_get_one_free_map[sku]) == 0: continue
        sku_count_map = __calculate_buy_one_get_one_free(sku_count_map, sku, sku_buy_two_get_one_free_map[sku])

    #iterate through checkout prices and calculate discounts
    total_checkout_price = 0
    for sku in sku_count_map:
        total_checkout_price += __calculate_price_of_item_with_discounts(sku_count_map, sku_price_map, sku_discount_map[sku], sku)

    return total_checkout_price


def __calculate_buy_one_get_one_free(sku_count_map: dict[str : int], bought_item_sku: str, free_item_sku: str) -> dict[str : int]:
    '''
    calculates how many free items can be removed based on how many items were bought with buy two get one free discount
    '''
    amount_multiple = 3 if bought_item_sku == 'F' else 2
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



