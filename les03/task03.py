def thesaurus(*args):
    arr = {key[0]: [] for key in args}
    for el in args:
        arr[el[0]].append(el)
    print(arr)


thesaurus("Иван", "Мария", "Петр", "Илья")
