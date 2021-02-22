user_input = []

for i in range(3):
    user_input.append(int(input('Введите время в секундах')))

# for i in user_input:
#     if i < 60:
#         print(i, ' сек.')
#     elif i < 3600:
#         print(f'{i // 60} мин. {i % 60} сек')
#     elif i < 86400:
#         print(f'{i // 3600} ч. {i % 3600 // 60} мин. {i % 60} сек.')
#     else:
#         print(f'{i // 86400 } д. {i % 86400 // 3600} ч. {i % 3600 // 60} мин. {i % 60} сек.')

for i in user_input:
    dd = i // 86400
    hh = i % 86400 // 3600
    mm = i % 3600 // 60
    ss = i % 60
    if dd > 0:
        print(f'{dd} д.', end=' ')
    if hh > 0:
        print(f'{hh} ч.', end=' ')
    if mm > 0:
        print(f'{mm} мин.', end=' ')
    print(f'{ss} сек.', end='\n')
