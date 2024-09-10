# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:24:54 2024

@author: Saidus_work
"""

# Yuqoridagi dasturni quyidagicha o'zgartiring:
 #foydalanuvchidan 5 ta mahsulot kiritishni so'rang. 
  # Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yangi, bor_mahsulotlar degan ro'yxatga,
   # do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing. 
    # Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, 
     # aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.


mahsulotlar = ['go\'sht', 'yog\'', 'un', 'meva', 'pechenye', 'sut', 'telefon', 'idish', 'qog\'oz', 'mato']
savat = []
print('Savatga 5 ta mahsulot kiriting.')
for n in range(5):
    savat.append(input(f'{n+1} - mahsulotni kiriting: '))

bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)
        
if mavjud_emas:
    print("Quyidagi mahsulotlar do'konimizda yo'q: ", mavjud_emas )
else:
    print('Siz so\'ragan mahsulotlar do\'konimizda bor.')

































