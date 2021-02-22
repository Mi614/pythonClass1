mylist = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


for el in mylist.copy():
    y = 0
    for d in el:
        if d.isdigit():
            y += 1
    if y > 0:
        mylist.append('"')
        mylist.append(el.zfill(2))
        mylist.append('"')
    else:
        mylist.append(el)
    mylist.remove(el)

print(mylist)

print(' '.join(mylist))
