from typing import Dict
from .calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body

def test_calculate():
    mock_request = MockRequest({"numbers": [15, 20, 25]})
    calculator_4 = Calculator4()
    response = calculator_4.calculate(mock_request)
    assert response == {'data': {'Calculator': 4, 'average': 20.0}}