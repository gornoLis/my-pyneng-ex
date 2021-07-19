# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
user_vlan = input("Введите номер vlan: ")

result = list()
with open("CAM_table.txt") as f:
    for line in f:
        line = line.split()
        if line and line[0].isdigit() and line[0] == user_vlan:
            vlan, mac, _, ports = line
            print(f"{vlan:<10} {mac:20} {ports}")