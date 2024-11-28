def class_and_break_time(start_class, end_class):
    if not isinstance(start_class, int) or not isinstance(end_class, int) or end_class < start_class:
        raise ValueError("start_class and end_class must be integers")
    if start_class <= 0 or end_class <= 0:
        raise ValueError("start_class and end_class must be positive and non-zero")

    class_breaks = [45, 5, 45, 10, 45, 20, 45, 10, 45, 10, 45, 5, 45, 10, 45]
    total_class_minutes = 0
    total_break_minutes = 0

    for i in range(start_class - 1, end_class):
        if(i%2 == 0):
            total_class_minutes += class_breaks[i]
        else:
            total_break_minutes += class_breaks[i]

    return total_class_minutes, total_break_minutes

print(class_and_break_time(3, 6))