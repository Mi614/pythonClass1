def thesaurus_adv(*args):
    arr = [[key[0][0], key[1][0], ' '.join(key)]
           for key in [el.split() for el in args] ]
    final = {}
    for key in arr:
        if final.get(key[1]) is None:
            final.update({key[1]: {key[0]: [key[2]]}})
        elif final[key[1]].get(key[0]) is None:
            final[key[1]].update({key[0]: [key[2]]})
        else:
            final[key[1]][key[0]].append(key[2])

    return final


print(thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева", "Сергей Васильев"))
