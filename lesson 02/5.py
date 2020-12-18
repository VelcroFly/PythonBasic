rating = [7, 5, 3, 3, 2]
new_element = ''

while True:
    try:
        new_element = float(input('Введите новый числовой элемент списка: '))
        break
    except ValueError:
        print('Ошибка ввода: Введите новый числовой элемент списка!')

if max(rating) < new_element:
    rating.insert(0, new_element)
elif min(rating) > new_element:
    rating.append(new_element)
else:
    for pos, element in enumerate(rating.copy()[::-1]):
        if new_element <= element:
            rating.insert((pos * -1), new_element)
            break

print(rating)

