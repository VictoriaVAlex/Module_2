fist = input('Введите целое число: ')
second = input('Введите второе целое число: ')
third = input('Введите третье целое число: ')
if fist == second == third:
    print(3)
elif fist == second or fist == third or second == third:
    print(2)
else:
    print(0)
