import time
from random import randint

hidden_num = randint(1, 100)
print('Добро пожаловать в числовую угадайку')


def is_valid(num):
    return num.isdigit() and 1 <= int(num) <= 100


def input_num():
    while True:
        number = input('Введите число от 1 до 100: ')
        if is_valid(number):
            return int(number)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


def search_num():
    while True:
        num = input_num()
        if num < hidden_num:
            print('Ваше число меньше загаданного, попробуйте еще разок: ')
        if num > hidden_num:
            print('Ваше число больше загаданного, попробуйте еще разок: ')
        if num == hidden_num:
            print('Вы угадали, поздравляем!')
            break


search_num()
time.sleep(1)
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
