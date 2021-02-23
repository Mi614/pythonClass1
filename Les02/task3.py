my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(my_list)):
    el = my_list[i].split()
    el[-1] = el[-1].title()
    my_list[i] = ' '.join(el)
    print(f'Привет {el[-1]}!')
print(my_list)
my_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for i in range(len(my_list)):
    print(f'Привет, {my_list[i].split()[-1].title()}!')