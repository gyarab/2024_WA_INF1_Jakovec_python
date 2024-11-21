def fibonacci(user_input):
    while True:
        try:
            if user_input <= 0:
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Generate Fibonacci sequence
    if user_input == 1:
        return [0]
    elif user_input == 2:
        return [0, 1]
    else:
        fib_sequence = [0, 1]
        while len(fib_sequence) < user_input:
            next_num = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_num)
        return fib_sequence


# Call the fibonacci() function and print the result
fib_sequence = fibonacci()
print("Fibonacci sequence:", fib_sequence)
