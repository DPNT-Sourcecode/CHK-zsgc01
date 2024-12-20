
from lib.solutions.HLO.hello_solution import hello

class TestHelloWorld():
    '''
    Hello World Test Suite
    '''
    def test_hello(self) -> None:
        '''
        test hello world
        '''
        test_name: str = 'Tom'
        response_string = hello(test_name)

        assert response_string == f'Hello, {test_name}!'



