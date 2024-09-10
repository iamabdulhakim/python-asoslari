# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 21:56:46 2024

@author: Saidus_work
"""

# =============================================================================
# # RO'YXATLAR BILAN ISHLASH
# 
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort()
# print(cars)
# 
# # cars = ['bmw','mercedes benz', 'volvo', 'Gm', 'tesla', 'audi']
# # cars.sort()
# # print(cars)
# 
# 
# # Ro'yxatni teskari tariblash
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# cars.sort(reverse=True)
# print(cars)
# 
# # asl ro'yxat ichidagi elementlarning ketma-ketligini buzmagan holda ro'yxatni tartiblash
# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh', 'Shamsiddin']
# print('Sorted qaytargan ro\'yxat :', sorted(mehmonlar))
# print('Asl qiymat :', mehmonlar )
# 
# print(sorted(mehmonlar, reverse=True))
# 
# #  sonli ro'yxatlarni ham tartiblash
# ages = [12, 98, 34, 65, 34, 76, 11]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))
# 
# # RO'YXATNI AYLANTIRISH
# 
# fruits = ['pear','banana','apple','watermelon','lemon']
# fruits.reverse()
# print(fruits)
# 
# # RO'YXATNING UZUNLIGINI BILISH - len()
# 
# fruits = ['pear','banana','apple','watermelon','lemon']
# print(len(fruits))
# 
# # range() FUNKTSIYASI
# 
# sonlar = list(range(0,10))
# print(sonlar)
# 
# # range() yordamida qadamni ham berishimiz mumkin:
# juft_sonlar = list(range(0,20,2))    # 0 dan 20 gacha 2 qadam bilan
# toq_sonlat =  list(range(1,20,2))    # 1 dan 20 gacha 2 qadam bilan
# print('Juft sonlar: ', juft_sonlar)
# print('Toq sonlar: ', toq_sonlat)
# 
# # SONLI RO'YXAT USTIDA SODDA AMALLAR
# 
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon = min(narhlar)
# qimmat = max(narhlar)
# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmati ", qimmat, ". Jami: ", jami)
# 
# # RO'YXATNI KESISH
# 
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars = cars[0:3]
# print(my_cars)
# 
# print(cars[1:4])
# 
# # RO'YXATDAN NUSXA OLISH
# sonlar = [1, 2, 3, 4, 5] # donlar degan ro'yxat yaratamiz
# sonlar2 = sonlar # sonlar2 degan ro'yxatni sonlar ga tenglaymiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)
# 
# 
# sonlar = [1, 2, 3, 4, 5] # sonlar degan ro'yxat yaratamiz
# sonlar2 = sonlar[:] # [:] ro'yxatni to'liq ko'chirib oladi
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yxati:", sonlar)
# print("Bu sonlar2 ro'yxati:", sonlar2)
# 
# # TUPLES - O'ZGARMAS RO'YXAT
# 
# tomonlar = (20, 30, 55.2)
# print(tomonlar)
# print(tomonlar[0], tomonlar[2])
# 
# toys = ('bus','car','bear','dino','snake','lizard') # o'zgarmas ro'yxat
# toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# # Ro'yxatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'mcqueen'
# toys = tuple(toys) # Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)
# 
# =============================================================================

# AMALIYOT

# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
davlatlar = ['o\'zbekiston', 'Rossiya', 'Koreya', 'Xiyoy', 'Suriya', 'Arabiston']
print(davlatlar)

#1 Ro'yxatning uzunligini konsolga chiqaring
print(len(davlatlar))
#2 sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(davlatlar))
#3 sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(davlatlar, reverse=True))
#4 Asl ro'yxatni qaytadan konsolga chiqaring
print(davlatlar)
#5 reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
davlatlar.reverse()
print(davlatlar)
#6 sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
juft_sonlar = list(range(120,1201,2))
print(juft_sonlar)

#1 Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(juft_sonlar))
#2 Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
print("Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirma: ",max(juft_sonlar)-min(juft_sonlar) )
#3 Ro'yxatdagi elementlar sonini hisoblang
print(len(juft_sonlar))
#4 Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(juft_sonlar[0:20])
print(juft_sonlar[260:280])
print(juft_sonlar[-20:])

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar = ['qaymoq', 'shashlik', 'kalbasa', 'somsa', 'lavash']

# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta = taomlar[:]
print(nonushta)

# yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring va yana 2ta taom qo'shing
nonushta.remove('shashlik')
nonushta.remove('somsa')
nonushta.remove('lavash')
nonushta.append('saryog\'')
nonushta.append('pechenye')

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta = tuple(nonushta)
print(nonushta)
nonushta[2] = 'qaymoq va non '


                
        





