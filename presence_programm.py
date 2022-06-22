import psutil
from pypresence import Presence
import time

while True:
    client_id = int(input('Айди приложения в ddp: '))  # айди приложения в ddp

    if client_id == None:
        print('Введите айди приложения в ddp')  # проверка на ввод айди
        exit()
    else:
        RPC = Presence(client_id, pipe=0)  # хуйня какая-то
        RPC.connect()  # подключаемся к discord
        details = input('Описание вашей активности: ')  # текст присутствия
        if details == '':
            print('Описание обязательно')
        else:
            state = input('Что вы конкретно делаете: ')  #
            if state == '':
                large_image = input('Ссылка на изображение: ')  # ссылка на изображение
                if large_image == '':
                    while True:  # бесконечный цикл
                        print(RPC.update(details=details))
                        # обновляем присутствие
                        time.sleep(15)  # пауза в 15 секунд
                else:
                    large_text = input('Текст изображения: ')  # текст изображения
                    if large_text is None:
                        print(RPC.update(details=details,
                                         large_image=large_image))
                    else:
                        print(RPC.update(details=details,
                                         large_image=large_image,
                                         large_text=large_text))
            else:
                large_image = input('Ссылка на изображение: ')  # ссылка на изображение
                if large_image == '':
                    while True:  # бесконечный цикл
                        print(RPC.update(details=details,
                                         state=state))
                        # обновляем присутствие
                        time.sleep(15)  # пауза в 15 секунд
                else:
                    large_text = input('Текст изображения: ')  # текст изображения
                    if large_text is None:
                        print(RPC.update(details=details,
                                         state=state,
                                         large_image=large_image))
                    else:
                        print(RPC.update(details=details,
                                         large_image=large_image,
                                         large_text=large_text))
