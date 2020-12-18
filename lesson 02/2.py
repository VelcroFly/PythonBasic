user_input_list = []
val = str()
cnt = int()

while True:
    val = input('Укажите добавляемый в список элемент/ "q" - закончить ввод: ')
    if val == 'q':
        break
    else:
        user_input_list.append(val)

swapped_list = list()

for i in user_input_list[1::2]:
    swapped_list.append(i)

for pos, i in enumerate(user_input_list[::2]):
    cnt += 1
    swapped_list.insert(pos + 1 * cnt, i)

print(swapped_list)



