# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 00:29:49 2022

@author: Alexander A. Nazarov

The program guesses a randomly generated number in the minimum number 
of attempts.
Программа угадывает случайно сгенерированное число за минимальное 
количество попыток.
"""

# Command to clear the console (terminal) for Spyder.
# Команда для очистки консоли (терминала) для Spyder.

# Warning! When working for VS Code, this command should be disabled.
# Предупреждение! При работе с VS Code эта команда должна быть отключена.
#%clear

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


### === CONSTANTS ===

# Constants that specify the range of possible values of the generated number 
# Константы, задающие интервал возможных значений сгенерированного числа
NUMBER_MIN = 1
NUMBER_MAX = 100


### === FUNCTIONS ===

def number_predict(number_in: int=1) -> int:
    """
    The function guesses the number using the half division algorithm.
    Функция угадывает число, используя алгоритм половинного деления.
    
    Args:
        number (int, optional): The hidden number. Defaults to 1.
                                Загаданное число. По умолчанию равно 1.

    Returns:
        int: Number of attempts
             Число попыток
    """
    
    number_low = NUMBER_MIN
    number_high = NUMBER_MAX
        
    # Implementation of the half division algorithm
    # Реализация алгоритма половинного деления
    def guessing_number(a, b): return int(round((a+b) / 2))
        
    count = 0
    while True:
        count += 1
        number_predicted = guessing_number(number_low, number_high)
        if number_predicted < number_in:
            number_low = number_predicted
        elif number_predicted > number_in:
            """Условие, предотвращающее зацикливание алгоритма при 
            округлении к нижней границе
                A condition that prevents the algorithm from looping 
            when rounding to the lower bound"""
            if number_predicted == 2:
                number_predicted = 1
                break
            else:
                number_high = number_predicted
        else:
            break
    
    return count


def score_game(func_in, size_in: int=1000) -> int:
    """
        The function returns the average number of attempts for which the 
    algorithm guesses a random number.
        Функция возвращает среднее число попыток, за которое алгоритм угадывает
    случайное число.
    
    Args:
        func_in ([type]): guessing function 
                          функция угадывания
        size_in (int, optional): number of iterations 
                                 число итераций
            
    Returns:
        int: average number of attempts
             среднее количество попыток
    """
    
    # List to save the number of attempts 
    # Список для сохранения количества попыток
    count_ls = []
    
    # Generating a list of random numbers
    # Генерируем список случайных чисел
    np.random.seed(1)
    random_array = np.random.randint(NUMBER_MIN, NUMBER_MAX, size=size_in)
            
    for elem in random_array:
        count_ls.append(func_in(elem))
            
    # Determination the average number of attempts
    # Определение среднего числа попыток
    score = int(np.mean(count_ls))
        
    print(f"Average number of guessing attempts: {score}")
        
    # Histogram of the number of attempts to guess a random number
    # Гистограмма количества попыток угадать случайное число
    groups = [elem for elem in set(count_ls)]
        
    bins = []
    for i in range(1, max(groups)+1):
        bins.append(i - 0.5)
        
    plt.hist(count_ls, bins=bins)
    plt.show()     
    
    return score


### === RUN ===

if __name__ == "__main__":
    Title = "Calculating the average number of attempts for which the half " +\
        "division algorithm guesses the number"
    print(Title.upper(), '\n')

    score_game(number_predict, 1000)
