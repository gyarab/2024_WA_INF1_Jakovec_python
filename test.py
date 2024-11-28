def rotate_array(arr, n):
    if isinstance(arr, list) and all(isinstance(x, int) for x in arr) and isinstance(n, int) and !(n < arr.length()):
        return arr[-n:] + arr[:-n]
    else:
        return "Invalid input"