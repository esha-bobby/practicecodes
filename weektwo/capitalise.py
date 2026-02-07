def cap_first_last(sentence):
    words = sentence.split()
    result = []
    for w in words:
        if len(w) == 1:
            result.append(w.upper())
        else:
            result.append(w[0].upper() + w[1:-1] + w[-1].upper())
    return " ".join(result)


