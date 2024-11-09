# -*- coding: utf-8 -*-
"""
Created on Wed Oct 16 19:12:41 2024

@author: Saidus_work
"""


# lambda YOHUD NOMSIZ FUNKSIYA 
            

# =============================================================================
# lambda argument : ifoda
# =============================================================================

import math
uzunlik = lambda pi, r : 2*pi*r
print(uzunlik(math.pi, 12))

#

product = lambda x, y : x ** y
print(product(5, 3))

#

def daraja(n):
    return lambda x : x**n

kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, kubi {kub(3)} ga teng")


# map() FUNKSIYASI


from math import sqrt

sonlar = list(range(11))
ildizlar = list(map(sqrt, sonlar))

#

sonlar = list(range(11))

def daraja2(x):
    """Berilgan sonning kvadratini qaytaruvchi funksiya"""
    return x*x 

print(list(map(daraja2, sonlar)))

#

sonlar = list(range(11))
kvadratlar = list(map(lambda x : x*x, sonlar))

#

a = [4, 5, 6]
b = [7, 8, 9]

a_plus_b = list(map(lambda x, y : x+y, a, b))

#

ismlar = ['hasan','husan','olim','umid']
print(list(map(lambda ism : ism.upper(), ismlar)))


# filter() FUNKSIYASI

import random

sonlar = random.sample(range(100), 10)

def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
    return x %2 == 0

juft_sonlar = list(filter(juftmi, sonlar))
print(sonlar)
print(juft_sonlar)

#

import random 

sonlar = random.sample(range(100),10)
juft_sonlar = list(filter(lambda son: son%2 == 0, sonlar))
print(sonlar)
print(juft_sonlar)

#

mevalar = ['olma','anor','anjir','shaftoli',"o'rik","tarvuz","qovun","banan"]

mevalar_b = list(filter(lambda meva: meva.startswith("b"), mevalar))
print(mevalar_b)

#

mevalar2 = list(filter(lambda meva: len(meva) <= 5, mevalar))
print(mevalar2)

#

a_r = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')), mevalar))
print(a_r)



                # AMALIYOT #
                
                
#1  Berilgan sonni 10 ga ko'paytiruvchi lambda funksiya yozing.

kopaytma = lambda x : x*10

#2  Ikki son qabul qilib, ularning yig'indisini qaytaruvchi lambda funksiya yozing.

yigindi = lambda son1, son2 : son1 + son2

#3  random moduli ichidagi sample funksiyasi yordamida 0 dan 1000 gacha sonlar oralig'idagi
# tasodifiy 10 ta sonlar ro'yxatini tuzing.

      # map() va lambda funksiya yordamida sonlarning kvadratini hisoblang.
      # filter() va lambda funksiya yordamida ro'yxatdan toq sonlarni ajratib oling.
      
      
from random import sample

sonlar = sample(range(1001), 10)

kvadratlar = list(map(lambda son : son*son, sonlar))
print(sonlar)
print(kvadratlar)

toq_sonlar = list(filter(lambda son : son%2 != 0, sonlar))
print(sonlar)
print(toq_sonlar)

#4  Berilgan son tub bo'lsa, True, aks holda, False qaytaruvchi funksiya yozing.
 
      # filter() va yuqoridagi funksiya yordamida 1 dan 10000 gacha oraliqdagi 
      # tub sonlar ro'yxatini tuzing

def tubmi(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True


tub_sonlar = list(filter(tubmi, range(1, 10000)))
print(tub_sonlar)



    
            
    
    









































