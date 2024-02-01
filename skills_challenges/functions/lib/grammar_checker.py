def grammar_checker(text):
    accepted_punc = ".!?:"
    capital = text[0].isupper()
    end_punc = text[-1] in accepted_punc
    return f"Capital Letter: {capital}\nEnd of sentence punctuation: {end_punc}"