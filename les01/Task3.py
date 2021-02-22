ending_word = ['процентов', 'процента', 'процент']

user_num = int(input('Введите число: '))

print(f'{user_num}', end=' ')

if user_num >= 5 or user_num == 0:
    print(ending_word[0])
elif 1 < user_num < 5:
    print(ending_word[1])
else:
    print(ending_word[2])