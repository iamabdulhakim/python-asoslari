# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 06:31:36 2024

@author: Saidus_work
"""

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. 
 # Foydalanuvchidan yangi login tanlashni so'rang va 
  # foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring.
   # Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" 
    # aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.

foydalanuvchilar = ['ahad_qayum', 'anvar', 'abdulhakim', 'elon_musk', 'iamsrk']
yangi_login = input('Yangi login tanlang: ')
yangi_login.lower() in foydalanuvchilar
if yangi_login.lower() in foydalanuvchilar:
    print('Login band, yangi login tanlang!')
else:
    print(f'Xush kelibsiz , {yangi_login.title()}! ')
        

 




 













































