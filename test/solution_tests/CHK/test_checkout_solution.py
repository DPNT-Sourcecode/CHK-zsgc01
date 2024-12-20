
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
        test_sku_string_with_multle_special_orders_a = 'AAABAAAAACACD'
        actual_checkout_value_with_multiple_offer_a = checkout_solution.checkout(test_sku_string_with_multle_special_orders_a)
        
        #total of 9 As, 1 B, 2 C and 1 D
        expected_checkout_value_a = 200 + 130  + 50 + (2 * 20) + 30 + 15
        assert actual_checkout_value_with_multiple_offer_a == expected_checkout_value_a


    def test_buy_two_get_one_free_offers(self) -> None:
        '''
        test buy two get one free offers
        '''
        #make sure b is free
        test_sku_string_with_get_one_b_free_1 = 'EEB'
        actual_buy_one_get_one_free_value_1 = checkout_solution.checkout(test_sku_string_with_get_one_b_free_1)
        expected_value_a = 40 * 2
        assert actual_buy_one_get_one_free_value_1 == expected_value_a

        #make sure one b is free and B's discount not applied
        test_sku_string_with_get_one_b_free_2 = 'EEBB'
        actual_buy_one_get_one_free_value_2 = checkout_solution.checkout(test_sku_string_with_get_one_b_free_2)
        expected_value_b = (40 * 2) + 30
        assert actual_buy_one_get_one_free_value_2 == expected_value_b

        #make sure buy two get one free discount applies to F
        test_f_discount_string = 'FFF'
        actual_f_discount_amount = checkout_solution.checkout(test_f_discount_string)
        expected_value_f = 20
        assert expected_value_f == actual_f_discount_amount

        test_discount_string_2 = 'FFFF'
        actual_f_discount_amount_2 = checkout_solution.checkout(test_discount_string_2)
        expected_value_f_2 = 30
        assert expected_value_f_2 == actual_f_discount_amount_2

        test_discount_string_3 = 'FFFFFF'
        actual_f_discount_amount_3 = checkout_solution.checkout(test_discount_string_3)
        expected_value_f_3 = 40
        assert expected_value_f_3 == actual_f_discount_amount_3


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









