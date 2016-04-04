n = ["Michael", "Ross", "Joe", "Phill"]


def join_strings(words):
    result = ""
    for item in range(len(words)):
        result += words[item]
    return result


print join_strings(n)
