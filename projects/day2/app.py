import calculator
from logger import logger

num1 = float(input("Enter first number: "))
logger.info(f"First number entered: {num1}")
num2 = float(input("Enter second number: "))
logger.info(f"Second number entered: {num2}")
operation = input("Enter operation (+, -, *, /): ")
logger.info(f"Operation selected: {operation}")
if operation == '+':
    result = calculator.add(num1, num2)
elif operation == '-':
    result = calculator.subtract(num1, num2)
elif operation == '*':
    result = calculator.multiply(num1, num2)
elif operation == '/':
    result = calculator.divide(num1, num2)

logger.info(f"Result calculated: {result}")
print(f"The result of {num1} {operation} {num2} is: {result}")
