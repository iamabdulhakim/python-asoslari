# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 16:12:19 2024

@author: Saidus_work
"""


# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. 
 # Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. 
  # Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring 
   # va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, 
    # "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.

# =============================================================================
# mahsulotlar = ['go\'sht', 'yog\'', 'un', 'meva', 'pechenye', 'sut', 'telefon', 'idish', 'qog\'oz', 'mato']
# savat = []
# print('Savatga 5 ta mahsulot kiriting! ')
# for n in range(5):
#     savat.append(input(f'{n+1} - mahsulotni kiriting: '))
# print(savat)   
# 
#  
# for mahsulot in savat: 
#     if mahsulot in mahsulotlar:
#       print(f'{mahsulot} do\'konimizda bor.')
#     else:
#       print(f'{mahsulot} do\'konimizda yo\'q.' )
# =============================================================================


mahsulotlar = ['go\'sht', 'yog\'', 'un', 'meva', 'pechenye', 'sut', 'telefon', 'idish', 'qog\'oz', 'mato']
savat = []
print('Savatga 5 ta mahsulot kiriting.')
for n in range(5):
    savat.append(input(f'{n+1} - mahsulotni kiriting: '))

for mahsulot in savat:
    if mahsulot in mahsulotlar:
        print(f'{mahsulot} do\'konimizda bor.')
    else:
        print(f'{mahsulot} do\'konimizda yo\'q')
    



































