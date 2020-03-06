import numpy as np

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1, 101) # предполагаемое число
        if number == predict: 
            return count # выход из цикла, если угадали
        

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,100)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали

def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его на половину диапазона поиска в зависимости от того, больше оно или меньше нужного, при этом уменьшая границу поиска.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    predict = np.random.randint(1,100)
    l = 1
    r = 100
    # (l, r) - границы поиска 
    while number != predict:
        count+=1
        if number > predict:
            l = predict
            predict = l + max(1, (r - l) // 2)
        elif number < predict: 
            r = predict
            predict = r - max(1, (r - l) // 2)
    return(count) # выход из цикла, если угадали
        
def score_game(game_core_v1):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        #print('original :' + str(number))
        count_ls.append(game_core_v1(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)


# запускаем
score_game(game_core_v3)