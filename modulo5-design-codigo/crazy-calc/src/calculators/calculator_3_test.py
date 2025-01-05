from typing import Dict, List
from pytest import raises
from .calculator_3 import Calculator3

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

class MockDriverHandlerError:
    def variance(self, numbers: List[float]) -> float:
        return 1000000
    
class MockDriverHandler:
    def variance(self, numbers: List[float]) -> float:
        return 3

def test_calculate_with_variance_error():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 200]})
    calculator_3 = Calculator3(MockDriverHandlerError())
    
    with raises(Exception) as excinfo:
        calculator_3.calculate(mock_request)

    assert str(excinfo.value) == "Process failure: variance greater than multiplication"

def test_calculate():
    mock_request = MockRequest({"numbers": [1, 2, 3, 4, 5]})
    calculator_3 = Calculator3(MockDriverHandler())
    response = calculator_3.calculate(mock_request)
    assert response == {'data': {'Calculator': 3, 'Success': True, 'multiplication': 120, 'variance': 3}}
    