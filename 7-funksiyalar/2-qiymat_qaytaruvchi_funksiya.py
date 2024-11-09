# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 06:12:26 2024

@author: Saidus_work
"""



# Funksiyadan oddiy qiymat qaytarish

def toliq_ism_yasa(ism, familiya):
    """Toliq ism qaytaruvchi funksiya"""
    toliq_ism = f"{ism} {familiya}"
    return toliq_ism
    
talaba1 = toliq_ism_yasa("Adulhakim", "Mukhammadov")
talaba2 = toliq_ism_yasa("Hakim", "Olimov")
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}") 

# Ixtiyoriy argumentlar

def toliq_ism_yasa(ism, familiya, otasinig_ismi=''):
    """Toliq ism qaytaruvchi funksiya"""
    if otasinig_ismi:
        toliq_ism = f"{ism} {familiya} {otasinig_ismi}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism

talaba1 = toliq_ism_yasa("ali", 'valiyev')
talaba2 = toliq_ism_yasa("ali", "valiyev", "halimovich")
print(f"Darsga kelmagan talabalar:{talaba1} va {talaba2}")

# Funksiyadan lug'at qaytarish

def avto_info(kompaniya, model, rang, korobka, yil, narx=None):
    avto = {
        "Kompaniya":kompaniya,
        "Model":model,
        "Rang":rang,
        "Korobka":korobka,
        "Yil":yil,
        "Narx":narx
        }
    return avto

avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2020)
avto2 = avto_info("GM", "Gentra", "Oq", "Mexanika", 2018, 16000)
avtolar = [avto1, avto2]
print('Onlayn bozordagi mavjud avtomobillar: ')
for avto in avtolar:
    if avto["Narx"]:
        narx = avto["Narx"]
    else:
        narx = "Noma'lum"
    print(f"{avto['Rang']} {avto['Model']}. Narxi: {narx}")

        
# Funksiyadan ro'yxat qaytarish

# =============================================================================
# def oraliq(min, max):
#     """Ikki son oralig'idagi sonlarni ro'yxat ko'rinishida qaytaruvchi funksiya."""
#     sonlar = []
#     while min < max:
#         sonlar.append(min)
#         min += 1 
#     return sonlar
# 
# print(oraliq(1, 10))
# print(oraliq(10, 25))
# 
# =============================================================================


def oraliq(min, max, qadam=1):
    """Ikki son oralig'idagi sonlarni ro'yxat ko'rinishida qaytaruvchi funksiya."""
    sonlar = []
    while min < max:
        sonlar.append(min)
        if qadam:
            min += qadam
    return sonlar 

print(oraliq(0, 21))
print(oraliq(0, 21, 2))


# Funksiyalarni tsiklda ishlatish

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting: ")
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rang = input("Rangi: ")
#     korobka = input("Korobka: ")
#     yil = input("Ishlab chiqarilgan yili: ")
#     narx = input("Narxi: ")
    
#     avtolar.append(avto_info(kompaniya, model, rang, korobka, yil, narx))
#     javob = input("Yana avto qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         break

# =============================================================================
# print('Salonimizdagi avtolar:')
# for avto in avtolar:
#     print(f"avto['Model'] - avto['Korobka'].")
# =============================================================================


            # AMALIYOT #
            
#1  Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili 
 # va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. 
 # Lug'atda foydalanuvchi yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling 
 # (masalan, tel.raqam, el.manzil)
 
def info_ol(ism, familiya, t_yil, manzil, email=None, telefon_raqam=None):
    """Foydalanuvchidan ma'lumotlar qabul qilib lug'at qaytaruvchi funksiya"""
    info = {
        "ism" : ism,
        "familiya" : familiya,
        "tug'ulgan yil" : t_yil,
        "yosh" : 2024 - t_yil,
        "manzil" : manzil,
        "email" : email,
        "telefon" : telefon_raqam
        }
    return info

#2  Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, 
 # va mijozlar degan ro'yxatni shakllantiring. 
 # Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
 
# =============================================================================
# print("Mijozlar ro'yxatini shakllantiramiz.")
# mijozlar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting.")
#     ism = input("Ism kiriting: ")
#     familiya = input("Familiya kiriting: ")
#     t_yil = int(input("Tug'ulgan yilni kiriting: "))
#     manzil = input("Manzil kiriting: ")
#     email = input("Email kiriting: ")
#     telefon_raqam = input("Telefon raqam kiriting: ")
#     mijozlar.append(info_ol(ism, familiya, t_yil, manzil, email, telefon_raqam))
#     javob = input("Yana ma'lumot qo'shasizmi?(ha/yo'q)\n")
#     if javob == "ha":
#         continue
#     else:
#         break
#     
# print("\nMijozlar haqida ma'lumotlar:")
# for mijoz in mijozlar:
#     ism = mijoz["ism"]
#     familiya = mijoz["familiya"]
#     t_yil = mijoz["tug'ulgan yil"]
#     yosh = mijoz["yosh"]
#     manzil = mijoz["manzil"]
#     email = mijoz["email"]
#     tel = mijoz["telefon"]
#     print(f"- {ism.title()} {familiya.title()} {t_yil} - yilda,\n"
#           f"{manzil.title()}da tug'ulgan. Yoshi {yosh} da.\n"
#           f"Uning email va telefoni: {email}, {tel}")
# 
# =============================================================================

#3  Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing.

def katta_sonni_qaytar(son1, son2, son3):
    """Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya."""
    sonlar = [son1, son2, son3]
    return max(sonlar)

katta_son = katta_sonni_qaytar(50, 50, 44-11)
print(f"\nEng katta son: {katta_son}")


#4  Foydalanuvchidan aylaning radiusini qabul qilib olib, 
# uning radiusini, diametrini, perimetri va yuzini 
# lug'at ko'rinishida qaytaruvchi funksiya yozing.

def aylana_hisobla(aylana_radiusi):
    aylana = {
        "radius" : aylana_radiusi,
        "diametr" : 2 * aylana_radiusi,
        "perimetr" : 2 * 3.14 * aylana_radiusi,
        "yuza" : 3.14 * (aylana_radiusi**2)
        }
    return aylana


#5 Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing. 
# (tub sonlar — faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)

def tub_sonlar_top(min,max):    
    tub_sonlar = []    
    for n in range(min,max+1):
        tub = True
        if (n==1):
            tub = False
        elif(n==2):
            tub = True
        else:
            for x in range(2,n):
                if(n%x==0):
                    tub = False
        if tub:
            tub_sonlar.append(n)
                
    return tub_sonlar

a = tub_sonlar_top(1, 10)                
                
#6  Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi 
# sonlar ro'yxatni qaytaruvchi funksiya yozing. 
# Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik 
# Fibonachchi ketma-ketligi deyiladi. 
# Bunda boshlang’ish had ko’pincha 1 deb olinadi. 1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...


def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

print(fibonacci(20))



       
        
        
        
        



        





        
            











    
    



    

    

    











    
 





    

     
     

            
            
    
    

        

    
    






    
 
    





































