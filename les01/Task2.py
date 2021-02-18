num_list = []
sum_a = 0
sum_c = 0

for num_i in range (1, 1000, 2):
    num_list.append(num_i ** 3)

# a
for i in num_list:
    x = 0
    for d in str(i):
        x += int(d)
    if x // 7 != 0:
        sum_a += i

# c
for i in num_list:
    x = 0
    i += 17
    for d in str(i):
        x += int(d)
    if x // 7 != 0:
        sum_c += i

print(num_list)
print(sum_a)
print(sum_c)
