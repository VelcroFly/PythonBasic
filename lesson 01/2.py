seconds = int(input('Введите время в секундах:'))
hours = seconds // 3600
minutes = seconds // 60 % 60
secs = seconds % 60

# print(f'Вереводим {seconds} секунд в формат чч:мм:сс.')
# print(f'Результат: {(seconds // 3600):02}:{(seconds % 3600 // 60):02}:{(seconds % 3600 // 60):02}')
print(f'{hours:02}:{minutes:02}:{secs:02}')
