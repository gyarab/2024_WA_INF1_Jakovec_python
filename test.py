# Convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    if not isinstance(celsius, (int, float)):
        raise ValueError("Input must be a number.")
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# Convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, (int, float)):
        raise ValueError("Input must be a number.")
    celsius = (fahrenheit - 32) * 5/9
    return celsius

# Check if input is a valid number
def is_valid_number(value):
    return isinstance(value, (int, float))

# Generate Fibonacci sequence
def fibonacci(user_input):
    if not isinstance(user_input, int) or user_input <= 0:
        raise ValueError("Input must be a positive integer.")
    elif user_input == 1:
        return [0]
    elif user_input == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < user_input:
            next_num = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_num)
        return fib_sequence

# Example Usage
try:
    # Test temperature conversions
    celsius = 25
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius}°C is {fahrenheit}°F")

    fahrenheit = 77
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit}°F is {celsius}°C")

    # Test Fibonacci sequence
    user_input = int(input("Enter the number of Fibonacci terms: "))
    fib_sequence = fibonacci(user_input)
    print("Fibonacci sequence:", fib_sequence)
except ValueError as e:
    print(f"Error: {e}")
