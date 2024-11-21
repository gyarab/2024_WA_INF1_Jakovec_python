def is_prime(number):
    if(isinstance(number, int) == False):
        return False
    elif (number <= 0):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True