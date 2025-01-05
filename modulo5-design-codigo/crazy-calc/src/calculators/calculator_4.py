from typing import Dict, List
from flask import request as FlaskRequest
from src.errors.http_unprocessable_entity import HttpUnprocessableEntityError

class Calculator4:
    def calculate(self, request: FlaskRequest) -> Dict: #type: ignore
        body = request.json
        input_data = self.__validate_body(body)
        response = self.__average(input_data)
        formated_response = self.__format_response(response)
        return formated_response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Invalid Body Request!")
        
        input_data = body["numbers"]
        return input_data
    
    def __average(self, numbers: List[float]) -> float:
        result_average = sum(numbers) / len(numbers)
        return result_average
    
    def __format_response(self, average: float) -> Dict:
        return {
            "data": {
                "Calculator": 4,
                "average": round(average, 2)
            }
        }