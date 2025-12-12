Prompt Chain for Task 2 — Debugging Python Code

---------------------------------------------------------

Prompt 1
Identify issues in the following Python code and explain what is causing errors:
def calculate_average(numbers):
    total = 0
    for num in numbers:
        total = total + num
    average = total / len(num)   # Bug: len(num) is wrong
    return average

values = [10, 20, 30, 40]
print("Average is:", calculate_average(values))

Output:
- The expression len(num) is incorrect because num represents a single number, not the list.
- No validation for empty lists.
- No type checking to ensure input is a list of numbers.
- Manual summation is fine but can be simplified using sum().

---------------------------------------------------------

Prompt 2
Rewrite the code with fixes and improvements. Add basic error handling.

Output:
- Introduced type checking with isinstance()
- Added empty list validation
- Replaced manual loop with sum()
- Corrected average calculation using len(numbers)

---------------------------------------------------------

Prompt 3
Explain the differences between the buggy and corrected versions in simple terms.

Output:
- Fixed incorrect length calculation
- Added basic defensive programming
- Made the code cleaner and more readable
- Ensured the function behaves predictably with bad input

