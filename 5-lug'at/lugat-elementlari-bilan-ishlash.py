# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 15:01:32 2024

@author: Saidus_work
"""

# =============================================================================
# 
# # LUG'AT ELEMENTLARI BILAN ISHLASH
# 
# 
# # .items() METODI
# 
# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }
# 
# print(talaba_0.items())
# 
# #
# 
# for kalit, qiymat in talaba_0.items():
#     print(f'Kalit: {kalit}')
#     print(f'Qiymat: {qiymat}\n')
#     
# #
# 
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
# 
# for k, q in telefonlar.items():
#     print(f'{k.title()} ning telefoni {q}.')
#     
# # .keys() METODI
# 
# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
#     
# print(mahsulotlar.keys())
# 
# #
# 
# print("Do'kondagi mahsulotlar:")
# 
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())
# 
# 
# print("Do'kondagi mahsulotlar:")
# 
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())
# 
# #
# 
# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f'{mahsulot.title()} {mahsulotlar[mahsulot]} so\'m ')
#         
# for mahsulot in bozorlik:
#     if mahsulot not in mahsulotlar:
#         print(f"Do'koningizga {mahsulot} ham olib keling! ")
#         
# 
# # LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
# 
# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':25000,
#     'shaftoli':30000
#     }
# print("Do'kondagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())
# 
#     
# # .values() METODI
# 
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }
# print(telefonlar.values())
# 
# #
# print('Foydalanuvchilarning telefonlari:')
# for tel in telefonlar.values():
#     print(tel)
# 
# #
# 
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'hamida':'galaxy s9',
#     'maryam':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'    
#     }
# print('Foydalanuvchilarning telefonlari:')
# for tel in telefonlar.values():
#     print(tel)
# 
# # 
# 
# print('Foydalanuvchilarning telefonlari:')
# for tel in set(telefonlar.values()):
#     print(tel)
#     
#     
# # SET ma'lumot turi
# 
# toys = {'car', 'ball', 'lamp', 'ball', 'pazl', 'car'}
# print(toys)
# =============================================================================
    
# =============================================================================
# 
#  Pythonda set yana bir ma'lumot turi bo'lib, ro'yxat va lug'at kabi bir nechta 
#   elementlarni saqlashga mo'ljallangan. Lug'at va ro'yxatdan farqli ravishda, 
#    set ichidagi elementlar biror tartibda saqlanmaydi, 
#     va ularga indeks orqali murojat qilib bo'lmaydi. 
#     Shuningdek, set ichida bir hil elementlar bo'lmaydi.
#     
# =============================================================================


        # AMALIYOT #


#1    Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
 # Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida 
  # chiroyli qilib konsolga chiqaring.

python_izohli_lugati = {'integer':"butun son",
                        'float':"o'nlik son",
                        'string':"matn",
                        'if':"agar",
                        'else':"aks holda",
                        'elif':"aks holda agar",
                        'true':"rost",
                        'talse':"yolg'on",
                        'and':"va",
                        'or':"yoki"
                        }


for k, q in sorted(python_izohli_lugati.items()):
# =============================================================================
#     print(f'Kalit: {k.title()}')
#     print(f'Qiymat: {q}\n')
# =============================================================================
    print(f'{k.title()} - {q}')
    

#2    Davlatlar va ularning poytaxtlari lug'atini tuzing. 
  # Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, 
    # alifbo ketma-ketligida konsolga chiqaring.
    
davlatlar = {"o'zbekiston":"toshkent",
             "rossiya":"moskva",
             "korea":"seoul",
             "fransiya":"parij",
             "hindiston":"dehli",
             "turkiya":"istanbul"
             }

print('<<<< Davlatlar >>>> ')
for k in sorted(davlatlar.keys()):
    print(k.upper())

print('<<<< Poytaxtlar >>>> ')
for q in sorted(davlatlar.values()):
    print(q.title())


#3    Foydalanuvchidan istalgan davlatni kiritishni so'rang 
 # va shu davlatning poytaxtini konsolga chiqaring. 
  # Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
   # "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring
 
   
# =============================================================================
# davlat = input('Istalgan davlatni kiriting: ').lower()
# if davlat in davlatlar.keys():
#     print(f'{davlat.upper()} ning poytaxti - {davlatlar[davlat].title()}.')
# else:
#     print("Bizda bunday ma'lumot yo'q!")
# =============================================================================
    

# =============================================================================
# davlat = input('Istalgan davlatni kiriting: ').lower()
# poytaxt = davlatlar.get(davlat)  
# if poytaxt == None:
#     print("Bizda bunday ma'lumot yo'q!")
# else:
#     print(f'{davlat.upper()} ning poytaxti - {poytaxt.title()}.')
# =============================================================================
    


#4    Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
 # Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
  # Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, 
   # agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" 
    # degan xabarni chiqaring.
    
menyu = {
    'osh':15000,
    'shashlik':13000,
    'somsa':7000,
    'langet':22000,
    'jiz':25000,
    'qozonkabob':17000,
    'sho\'rva':16000,
    'lag\'mon':19000,
    'chuchvara':20000,
    'manti':5000
    }

print('3 xil ovqat buyurtma bering:')
buyurtma = []
for n in range(3):
    buyurtma.append(input(f'{n+1} - taomni kiriting: ').lower())


for taom in buyurtma:
    if taom in menyu.keys():
        print(f'{taom.upper()} ning narxi {menyu[taom]} so\'m. ')
    else:
        print(f'Bizda {taom.upper()} yo\'q! ')

    

    

    
    

    
    
    
    
 

    
    



















































