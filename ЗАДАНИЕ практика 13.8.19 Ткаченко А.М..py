bilet = int(input('Введите кол-во билетов: '))
count = 0
for i in range(bilet):
    age = int(input('Введите возраст: '))
    if age < 18:
        count += 0
    elif 18 <= age < 25:
        count += 990
    else:
        count += 1390
if bilet > 3:
    count = count * 0.9
print('Итого' + ' ' + str(round(count)) + ' ' + 'рублей')
