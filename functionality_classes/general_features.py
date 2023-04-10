from fuzzywuzzy import fuzz, process


def find_similar_name(user_input, where_from):
    names = []
    objs = []
    for i in where_from:
        names.append(where_from[i].name)
        objs.append(where_from[i])
    best_match = process.extractOne(user_input, names, scorer=fuzz.partial_ratio, score_cutoff=70)
    return objs[names.index(best_match[0])] if best_match else None
