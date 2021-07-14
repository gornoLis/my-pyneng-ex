# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

while True:
    ip = input("Введите IP-адрес: ")
    try:
        octs = ip.split(".")
        if len(octs) != 4:
            raise ValueError
        for oct in octs:
            if int(oct) < 0 or int(oct) > 255:
                raise ValueError

        oct1 = int(octs[0])

        if ip == '0.0.0.0':
            result = 'unassigned'
        elif ip == '255.255.255.255':
            result = 'local broadcast'
        elif oct1 >=0 and oct1 <= 223:
            result = 'unicast'
        elif oct1 >= 224 and oct1 <=239:
            result = 'multicast'
        else:
            result = 'unused'
        print(result)
        break
    except ValueError:
        print("Неправильный IP-адрес")
