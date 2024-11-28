def split_into_threes(text):
    if not isinstance(text, str):
        text = str(text)
    result = []
    for i in range(0, len(text), 3):
        substring = text[i:i+3]
        if len(substring) == 3:
            result.append(substring)
    return result