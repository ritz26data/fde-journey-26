import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

def calculate_average(data):
    logging.info("Calculating average")
    if not data:
        return 0
    return sum(data) / len(data)

def find_maximum(data):
    logging.info("Finding maximum")
    if not data:
        return None
    return max(data)

def find_minimum(data):
    logging.info("Finding minimum")
    if not data:
        return None
    return min(data)

def calculate_total(data):
    logging.info("Calculating total")
    return sum(data)

def main():
    data = [10, 20, 30, 40, 50]

    logging.info("Starting calculations")
    average = calculate_average(data)
    maximum = find_maximum(data)
    minimum = find_minimum(data)
    total = calculate_total(data)

    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"Total: {total}")    

if __name__ == "__main__":
    main()  