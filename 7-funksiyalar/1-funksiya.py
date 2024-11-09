# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 19:59:02 2024

@author: Saidus_work
"""

 
                # FUNKSIYA bilan tanishamiz #
                
                
# =============================================================================
# # Funksiya yaratamiz
# 
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print('Assalomu alaykum!')
#     
# salom_ber()
# 
# # Funksiyaga qiymat uzatish
# 
# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
#     
# salom_ber("abdulhakim")
# 
# # Docstring
# 
# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib,
#     unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
#     
# #salom_ber()
# print(salom_ber.__doc__)
# print(type.__doc__)
# print(print.__doc__)
# 
# # Funksiyaga bir necha bor murojaat qilish
# 
# salom_ber("ali")
# salom_ber("vali")
# salom_ber("abdulhakim")
# salom_ber("anvar")
# salom_ber("nodir")
# 
# # Argument va Parametr
# 
# # <<<Funksiya yaratishda, qavs ichida berilgan, 
#  #funksiya to'g'ri ishlashi uchun uzatiladigan qiymat 
#   #parameter deb ataladi.>>>
#   
# # <<<Foydalanuvchi funksiyaga murojat qilishda 
#  #funksiyaga uzatgan qiymat esa argument deb ataladi.>>>
#  
# 
# #  Funksiyaga bir nechta argument uzatish
# 
#          # to'g'ri tartibda uzatish:
#              
# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ismi va familiyasini jamlab chiqaruvchi funksiya."""
#     print(f'Foydalanuvchi ismi: {ism.title()}\n'
#           f'Foydalanuvchi familiyasi: {familiya.title()}')
#     
# 
# toliq_ism("abdulhakim", "mukhammadov")
# toliq_ism("mukhammadov", "abdulhakim")
# 
# #
# 
# def yosh_hisobla(ism, tugulgan_yil):
#     """Foydalanuvchi yoshini hisoblovchi funksiya"""
#     print(f"{ism.title()} {2024 - tugulgan_yil} yoshda.")
#     
# yosh_hisobla("ali", 2005)
# #yosh_hisobla(2005, "ali")
# 
#         # kalit so'z bilan uzatish
#         
# yosh_hisobla(tugulgan_yil=2005, ism="ali")
# toliq_ism(familiya="mukhammadov", ism="abdulhakim")
# 
# 
# # Standart qiymat
# 
# def yosh_hisobla(tugulgan_yil, joriy_yil=2024): 
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil - tugulgan_yil} yoshdasiz.")
#     
# yosh_hisobla(2005, 2024)
# yosh_hisobla(2007)
# 
# 
# # Funksiyaga murojaat qilishda xatoliklar
# 
# # =============================================================================
# # tyil = int(input("Tug'ilgan yilingizni kiriting: "))
# # yosh_hisobla(tyil)
# # =============================================================================
# 
# #
# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# 
# yosh_hisobla(2005,2024)
# 
# #
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
# 
# salom_ber()
# 
# #
# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
#  
# toliq_ism("ali", "valiyev")
# 
# =============================================================================

            # AMALIYOT #
            

#1  Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

def tugilgan_yil(ism, yosh):
    """Foydalanuvchi ismi va yoshini so'rab,
    uning tug'ilgan yilini hisoblaydigan funksiya"""
    print(f"{ism.title()} {2024 - yosh} - yilda tug'ilgan.")
    
tugilgan_yil("ali", 19)
tugilgan_yil(yosh=16, ism="anvar")
tugilgan_yil("vali", 20)

#2   Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.

def kvadrat_va_kub(son):
    """Foydalanuvchidan son olib, uning kvadrati va kubini
    konsolga chiqaruvchi funksiya"""
    print(f"{son} ning kvadrati - {son**2} ga teng, kubi - {son**3} ga teng.")
    
kvadrat_va_kub(2)
kvadrat_va_kub(5)
kvadrat_va_kub(9)
kvadrat_va_kub(-4)
kvadrat_va_kub(0)

#3   Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

def juft_toq(son):
    """Kiritilgan sonning juft yoki toqligini hisoblovchi funksiya"""
    if son %2 == 0:
        print(f"{son} - juft son.")
    else:
        print(f"{son} - toq son.")
        
juft_toq(4)
juft_toq(0)
juft_toq(1)
juft_toq(-6)
juft_toq(5.0)
juft_toq(20)
juft_toq(9)

#4   Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. 
 # Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
 
def son_kattami_tengmi(son1, son2):
    """Kiritilgan ikki sondan kattasini konsolga chiqaruvchi
    yoki sonlar teng bo'lsa 'Sonlar teng' degan xabarni konsolga chiqaruvchi funksiya"""
    if son1 > son2:
        print(f"{son1} soni {son2} dan katta.")
    elif son1 < son2:
        print(f"{son2} soni {son1} dan katta.")
    else:
        print(f"{son1} soni {son2} soniga teng.")
        
son_kattami_tengmi(2, 4)
son_kattami_tengmi(-9, 12)        
son_kattami_tengmi(45.8, 25)
son_kattami_tengmi(-30, -7)
son_kattami_tengmi(60.5, 60.5)
son_kattami_tengmi(9, 9)
son_kattami_tengmi(10*3.5, 20/-4)

#5  Foydalanuvchidan x va n sonlarini olib, x ning n-darajasini konsolga chiqaruvchi funksiya.

def x_n_daraja(x, n=2):
    """x ning n-darajasini hisoblovchi funksiya"""
    print(f"{x} ning {n}-darajasi - {x**n} ga teng.")
    
x_n_daraja(5, 2)
x_n_daraja(-23, 5)
x_n_daraja(2, 6.3)
x_n_daraja(-5, -9)
x_n_daraja(8)
x_n_daraja(-6)


#6  Yuqoridagi funksiyada n uchun 2 standart qiymatini bering. (Yuqorida n=2 bo'ldi.)


#7  Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga 
 # qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. 
 # Natijalarni konsolga chiqaring.

def qoldiqsiz(son):
    """Kiritilgan sonni 2 dan 10 gacha bo'lgan sonlarga 
       qoldiqsiz bo'linishini tekshiruvchi funksiya""" 
    for n in range(2, 11):
        if son%n == 0:
            print(f"{son} soni {n} ga qoldiqsiz bo'linadi.(✔)"
                  f"{son/n}")
        else:
            print(f"{son} soni {n} ga qoldiqsiz bo'linmaydi.(✘)"
                  f"{son/n}")

qoldiqsiz(18)
qoldiqsiz(30)
qoldiqsiz(-5)
qoldiqsiz(9.0)




    
        

 

        



    








    









            
    




 
 


 





 
    
    
    

            
                

                
                






































