

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

    total_checkout_value = 0

    






