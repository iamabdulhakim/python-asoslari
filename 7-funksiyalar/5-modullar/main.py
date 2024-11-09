# -*- coding: utf-8 -*-
"""
Created on Mon Oct 14 11:15:04 2024

@author: Saidus_work
"""

# MODULNI CHAQIRIB OLISH

# =============================================================================
# import avto_info_mod
# 
# avto1 = avto_info_mod.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# avto_info_mod.info_print(avto1)
# =============================================================================

# MODULGA QISQA NOM BERISH

# =============================================================================
# import avto_info_mod as aim
# 
# avto1 = aim.avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# aim.info_print(avto1)
# 
# =============================================================================

# MODUL ICIHDAN MA'LUM FUNKSIYALARNI KO'CHIRIB OLISH

# =============================================================================
# from avto_info_mod import avto_info, info_print 
# 
# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)
# 
# =============================================================================

# FUNKSIYALARGA QISQA NOM BERISH

# =============================================================================
# from avto_info_mod import avto_info as ainfo, info_print as iprint
# 
# avto1 = ainfo("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# iprint(avto1)
# =============================================================================

# MODUL ICHIDAGI BARCHA FUNKSIYALARNI KO'CHIRIB OLISH

# =============================================================================
# from avto_info_mod import *
# 
# avto1 = avto_info("GM", "Malibu", "Qora", "avtomat", 2020,40000)
# info_print(avto1)
# =============================================================================


# MODULDA O'ZGARUVCHI SAQLASH


# import avto_info_mod

# print(avto_info_mod.mashinalar)



                # PYTHON MODULLARI #
                

# math MODULI

# =============================================================================
# import math
#         
#     #1  sqrt() - qavs ichida berilgan qiymatning kvadrat ildizini qaytaradi
# x = 81
# print(math.sqrt(x))
# 
#     #2  pow(x,y) - x ning y-darajasini qaytaradi
# print(math.pow(5, 5))
# 
#     #3  pi - PI ning qiymatini saqlovchi o'zgaruvchi
# print(math.pi)
# 
#     #4  log2(x) va log10(x) - x` ning 2 va 10-lik logorifmini qaytaruvchi funksiyalar
# print(math.log2(8))
# print(math.log10(100))
# =============================================================================


# random MODULI

import random

    #1  randint(a,b) - Bu funksiya a va b oraligi'da tasodifiy butun son qaytaradi.
son = random.randint(20,50)
print(son)

    #2  choice(x) - x ning ichidan tasodifiy qiymatni qaytaruvchi funksiya. 
    #Bunda x bir necha elementdan iborat o'zgaruvchi (matn, ro'yxat) bo'lishi kerak.
ismlar = ['olim','anvar','hasan','husan']
ism = random.choice(ismlar)
print(ism)
print(random.choice(ism))

x = list(range(0, 51, 5))
print(x)
print(random.choice(x))

    #3  shuffle(x) - x ichidagi elementlarni tasodifiy tartibda qaytaruvchi funksiya. 
    #Bunda x bir necha elementdan iborat o'zgaruvchi (matn, ro'yxat) bo'lishi kerak.
x = list(range(11))
print(x)
random.shuffle(x)
print(x)

    #4  sample(x, k) - x  ro'yxat ichidan tasodifiy k ta elementni ajratib oladi.
x = list(range(100))
y = random.sample(x, 15)
print(y)






































































