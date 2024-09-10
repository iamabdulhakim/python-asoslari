# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 06:40:28 2024

@author: Saidus_work
"""
#
# =============================================================================
# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else: 
#         print(avto.title())
# =============================================================================
#
# =============================================================================
# ism = input('Ismingiz nima?\n>>> ')
# if ism.lower() != 'ali': 
#     print(f'Uzr! {ism.title()}, biz Ali ni kutyapmiz.')
# else: 
#     print('salom Ali! ')
# =============================================================================
#
# =============================================================================
# javob = float(input('12 * 6  nechiga teng? '))
# if javob != 72:
#     print('Javob xato.')
# =============================================================================
#
# =============================================================================
# yosh = int(input('yoshingiz nechida? '))
# if yosh >= 18:
#     print('Xush kelibsiz.')
# else:
#     print('Kirish mumkin emas.')
# =============================================================================
#
# =============================================================================
# yil = int(input('Yilingizni kiriting: '))
# if 2024-yil < 18:
#     print(f'Yoshingiz {2024-yil} da ekan,')
#     print('kirish mumkin emas.')
# else:
#     print('Xush kelibsiz.')
# =============================================================================
#
# =============================================================================
# yosh = int(input('Yoshingiz nechida? '))
# if yosh > 65: print('Siz COVID 19 risk guruhida ekansiz.')
# =============================================================================
#
# =============================================================================
# x , y = 250 , 500
# print('x>y') if x > y else print('y>x')
# =============================================================================

# AMALIYOT

# Quyidagi dasturlarni bajaring. 
# =============================================================================
# avtolar = ['audi', 'bmw', 'volvo', 'kia', 'hyundai']
# for avto in avtolar:
#     if avto == 'bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())
# =============================================================================

# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, 
   # ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. 
     # GM uchun ikkala harfni katta qiling.
     
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car == 'gm':
        print(car.upper())
    else:
        print(car.title())
        
# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())

# Foydalanuvchi login ismini so'rang. 
 # Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?"
  # xabarini konsolga chiqaring.
   # Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!" matnini konsolga chiqaring.
# =============================================================================
# login = input('Loginingizni kiriting: ')
# if login.lower() == 'admin':
#     print( "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" )
# else: 
#     print(f'Xush kelibsiz, {login}! ')
# =============================================================================
   
# Foydalanuvchidan 2 ta son kiritishni so'rang. 
 #Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# =============================================================================
# a = int(input('Birinchi sonni kiriting: '))     
# b = int(input('Ikkinchi sonni kiriting: '))
# if a == b:
#     print('Sonlar teng ekan')
# =============================================================================
    
# Foydalanuvchidan istalgan son kiritishni so'rang. 
 # Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son"
  # degan xabarni chiqaring.   
# =============================================================================
# son = int(input('Istalgan sonni kiriting: '))
# if son < 0:
#     print('Manfiy son')
# else:
#     print('Musbat son')
# =============================================================================

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab
  # konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring.
# =============================================================================
# son = int(input('Son kiriting: '))
# if son > 0:
#     print(son**(1/2))
# else:
#     print('Musbat son kiriting! ')
# =============================================================================
    
# Kiritilgan son toq yoki juftligini konsolga chiqaruvchi dastur.
son = int(input('Istalgan son kiriting: '))
if son % 2 == 0:
    print(f'{son} - juft son.')
else:
    print(f'{son} - toq son.')














