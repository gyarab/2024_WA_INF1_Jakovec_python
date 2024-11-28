def rotate_array(arr, n):
    if isinstance(arr, list) and all(isinstance(x, int) for x in arr) and isinstance(n, int):
        return arr[-n:] + arr[:-n]
    else:
        return "Invalid input"
print (rotate_array([1, 2, 3, 4, 5, 6], "d")) # [5, 6, 1, 2, 3, 4]