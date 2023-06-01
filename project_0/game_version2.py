import numpy as np

def random_predict(number: int) -> int:
    """Функция для угадывания числа

    Args:
        number (int): загаданное число

    Returns:
        int: количество попыток
    """
    count = 1
    predict = np.random.randint(1, 101)  # предполагаемое число

    while predict != number:
        count += 1
        if predict < number:
            predict += 1
        elif predict > number:
            predict -= 1

    return count

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict (function): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# Запуск игры
score_game(random_predict)