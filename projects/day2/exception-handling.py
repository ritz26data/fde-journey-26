import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def divide(a, b):
    return a / b

try:
    print(divide(10, 2))
    print(divide(10, 0))  # This will raise a ZeroDivisionError
except ZeroDivisionError as e:
    logging.exception(f"Error: {e}")