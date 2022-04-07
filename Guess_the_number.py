# Программа генерирует случайное число в диапазоне от 1 до 100
# и просит пользователя угадать это число.

from random import randint

number = randint(1, 100)

print('Привет, попробуй угадать число от 1 до 100')
num = -1

while num != number:
    num = int(input('Введи свое число: '))
    if num > number:
        print('Твое число слишком большое, попробуй еще раз')
    elif num < number:
        print('Твое число слишком мало, попробуй еще раз')
else:
    print(f'Поздравляю, ты отгадал число {number}')