# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 05:31:21 2024

@author: Saidus_work
"""

# SONLAR

a = 20    # Sonlar musbat yoki
b = -30   # manfiy bo'lishi mumkin
c = a + b 
print(c)

# Kvadratning yuzini hisoblaymiz:
    
kvadrat_tmni = 20
kvadrat_yuzi = kvadrat_tmni**2
print(kvadrat_yuzi)

# FLOATS — O'NLIK SONLAR

pi = 3.14159    # o'nlik son (float)
radius = 10     # butun son (integer)
diametr = 2*radius
print('Aylana uzunligi ', pi*diametr, 'ga teng')


# BUTUN SONDAN O'NLIK SONGA

a = -20 
b = 40
c = b/a
print(c)
#
a = 2 
b = 3.0
print(a+b)
print(a*b)
print(a**b)
print(2*(a+b))

# UZUN SONLARNI KIRITISH

aholi_soni = 7_594_000_000  # o'zmizga qulay bo'lishi uchun shunday yozdik
print("Yer kurrasida ", aholi_soni, "ga yaqin odam yashaydi")

# KONSTANTA (O'zgarmas qiymat)

PI = 3.14159
raduis = 21.2


# =============================================================================
# # BIR NECHTA O'ZGARUVCHIGA QIYMAT BERISH
# # Quyidagi kod x ga 10, y ga -7.25, va z ga -30 qiymatini yuklaydi.
# x, y, z = 10, -7.25, -30
# #
# yosh, ism = 36, "Olimjon"
# print(f'{ism} {yosh} yoshda')
# =============================================================================

# O'ZGARUVCHI TURINI ALMASHTIRISH

ism = 'Jobir'
yosh = 36
xabar = ism + ' ' + str(yosh) + ' yoshda'
print(xabar)

# O'ZGARUVCHI TURINI TEKSHIRISH - " type() "

ism = 'Jobir'
yosh = 36
print(type(ism))
print(type(yosh))

# INPUT() VA SONLAR

# =============================================================================
# #1 foydalanuvchining tug'ilgan yilini so'raymiz
# t_yil = input(" Tyg'ulgan yilingizni kiriting:")
# #2 foydalanuvchi yoshini xisoblaymiz
# yosh = 2024 - t_yil
# #3 foydalanuvchi yoshini konsolga chiqaramiz
# print('Siz ' + yosh + 'yoshdasiz')
# =============================================================================

# =============================================================================
# #1 foydalanuvchining tug'ilgan yilini so'raymiz
# t_yil = int(input(" Tyg'ulgan yilingizni kiriting:"))
# #2 foydalanuvchi yoshini xisoblaymiz
# yosh = 2024 - t_yil
# #3 foydalanuvchi yoshini konsolga chiqaramiz
# print('Siz ' + str(yosh) + ' yoshdasiz')
# 
# =============================================================================


# =============================================================================
# #1.1 foydalanuvchining tug'ilgan yilini so'raymiz
# t_yil = input(" Tyg'ulgan yilingizni kiriting:")
# #1.2 t_yil o'zgaruvchini int ga aylantiramiz
# t_yil = int(t_yil)
# #2 foydalanuvchi yoshini xisoblaymiz
# yosh = 2024 - t_yil
# #3 foydalanuvchi yoshini konsolga chiqaramiz
# print('Siz ' +  str(yosh) + ' yoshdasiz')
# 
# =============================================================================


























