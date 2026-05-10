from ping3 import ping, verbose_ping

def ping_test(host):
    for i in range(4):
        ping_exit = ping(host, unit='ms')           #пинг сервера, выводим в миллисекундах
        if ping_exit == False:                      #проверка на неверный домен либо айпишник
            print("Ошибка: неверный домен/ip")
            break;
        elif ping_exit == None:                     #проверка на время ожидания
            print('Время ожидания истекло (сервер не отвечает)')
            break;
        else:
            print(int(ping_exit), 'ms')             #собственно вывод


ping_test(input("Введите ваш домен: "))
