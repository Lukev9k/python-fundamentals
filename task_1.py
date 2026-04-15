my_words = ['po', 'cat', 'elf', 'check', 'return', 'capital']

def filter_long_words(words: list, min_length: int) -> list:
    # [what_to_keep   for item in collection   if condition]
    # give me each item, for each item in words, if len(item) > min_length
    result = [word for word in words if len(word) > min_length]
    return result

print(filter_long_words(my_words, 3))
