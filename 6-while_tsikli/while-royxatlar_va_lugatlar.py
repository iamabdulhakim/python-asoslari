# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 20:44:37 2024

@author: Saidus_work
"""


            # While sikli, roʻyxatlar va lugʻatlar #
            
            
# WHILE YORDAMIDA RO'YXATNI TO'LDIRISH

# =============================================================================
# ismlar = []
# 
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.\n")
# n = 1  # ismlarni sanash uchun 
# while True:
#     savol = f"{n} - do'stingizning ismini kiriting:\n"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)\n")
#     if javob == 'ha':
#         n = n+1
#         continue
#     else:
#         break
#     
# print("\nDo'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())
# =============================================================================
    
    
# WHILE YORDAMIDA LUG'ATNI TO'LDIRISH

# =============================================================================
# print("\nDo'stlaringiz yoshini saqlaymiz.\n")    
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingizning ismini kiriting:\n")
#     yosh = input(f"{ism.title()} ning yoshini kiriting:\n")
#     dostlar[ism] = int(yosh)  # ism - kalit; yosh - qiymat.
#     j = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)\n")
#     if j == "yo'q":
#         ishora = False
#         
# print('\nDo\'stlaringiz yoshi haqida ma\'lumot.')        
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} ning yoshi {yosh} da.")
# =============================================================================
    
    
# RO'YXAT ELEMENTLARINI O'CHIRISH


# =============================================================================
# cars = ['lacetti','nexia','toyota','nexia','audi' 'lacetti','malibu','nexia']
# car = "nexia"
# while car in cars:
#     cars.remove(car)
# print(cars)
# =============================================================================
    

# RO'YXATDAN RO'YXATGA (LUG'ATGA) ELEMENT KO'CHIRISH

# =============================================================================
# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholanganlar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting:\n")
#     print(f"{talaba.title()} baholandi.\n")
#     baholanganlar[talaba] = int(baho)
# =============================================================================
    
    
                # AMALIYOT #


#1   Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. 
 # Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

# =============================================================================
# buyurtmalar = []
# n = 1
# print("\nBuyurtmalarni qabul qiluvchi dastur.\n")
# while True:
#     savol = f"{n} - buyurtmangiz nima?\n>>> "
#     buyurtma = input(savol).lower()
#     buyurtmalar.append(buyurtma)
#     javob = input("Yana buyurtma berasizmi!? (ha/yo'q)\n")
#     if javob == "ha":
#         n = n+1
#         continue
#     else:
#         break
# print("\nBuyurtmangiz qabul qilindi!")
# =============================================================================


#2   e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. 
 # Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.

# =============================================================================
# print("Mahsulotlar va ularning narxlarini shakllantiruvchi dastur.\n")
# mahsulotlar = {}
# ishora = True
# while ishora:
#     mahsulot = input("Mahsulot nomini kiriting: ").lower()
#     narx = int(input(f"{mahsulot.title()}ning narxini kiriting: "))
#     mahsulotlar[mahsulot] = narx
#     javob = input("Yana mahsulot qo'shasizmi? (ha/yo'q)\n")
#     if javob == "ha":
#         continue
#     else:
#         ishora = False
# print("\nRahmat, ma'lumotlar qo'shildi!")
# 
# =============================================================================

#3   Yuqoridagi ikki dasturni jamlaymiz. 
 # Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni 
 # e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). 
 # Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, 
 # aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

# =============================================================================
# buyurtmalar = ['telefon', 'kitob', 'non', 'shirinlik', 'krossovka', 'soat', 'sumka']
# mahsulotlar = {'kitob': 45000, 'kurtka': 300000, 'soat': 100000, 'gul': 80000, 'telefon': 5000000, 'sumka': 150000}
# 
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         print(f"{buyurtma.title()}ning narxi - {mahsulotlar[buyurtma]} so'm.") 
#     else:
#         print(f"Bizda {buyurtma.title()} mavjud emas!")
# =============================================================================
        

        
        
        




    
    


    
    
    






















