# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
address = input("Введите IP-адрес сети: ")
address = address.split("/")
network = address[0].split(".")
mask = int(address[1])

output_network = '''
Network:
{0:<8} {1:<8} {2:<8} {3:<8}
{0:08b} {1:08b} {2:08b} {3:08b}
'''
output_mask = '''
Mask:
/{0}
{1:<8} {2:<8} {3:<8} {4:<8}
{1:08b} {2:08b} {3:08b} {4:08b}
'''

octs = [
    int(network[0]),
    int(network[1]),
    int(network[2]),
    int(network[3])
]
bin_mask = "1"*mask + "0"*(32-mask)
m = [
    int(bin_mask[0:8],2),
    int(bin_mask[8:16],2),
    int(bin_mask[16:24],2),
    int(bin_mask[24:32],2)
]
print(output_network.format(octs[0], octs[1],octs[2],octs[3]))
print(output_mask.format(mask,m[0],m[1],m[2],m[3]))