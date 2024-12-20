
from lib.solutions.CHK import checkout_solution

class TestCheckoutSuite():
    '''
    suite for testing checkout solution
    '''

    def test_checkout(self) -> None:
        '''
        test the checkout method
        '''

        #test normal behaviour without any applicable special offers
        test_sku_string_no_offer: str = 'ABCD'
        actual_checkout_value_no_offer = checkout_solution.checkout(test_sku_string_no_offer)
        expected_checkout_value_no_offer = 50 + 30 + 20 + 15
        assert actual_checkout_value_no_offer == expected_checkout_value_no_offer

        #test behaviour when special offers apply
        test_sku_string_with_offer: str = 'ABAACD'
        actual_checkout_value_with_offer = checkout_solution.checkout(test_sku_string_with_offer)
        expected_checkout_value_with_offer = 130 + 30 + 20 + 15
        assert actual_checkout_value_with_offer == a




