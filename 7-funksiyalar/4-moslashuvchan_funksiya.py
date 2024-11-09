# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 21:21:47 2024

@author: Saidus_work
"""


               # MOSLASHUVCHAN FUNKSIYA (*args, **kwargs) #


#  *args USULI
               
def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    yigindi = 0
    for son in sonlar:
        yigindi = yigindi + son
    return yigindi

print(summa(1,2))
print(summa(1,2,3,4,5))
print(summa(2,5,78,34,12))
#
def summa(x, y, *sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return x+y+sum(sonlar)

print(summa(5, 9, 12, 3, -2, 0.3, -12, 4, 6))
# print(summa(2))
print(summa(2, 3))



#  **kwargs USULI

def avto_info(kompaniya, model, **malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar["kompaniya"] = kompaniya
    malumotlar["model"] = model
    return malumotlar

avto1 = avto_info("GM", "Malibu", rang = "qora", yili = 2021)
avto2 = avto_info("Kia","K5", rang = "qizil", narx = 35000)



                 # AMALIYOT #
                 
#1  Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing.

def kopaytir(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma = kopaytma * son
    return kopaytma

print(kopaytir(1,2,3))
print(kopaytir(1))
print(kopaytir(0))
print(kopaytir())
print(kopaytir(-4, 6, 15, 5.8, 9, -6))
print(kopaytir(23.4, 78.1, 8.3))
print(kopaytir(4,5,6))


#2  Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. 
# Talabaning ismi va familiyasi majburiy argument, 
# qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.


def talaba_info(ism, familiya, **info):
    info["ism"] = ism.title()
    info["familiya"] = familiya.title()
    return info

talaba = talaba_info("ali", "valiyev", yosh = 20, manzil = "namangan", kurs = 2)








                

















