from fuzzywuzzy import process


def find_nearest(text: str, variants: list, limit=7):
    print(456)
    return process.extract(text, variants, limit=limit)
