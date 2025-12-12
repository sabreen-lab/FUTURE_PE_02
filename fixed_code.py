# Corrected Python code 

def calculate_average(numbers):
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of numbers.")
    if len(numbers) == 0:
        raise ValueError("List cannot be empty.")

    total = sum(numbers)
    average = total / len(numbers)
    return average

values = [10, 20, 30, 40]
print("Average is:", calculate_average(values))
