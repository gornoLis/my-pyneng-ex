# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
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
except ValueError:
   print("Неправильный IP-адрес")