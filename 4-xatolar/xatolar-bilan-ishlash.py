# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 14:31:28 2024

@author: Saidus_work
"""

            #--------XATOLAR BILAN ISHLASH---------------#

# Xatolar 3 turli bo'ladi:
    
# 1. SYNTAX ERROR

      # Syntax error - dasturlash tili qoidalarga amal qilmaslik natijasida 
#kelib chiqadigan xatolik.
# print 'Hello world!'
# print('Hello world!')
    # EOL va EOF xatolik: 1. EOL (End of Line - qator yakuni) xatoligi sytax error ning bir turi 
#bo'lib, odatda qator oxirida qo'shtirnoq yoki birtirnoqni yopish esdan chiqqanda yuzaga keladi.
# print("Hello world!)
# print('Hello world!')
# 2. EOF (End of function - funktsiya yakuni) xatoligi esa f-ya oxirida qavsni yopish esdan 
#chiqqanda yuzaga keladi.
# print('Hello world'
# print('Hello world')

# 2. INDENTATION ERROR

    # Python da qator boshidan yozish yoki joy tashlab yozish muhim ahamiyatga ega. Qator boshidan
#asossiz joy qoldirish IndentationError ga olib keladi. Ba'zi joylarda aksincha, bo'sh joy
#tashlab yozish talab qilinadi. Masaln for tsiklida yoki if-elif-else shartlari ichida va h.k.

# print('10 gacha sanaymiz.')
# for n in range(0,10):
#     print(n+1)
    
# son = -50 
# if son  >= 0:
#     print('Musbat son.')
# else:
#     print('Manfiy son.')

# 3. RUN TIME ERROR

    # Run time error - dasturni bajarish jarayonida kelib chiqadi. Syntax error dan farqli 
#ravishda, Python bunday xatolarni dastur bajarilishidan avval aniqlay olmaydi. Run time error ni
#bir nechta turlari bor: 
    # 1. Type error - biror amalni (f-ya, metod, ifoda) noto'g'ri ma'lumot
#turi ustida bajarish. 
# son = input('Istalgan son kiriting: ')
# print(f'{son} ning kvadrati {son**2} teng. ')  
# son = float(input('Istalgan son kiriting: '))
# print(f'{son} ning kvadrati {son**2} teng. ')
    # 2. Name error - o'zgaruvchi, f-ya, obyekt nomini noto'g'ri yozish natijasiga kelib chiqadi.
# prit('Hello world!')
# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mvalar:
#     print(meva)
    # 3. Value error - f-ya ga noto'g'ri qiymat yuborish natijasidagi xatolik.
# son = int(input("Istalgan son kiriting: "))
# if son>=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")
    # 4. Index Error - ro'yxat elementlariga murojaat qilishda noto'g'ri qiymat kiritish.
# mevalar = ['olma','anor','uzum']
# print(mevalar[3])
    # 5. Zero Division Error - dastur jarayonida 0 ga bo'lish yuzaga kelgandagi xatolik.
# x, y = 50, 50
# z = 250/(x-y)

# 4. MANTIQIY XATOLAR

    # Mantiqiy xatolar - dasturchi tomonidan yo'l qo'yilgan va kutilgan natijani berishda
#to'sqinlik qiluvchi xatolar. Bunday xatolar eng ko'p uchraydi va ularni aniqlash qiyin bo'ladi.
#Aksar holatlarda Python mantiqiy xatolarni aniqlamaydi va dastur bajarilaveradi
#(lekin kutilgan natija chiqmaydi).
            
                # MISOLLAR #
                
# radius = 5
# pi = 4.14
# aylana_yuzi = pi*radius**2
# print(aylana_yuzi)
# Bu yerda natija xato chiqadi, chunki "pi = 3.14" bo'lishi kerak edi.

# son = float(input("Istalgan son kiriting: "))
# ildiz = son**1/2
# print(f"{son} ning ildizi {ildiz} ga teng")
# Bu yerda ham natija xato chiqadi, "ildiz = son**(1/2)"bo'lishi kerak edi.

# mevalar = ['olma','uzum','nok','anor','anjir']
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi")
# Yuqorida "Dastur tugadi" matni bir marta, dastur tugaganidan so'ng chiqishi kerak edi. 
#Lekin o'ngga suriib qolgani uchun bir necha bor qaytarildi.


                # Amaliyot #

# =============================================================================
# son = float(input("Juft son kiriting: "))
# if son % 2 == 0:
#     print("Rahmat!")
# else:
#     print("Bu son juft emas.")
# =============================================================================

     
# =============================================================================
# yosh = int(input("Yoshingiz nechida?"))
# if yosh<=4 or yosh>=60:
#     narh = 0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")
# 
# =============================================================================


# =============================================================================
# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")
# =============================================================================

    
# =============================================================================
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# 
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# 
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konimizda {mahsulot} yo'q")
# else: 
#     print("Savatingiz bo'sh")            
#     
# =============================================================================

    
# =============================================================================
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# 
# 
# savat = []
# for n in range(5):
#     savat.append(input(f'Savatga {n+1}-mahsulotni qo\'shing: '))
# 
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# 
# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# 
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
# =============================================================================
    

# =============================================================================
# users = ['alisher1983','aziza','yasina' 'umar']
# 
# login = input("Yangi login tanlang:")
# 
# if login.lower() in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print("Xush kelibsiz!")
# =============================================================================

    










































