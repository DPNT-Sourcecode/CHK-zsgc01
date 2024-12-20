

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    '''
    Our price table and offers: 
    +------+-------+----------------+
    | Item | Price | Special offers |
    +------+-------+----------------+
    | A    | 50    | 3A for 130     |
    | B    | 30    | 2B for 45      |
    | C    | 20    |                |
    | D    | 15    |                |
    +------+-------+----------------+
    '''
    if not isinstance(skus, str): return -1
    if len(skus) == 0: return 0

    #map to keep count of how many items are in the SKU string
    sku_count_map: dict[str : int] = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0,
        'E': 0
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
        'E': 40
    }

    sku_discount_map: dict[str : list[tuple[int, int]]] = {
        'A': [(5, 200), (3, 130)],
        'B': [(2, 45)],
        'C': [],
        'D': [],
        'E': []
    }

    #calculate total price of A with discounts included
    number_of_item_a_at_normal_price = sku_count_map['A'] % 3
    number_of_discounted_item_a = sku_count_map['A'] // 3
    total_price_a = (number_of_item_a_at_normal_price * sku_price_map['A']) + (number_of_discounted_item_a * 130)

    #calculate total price of b with discounts included
    number_of_item_b_at_normal_price = sku_count_map['B'] % 2
    number_of_discounted_item_b = sku_count_map['B'] // 2
    total_price_b = (number_of_item_b_at_normal_price * sku_price_map['B']) + (number_of_discounted_item_b * 45)

    #no discounts for sku c and d
    total_price_c = sku_count_map['C'] * sku_price_map['C']
    total_price_d = sku_count_map['D'] * sku_price_map['D']

    return total_price_a + total_price_b + total_price_c + total_price_d


def __calculate_buy_one_get_one_free(sku_count_map: dict[str : int]) -> dict[str : int]:
    '''
    calculates how many B items can be removed based on how many E's were bought
    '''
    count_e = sku_count_map['E']
    count_free_b = count_e // 2

def __calculate_price_of_item_with_discounts(sku_count_map: dict[str : int], sku_price_map: dict[str : int], discounts: list[tuple[int, int]], item: str) -> int:
    '''
    returns an new price with discount
    '''
    count_of_item = sku_count_map[item]

    total_price_item = 0

    for number, offer_price in discounts:
        total_price_item += count_of_item // number * offer_price
        count_of_item %= number

    total_price_item += count_of_item * sku_price_map[item]

    return total_price_item









