# Intentional buggy Python code 

def calculate_average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    average = total / len(num)   # Bug: len(num) is wrong
    return average

values = [10, 20, 30, 40]
print("Average is:", calculate_average(values))
