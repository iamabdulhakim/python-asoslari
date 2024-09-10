# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 06:59:00 2024

@author: Saidus_work
"""
# =============================================================================
# 
#         # for TAKRORLASH OPERATORI
# 
# # for BILAN TANISHAMIZ
# 
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
#     
# # for QANDAY ISHLAYDI
# 
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan, Palonchiyevlar oilasi")
# #
# # mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# # for mehmon in mehmonlar:
# # print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
# # print("Hurmat bilan, Palonchiyevlar oilasi\n")
# # 
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 Dekabr kuni nahorga oshga taklif qilamiz")
# print("Hurmat bilan, Palonchiyevlar oilasi\n")
# #
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
#     
#     print(mehmonlar) # bu qator tsikl tashqarisida bo'lishi kerak edi
# #
# mehmonlar = ['Ali','Vali','Hasan', 'Husan','Olim']
# for mehmon in mehmonlar:
#     print(mehmon)
#     
# print(mehmonlar)
# 
# # for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH
# 
# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")
# #
# sonlar = list(range(11)) # 1 dan 10 gacha sonlar ro'yxatini yaratamiz
# sonlar_kvadrati =[] # bo'sh ro'yxat yaratamiz
# for son in sonlar:  # sonlar dagi har bir son uchun
#     sonlar_kvadrati.append(son**2) # uning kv.ni hisoblab, sonlar_kvadrati ga yuklaymiz
# 
# print(sonlar)
# print(sonlar_kvadrati)
# 
# #  for va input()
# dostlar = []
# print("5 ta eng yaqin do'stingiz kim?")
# for n in range(5):
#     dostlar.append(input(f'{n+1} - do\'stingizni ismimi kiriting: '))
# 
# print(dostlar)
# 
#                                                                    
# =============================================================================


# AMALIYOT

# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing

ismlar = ['Ali','Umar','Anvar','Bobur','Sodiq']
for ism in ismlar:
    print('Salom ',ism,' qalaysan!')
    print('Hayr ',ism)
    
# Yuqoridagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring    
  # (n o'rniga kod necha marta takrorlanganini yozing)

print('\nKod ',len(ismlar),' marta takrorlandi.\n')

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing.
   # Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.

toq_sonlar = list(range(11,100,2))
for son_kubi in toq_sonlar:
    print(f'{son_kubi} ning kubi - {son_kubi**3} ga teng.')
    
# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang va kinolar degan ro'yxatga saqlab oling. 
   # Natijani konsolga chiqaring.    
# =============================================================================
# 
# kinolar = []
# print('Eng sevimli kinolaringiz qaysilar?')
# for n in range(5):
#     kinolar.append(input(f'{n+1} - kinoni kiriting: '))
# print(kinolar)
# 
# =============================================================================

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, 
 # va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. 
  # Ro'yxatni konsolga chiqaring.

n_o = int(input('Bugun nechta odam bilan gaplashdingiz?: '))
odamlar = []
for n in range(n_o):
    odamlar.append(input(f' {n+1} - odam:'))
print(odamlar)    
        

























