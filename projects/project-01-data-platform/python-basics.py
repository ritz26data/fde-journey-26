def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def find_maximum(numbers):
    if not numbers:
        return None
    return max(numbers)

def lowest_score(numbers):
    if not numbers:
        return None
    return min(numbers)

def total_score(numbers):
    if not numbers:
        return 0
    return sum(numbers)

def main():
    data = [10, 20, 30, 40, 50]
    
    average = calculate_average(data)
    maximum = find_maximum(data)
    minimum = lowest_score(data)
    total = total_score(data)

    print(f"Average: {average}")
    print(f"Maximum: {maximum}")
    print(f"Minimum: {minimum}")
    print(f"Total: {total}")
    print(f"Scores: {data}")

if __name__ == "__main__":
    main()