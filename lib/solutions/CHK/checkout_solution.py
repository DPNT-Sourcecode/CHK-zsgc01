

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
    if len(skus) == 0: return -1

    sku_count_map: dict[str : int] = {
        'A': 0,
        'B': 0,
        'C': 0,
        'D': 0
    }

    for sku_char in skus:
        if sku_char not in sku_count_map: return -1
        sku_count_map[sku_char] += 1

    sku_price_map: dict[str : int] = {
        'A': 50,
        'B': 30,
        'C': 20,
        'D': 15
    }

    number_of_item_a_at_normal_price = sku_count_map['A'] % 3
    number_of_discounted_item_a = sku_count_map['A'] // 3
    total_price_a = (number_of_item_a_at_normal_price * sku_price_map['A']) + (number_of_discounted_item_a * 130)

    number_of_item_b_at_normal_price = sku_count_map['B'] % 3
    number_of_discounted_item_b = sku_count_map['B'] // 3
    total_price_b = (number_of_item_b_at_normal_price * sku_price_map) + (number_of_discounted_item_b * 45)

    total_price_c = sku_count_map['C'] * 20
    total_price_d = sku_count_map['D'] * 15

    return total_price_a + total_price_b + total_price_c + total_price_d








