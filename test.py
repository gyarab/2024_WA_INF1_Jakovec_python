def rotate_array(arr, n):
    if isinstance(arr, list) and all(isinstance(x, int) for x in arr):
        return arr[-n:] + arr[:-n]
    else:
        return "Invalid input"