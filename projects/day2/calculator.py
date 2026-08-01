from logger import logger

def add(a:float, b:float) -> float:
    #logger.info(f"Adding {a} and {b}") 
    return a + b

def subtract(a:float, b:float) -> float:
    #logger.info(f"Subtracting {b} from {a}")
    return a - b

def multiply(a:float, b:float) -> float:
    #logger.info(f"Multiplying {a} and {b}")
    return a * b

def divide(a:float, b:float) -> float:
    #logger.info(f"Dividing {a} by {b}")
    if b == 0:
        logger.error("Attempted to divide by zero.")
        raise ValueError("Cannot divide by zero.")
    return a / b