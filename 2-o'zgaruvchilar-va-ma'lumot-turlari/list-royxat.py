# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:06:01 2024

@author: Saidus_work
"""

# =============================================================================
# #  LIST (RO'YXAT)
# 
# mevalar = ["olma ", "anjir ", "shaftoli", "o'rik "] #  mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000]  # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5]   # sonlar va matnlar-aralash ro'yxat
# ismlar = [] # bo'sh ro'yxat
# 
# mevalar = ["olma ","anjir ","shaftoli ", "o'rik"]
# print('Birinchi meva: ', mevalar[0])
# print('Ikkinchi meva: ', mevalar[1])
# #
# mevalar = ["olma ","anjir ","shaftoli ", "o'rik"]
# print('Birinchi meva: ', mevalar[0].title())
# print('Ikkinchi meva: ', mevalar[1].upper())
# #
# narhlar = [12000, 18000, 10900, 22000]
# print(narhlar[2] + narhlar[3])
# # 
# car_models = ['Toyota', 'GM', 'Volvo', 'BMW', 'Hyundai', 'Kia', 'Volkswagen']
# print(car_models[-1]) # Listning eng oxirgi elementiga -1 bilan murojat qilamiz 
# 
# ##################
# 
# # Elementni o'zgartirish
# 
# narhlar = [12000, 18000, 10900, 22000]
# narhlar[0] = 13000
# narhlar[2] = 11000
# narhlar[3] = narhlar[3] + 2000
# print(narhlar)
# 
# # Yangi element qo'shish
# 
# mevalar = ["olma ","anjir ","shaftoli ", "o'rik"]
# mevalar.append('tarvuz')
# print(mevalar)
# #
# cars = []
# cars.append('Lacetti')
# cars.append('Nexia 3')
# cars.append('Cobalt')
# print(cars)
# #
# cars = ['Lacetti', 'Nexia 3', 'Cobalt']
# cars.insert(0, 'Malibu')
# print(cars)
# #
# cars.insert(2, 'Damas')
# print(cars)
# 
# # Elementni o'chirish
# 
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# del mevalar[1]
# print(mevalar)
# #
# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# mevalar.remove('shaftoli')
# print(mevalar)
# #
# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
# hayvonlar.remove('mushuk')
# print( hayvonlar)
# 
# # Elementni sug'urib olish
# 
# bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3)
# print('Men ' + mahsulot + ' sotib oldim')
# print('Olinmagan mahsulotlar: ', bozorlik)
# #
# 
# mahsulot = bozorlik.pop()
# print(mahsulot)
# =============================================================================


# AMALIYOT
# quyidagi mashqlarni bajaring:
    
#1 ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
ismlar = ['Ali', 'Hasan', 'Husan', 'G\'ani']

# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:
print('Salom ' + ismlar[0] + ' ishlar yaxshimi!')
print(ismlar[1] + ' va ' + ismlar[2] + ' egizaklar.')
print(ismlar[3] + " g'ildirakni g'izillatib g'ildiratdi.")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
sonlar = [12 , -45 , -6 , 5.4 , 10 ,3.14]
print(sonlar)

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring.
print( sonlar[0] + sonlar[2])
print(sonlar[4] / sonlar[5])
print(sonlar[0] + 8 )

sonlar[2] = 15
sonlar[4] = 8
print(sonlar)

del sonlar[5]
print(sonlar)
sonlar.insert(5, -100)
print(sonlar)

#t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.

t_shaxslar = ['Amir Temur ',' Islom Karimov']
z_shaxslar = ['Shah Rukh Khan ', ' Elon Musk']
print(t_shaxslar , z_shaxslar)
shaxs1 = t_shaxslar.pop(0)
shaxs2 = z_shaxslar.pop(1)

print(f'Men tarixiy shaxslardan {shaxs1} bilan,\nzamonaviy shaxslardan {shaxs2} bilan suhbat qilishni istar edim ')

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.

friends = []
friends.append('Abror ')
friends.append('Vali ')
friends.append('Diyorbek ')
friends.append('Nodir ')
friends.append('Bilol ')
print(friends)

# mehmonga kela olmaydigan odamlar
friends.remove('Vali ')
friends.remove('Nodir ')
print(friends)

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
friends.append('Hoshim ')
friends.insert(0,'Mahmud ')
friends.insert(3,'Sobir ')
print(friends)

# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar = []
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(2))
print('Kelgan mehmonlar: ', mehmonlar)











