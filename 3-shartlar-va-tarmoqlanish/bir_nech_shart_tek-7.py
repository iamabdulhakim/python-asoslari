# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 07:31:29 2024

@author: Saidus_work
"""

# Foydalanuvchidan biror butun son kiritishni so'rang.
 # Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini
  # konsolga chiqaring.

son = int(input('Butun son kiriting: '))
for n in range(2,11):
    if son % n == 0:
        print(f'{son} soni {n} ga qoldiqsiz bo\'linadi.')
    else:
        print(f'{son} soni {n} ga qoldiqsiz bo\'linmaydi. ')
        
















