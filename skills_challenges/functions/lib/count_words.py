def count_words(string):
    numbers = '0123456789'
    list_of_words = string.split(" ")
    word_count = 0
    for i in list_of_words:
        if not any(char in numbers for char in i):            
                word_count += 1
    return word_count
    #word_only_string = ''.join(i for i in string if i.alpha())
    