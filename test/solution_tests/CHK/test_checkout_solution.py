
from lib.solutions.CHK import checkout_solution

class TestCheckoutSuite():
    '''
    suite for testing checkout solution
    '''

    def test_checkout(self) -> None:
        '''
        test the checkout method
        '''

        #test normal behaviour without applica
        test_sku_string: str = 'ABCD'
        actual_checkout_value = checkout_solution.checkout(test_sku_string)
        expected_checkout_value = 50 + 30 + 20 + 15
        assert actual_checkout_value == expected_checkout_value


