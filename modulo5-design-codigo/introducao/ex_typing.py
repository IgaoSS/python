from typing import Dict

def sum(num1: int, num2: float) -> int:
    return num1 + num2

def add1(num1: int, num2: float) -> Dict:
    return num1 + num2

val1 = sum(4, 5)
val2 = sum(4.4, 5)
val3 = sum(2, 5.1)
val4 = add1(2, 5.1)

print(val1)
print(val2)
print(val3)
print(val4)