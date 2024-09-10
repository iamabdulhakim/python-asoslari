# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:13:09 2024

@author: Saidus_work
"""


# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
 # Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
 # Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
 # Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

yosh = int(input('Yoshingiz nechida ? '))
if yosh <= 4 or yosh > 60:
    narx = 0
elif yosh <= 18:
    narx = 10000
else:
    narx = 20000
print(f'Sizga chipta {narx} so\'m. ')


 

















