# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:30:34 2024

@author: Saidus_work
"""


# BIR NECHA SHARTLARNI TEKSHIRISH

# =============================================================================
# son = -55
# if son < 0:
#     print('Manfiy son.')
# else:
#     print('Musbat son.')
# =============================================================================
    
#
# =============================================================================
# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     print('Sizga kirish bepul.')
# elif yosh <= 12:
#     print('Sizga kirish 5000 so\'m. ')
# else:
#     print('Sizga kirish 10000 so\'m. ')
# =============================================================================
    
#
# =============================================================================
# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# else:
#     price = 10000
#     
# print(f"Sizga kirish {price} so'm")   
# =============================================================================

#
# =============================================================================
# yosh = int(input('Yoshingiz nechida? '))
# if yosh <= 4:
#     narx = 0
# elif yosh <= 12:
#     narx = 5000
# elif yosh <= 65:
#     narx = 10000
# else: 
#     narx = 8000
# print(f'Sizga kirish {narx} so\'m. ')
# =============================================================================

#
# =============================================================================
# kun = input('Bugun nima kun ? ')
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni.')
# elif kun.lower() == 'payshanba' or kun.lower() == 'juma':
#     print('Bugun bayram kuni. ')
# else:
#     print('Bugun ish kuni.')
# =============================================================================

#
# =============================================================================
# kun = input('Bugun nima kun ? ') 
# harorat = float(input('Havo harorati qnday ? '))
# if kun.lower() == 'yakshanba' and harorat >= 30:
#     print("Cho'milgani ketdik.")
# elif kun.lower() == 'yakshanba' and harorat < 30:
#     print('Bugun uyda dam olamiz.')
# =============================================================================

#
# =============================================================================
# kun = input('Bugun nima kun ? ') 
# harorat = float(input('Havo harorati qnday ? '))
# if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat >= 30:
#     print('Cho\'milgani ketdik.')
# elif (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat < 30:
#     print('Uyda dam olamiz.')
# =============================================================================

#
# =============================================================================
# narx = 15000
# choy = True
# salat = True
# if choy and salat:
#     narx = narx + 10000
# elif choy or salat:
#     narx = narx + 5000
# print(f'Jami {narx} so\'m. ')
# =============================================================================
 
#
# =============================================================================
# narx = 15000
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 0
# 
# if choy:
#     print('Mijoz choy oldi')
#     narx = narx + 3000
#     
# if salat: 
#     print("Mijoz salat oldi.")
#     narx = narx + 5000
#     
# if non: 
#     print("Mijoz non oldi.")
#     narx = narx + 2000
# 
# if kompot: 
#     print("Mijoz kompot oldi.")
#     narx = narx + 5000
#     
# if assorti: 
#     print("Mijoz assorti oldi.")
#     narx = narx + 15000
#     
# print(f'Jami narx {narx} so\'m. ')
# =============================================================================

#
# =============================================================================
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# 
# ovqat = input('Nima ovqat yeysiz?')
# if ovqat.lower() not in menu:
#     print('Uzr, bizda bunday ovqat yo\'q. ')
# else: 
#     print('Buyurtma qabul qilindi.')
# =============================================================================

#
# =============================================================================
# a = float(input('son kiriting.'))
# if a == 5:
#     print(' a 5 ga teng.')
# elif not a == 5:
#     print('a 5 fa teng emas')
# =============================================================================

#
# =============================================================================
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]    
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f'menuda {taom} bor.')
#     else:
#         print(f'menuda {taom} yo\'q.')
# =============================================================================

#
# =============================================================================
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = []
# 
# if buyurtmalar:
#    for taom in buyurtmalar:
#       if taom in menu:
#         print(f"Menuda {taom} bor")
#       else:
#         print(f"Kechirasiz, menuda {taom} yo'q")
# else:
#     print('Savatchangiz bo\'sh.')
# =============================================================================
    
    
    
    


# =============================================================================
# 
# yosh = int(input("Yoshingiz nechida? "))
# if yosh < 12:
#     print("Sizga kirish 5000 so'm. ")
# elif yosh < 4:
#     print("Sizga kirish bepul.")
# else:
#     print("Sizga kirish 10000 so'm.")
# =============================================================================

# =============================================================================
# yosh = int(input('Yoshni kiriting: '))
# kun = input('Bugun nima kun? ')
# if (yosh < 7 or yosh > 65) and kun.lower() == 'chorshanba':
#     print('Bugun muzeyga kirish bepul! ')
# =============================================================================


# =============================================================================
# 
# narx = 20000
# 
# choy = True
# non = True
# salat = False
# kompot = False
# assorti = True
# 
# if choy:
#     print("Mijoz choy oldi.")
#     narx = narx + 2000
# if non:
#     print("Mijoz non oldi.")
#     narx = narx + 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narx = narx + 5000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narx = narx + 6000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narx = narx + 10000
#     
# print(f"Jami {narx} so'm bo'ldi. ")
# 
# ===========================================


# =============================================================================
# 
# cars = ['bmw', 'volvo', 'audi', 'cadillac']
# car = input('Qanday mashina haydamoqchisiz? ')
# if car.lower() in cars:
#     print('Mashinangiz tayyor!')
# else:
#     print('Uzr, bu mashina mavjud emas!') 
#     
# =============================================================================


# =============================================================================
# 
# cars = ['bmw', 'volvo', 'audi', 'cadillac']
# car = input('Qanday mashina haydamoqchisiz? ')
# if car.lower() not in cars:
#     print('Uzr, bu mashina mavjud emas!') 
# else:
#     print('Mashinangiz tayyor!')
#     
# =============================================================================


    
# =============================================================================
# rasta = ['gul', 'qand', 'kiyim', 'nos', 'meva']
# bozorlik = []
# 
# 
# if bozorlik:
#     for narsa in bozorlik:
#         if narsa in rasta:
#             print(f'{narsa} rastada bor.')
#         else:
#             print(f'{narsa} rastada mavjud emas.')
# else:
#     print("Ro'yxat bo'sh.")
# =============================================================================


    

    
    
    
    
                                                                                                                                                                            



















