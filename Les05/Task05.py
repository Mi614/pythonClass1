src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new_scr = [el for el in src if src.count(el) == 1]
print(new_scr)
result = [23, 1, 3, 10, 4, 11]
