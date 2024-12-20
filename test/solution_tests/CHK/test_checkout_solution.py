
from lib.solutions.CHK import checkout_solution

class TestCheckoutSuite():
    '''
    suite for testing checkout solution
    '''

    def test_checkout_without_offers(self) -> None:
        '''
        test the checkout method
        '''
        #test normal behaviour without any applicable special offers
        test_sku_string_no_offer: str = 'ABCDE'
        actual_checkout_value_no_offer = checkout_solution.checkout(test_sku_string_no_offer)
        expected_checkout_value_no_offer = 50 + 30 + 20 + 15 + 40
        assert actual_checkout_value_no_offer == expected_checkout_value_no_offer


    def test_checkout_with_single_offers(self) -> None:
        '''
        test checkout where single offers are applicable
        '''
        #test behaviour when special offers apply
        test_sku_string_with_offer_a: str = 'ABAACD'
        actual_checkout_value_with_offer = checkout_solution.checkout(test_sku_string_with_offer_a)
        expected_checkout_value_with_offer = 130 + 30 + 20 + 15
        assert actual_checkout_value_with_offer == expected_checkout_value_with_offer

        #test behaviour when special offers apply
        test_sku_string_with_offer_b: str = 'ABBACD'
        actual_checkout_value_with_offer_2 = checkout_solution.checkout(test_sku_string_with_offer_b)
        expected_checkout_value_with_offer_2 = 50 + 50 + 45 + 20 + 15
        assert actual_checkout_value_with_offer_2 == expected_checkout_value_with_offer_2

    def test_checkout_with_multiple_offers(self) -> None:
        '''
        test checkout where multiple offers are applicable
        '''

        test_sku_string_with_multle_special_orders_a = 'AAABAAAAACAAACAAD'
        actual_checkout_value_with_multiple_offer_a = checkout_solution.checkout(test_sku_string_with_multle_special_orders_a)
        
        #total of 13 As, 1 B, 2 C and 1 D
        expected_checkout_value_a = 200 + 130 + 130 + (2 * 50) + 2 * 20 + 30 + 15

        test_sku_string_with_get_one_b_free_1 = 'EEB'
        actual_buy_one_get_one_free_value_1 = checkout_solution.checkout(test_sku_string_with_get_one_b_free_1)


        test_sku_string_with_get_one_b_free_2 = 'EEBB'
        act


    def test_checkout_illegal_arguments(self) -> None:
        '''
        test illegal argument inputs
        '''
        #test behaviour with illegal arguments
        test_illegal_number_arg = 0
        actual_checkout_value_with_number_arg = checkout_solution.checkout(test_illegal_number_arg)
        assert actual_checkout_value_with_number_arg == -1

        #test illegal SKU value
        test_illegal_sku = 'AXVB'
        actual_checkout_value_with_illegal_sku_value = checkout_solution.checkout(test_illegal_sku)
        assert actual_checkout_value_with_illegal_sku_value == -1


    def test_checkout_empty_order(self) -> None:
        '''
        test an empty checkout sku string
        '''
        #test empty string
        actual_checkout_value_with_empty_string = checkout_solution.checkout('')
        assert actual_checkout_value_with_empty_string == 0














