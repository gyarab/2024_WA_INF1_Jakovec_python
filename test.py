def vowels_and_consonants(text):
    vowels = "aeiouáéíóúůýěAEIOUÁÉÍÓÚŮÝĚ"
    consonants = "bcčdďfghjklmnňpqrřsštťvwxzžBCČDĎFGHJKLMNŇPQRŘSŠTŤVWXZŽ"
    text = ''.join(filter(str.isalpha, text))
    
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char in vowels:
            vowel_count += 1
        elif char in consonants:
            consonant_count += 1
    
    return {"vowels": vowel_count, "consonants": consonant_count}
