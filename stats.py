def get_num_words(p1):
    num_words = len(p1.split())
    return num_words

def get_characters(p1):
    characters = {}
    for ch in p1:
        if characters.get(ch.lower()) != None:
            characters[ch.lower()] += 1
        else:
            characters[ch.lower()] = 1
    return characters

def sort_dict(p1):
    results = []
    for key, value in p1.items():
        if key.isalpha():
            results.append({'char': key, 'num': value})
    sorted_results = sorted(results, key=lambda x: x['num'], reverse=True)
    return sorted_results