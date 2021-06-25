import random as rd
import time

questions = {
"Как называется когда вы скрываете атрибуты класса от чтения и изменения!?": "Инкапсуляция",
"Оператор запроса в языке SQL, возвращающий набор данных из базы данных?": "Селект",
"Сколько стоит морковь?": "дорого"
}
questions_keys = questions.keys()
questions_values = questions.values()

gamers = ['Санжар', 'Кыял', 'Олжас', 'Константин', 'Айдана', 'Ислам']
gamers_amount = len(gamers)
count = 0

""" print('Добро пожаловать в игру "Поле Чудес"!')
time.sleep(1)
print('Внимание вопрос!')
time.sleep(1) """
""" 
def timer():
    for endtime in range(3):
        print(str(3 - endtime) + '...')
        time.sleep(1)
timer() """
random_questions = rd.choice(list(questions_keys))
answer = questions[random_questions]
answer = str(answer).upper()
close_view = []
print(random_questions)
for i in range(0, len(answer)):
    close_view.append('*')
print(''.join(close_view))

false_otvet = True
nachalo = True

for gamer in gamers:
    if not nachalo:
        continue
    
    
    user_choice = input('Угадать букву - 1 | Сказать слово сразу - 2: ')
    while True:
        current_user = gamers[count % gamers_amount]
        print(f'Игрок {current_user} пытается отгадать')
        if user_choice != '1' and user_choice != '2':
            print('Нужно выбрать 1 или 2!!! ')
            user_choice = input('Угадать букву - 1 | Сказать слово сразу - 2: ')
        else:
            if user_choice == '2':
                user_word = input('Назовите слово: ').upper()
                """ timer() """
                print(user_word, answer)

                if user_word == answer:
                    print(f'Вы угадали!!! \n Победитель {gamer}')
                    nachalo = False
                    break
            if user_choice == '1':
                user_word = input('Назовите букву: ').upper()
                if len(user_word) > 1 or user_word == user_word.isdigit() or user_word == '' or user_word == ' ':
                    user_word = input('Назовите букву: ')
                else:
                    if user_word in answer:
                        user_answer = ''
                        print('Такая буква есть!')
                        for i in range(0, len(answer)):
                            if answer[i] == user_word:
                                close_view[i] = user_word
                        user_answer = ''.join(close_view)
                        print(user_answer)
                        user_choice = input('Угадать букву - 1 | Сказать слово сразу - 2: ')
                    if user_answer == answer:
                        print(f'Вы угадали!!! \n Победитель {gamer}')
                        nachalo = False
                        break
                    
                    else:
                        print(f'{current_user}')
                        print('Такой буквы нет!')
                        count += 1



        