def make_snippet(str):
    words = str.split(" ")
    first_five = words[:5]
    snippet = ' '.join(first_five)
    if len(words) > 5:
        return f"{snippet}..."
    else:
        return snippet