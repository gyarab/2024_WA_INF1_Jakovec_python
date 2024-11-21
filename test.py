def celsius_to_fahrenheit(celsius):
    if(jeToReady(celsius) == False):
        raise valueError()
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    if(jeToReady(fahrenheit) == False):
        raise valueError()
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def jeToReady(abc):
    if isinstance(abc, int):
        return True
    else:    
        return False

def fibonacci(user_input):
    if(isinstance(user_input,int) == False) :
        raise valueError()
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


fib_sequence = fibonacci()
print("Fibonacci sequence:", fib_sequence)