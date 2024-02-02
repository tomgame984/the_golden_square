def get_most_common_letter(text):
    counter = {}
    char_only = "".join([i for i in text if i.isalpha()])
    print(char_only)
    for char in char_only:
        counter[char] = counter.get(char, 0) + 1
    letter = sorted(counter.items(), key=lambda item: item[1])[-1][0]
    print(sorted(counter.items(), key=lambda item: item[1]))
    return letter


print(f"""
Running:  get_most_common_letter("the roof, the roof, the roof is on fire!"))
Expected: o
Actual:   {get_most_common_letter("the roof, the roof, the roof is on fire!")}
""")
