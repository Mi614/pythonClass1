user_input = []

for i in range(3):
    user_input.append(int(input('Введите время в секундах')))

for i in user_input:
    dd = i // 86400
    hh = i % 86400 // 3600
    mm = i % 3600 // 60
    ss = i % 60
    years = 0 if dd < 365 else dd // 365
    mo = dd // 31 if dd < 365 else dd % 365 // 31

    if years > 0:
        print(f'{years} г.', end=' ')
    if mo > 0:
        print(f'{mo} мес.', end=' ')
    if dd > 0:
        print(f'{dd % 31} д.', end=' ')
    if hh > 0:
        print(f'{hh} ч.', end=' ')
    if mm > 0:
        print(f'{mm} мин.', end=' ')
    print(f'{ss} сек.', end='\n')
