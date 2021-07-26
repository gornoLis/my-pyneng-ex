# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess

def ping_ip_addresses(ip_list):
    reach_list = []
    unreach_list = []
    for ip in ip_list:
        result = subprocess.run(['ping','-n','3', ip],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            reach_list.append(ip)
        else:
            unreach_list.append(ip)
    return reach_list, unreach_list


if __name__== "__main__":
    ip_list= ["8.8.8.8", "1.144.1"]
    print(ping_ip_addresses(ip_list))