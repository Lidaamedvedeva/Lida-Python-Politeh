# -*- coding: utf-8 -*-
"""Untitled6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1imNq7J4Qm5dDBnvM3pan7HzJ6lBGjTFy
"""

import random
import time

def math_game():

    seconds = 3

    while True:

        rand_a = random.randint(1, 100)
        rand_b = random.randint(1, 100)
        right_answer = rand_a + rand_b

        print(f"Новый пример: {rand_a} + {rand_b}?")
        user_answer = int(input("Ваш ответ: "))

        if user_answer == right_answer:
            print("Поздравляю! Ваш ответ правильный")
            return
            #break

            print(f"Неверно! Штрафная пауза: {seconds} секунд")
            time.sleep(seconds)
            seconds = seconds + 1
        #  print(f'Игра закончилась')

math_game()