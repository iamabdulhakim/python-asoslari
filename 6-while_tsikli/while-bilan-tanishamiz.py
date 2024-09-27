# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 15:57:48 2024

@author: Saidus_work
"""

            # WHILE TSIKLI BILAN TANISHAMIZ #
            

# input()

# =============================================================================
# ism = input("Ismingiz nima ? ")
# print(f'Salom {ism.title()}!')
# =============================================================================

#

# =============================================================================
# ism = input("Ismingiz nima ? ")
# savol = f'Salom {ism.title()}. Yoshingiz nechida? '
# yosh = input(savol)
# =============================================================================

# Sonlar va input()

# =============================================================================
# ism = input("Ismingiz nima ? ")
# savol = f'Salom {ism.title()}. Yoshingiz nechida? '
# yosh = int(input(savol))
# height = input("Bo'yingiz necha metr? ")
# height = float(height)
# =============================================================================

# While 

# =============================================================================
# son = 1 
# while son <= 12:
#     print(son)
#     #son += 1
#     son = son + 1
# =============================================================================
    
# While va input()

# =============================================================================
# print("\nKiritilgan sonning kvadratini qaytaruvchi dastur.\n")
# savol = "Istalgan sonni kiriting: "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing.)\n"
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print('Dastur to\'xtadi.') 
# =============================================================================

# Ishora (flag)

# =============================================================================
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print("Dastur to'xtadi.")
# =============================================================================



# BREAK OPERATORI

# =============================================================================
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# 
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)
# =============================================================================
        
# 

# =============================================================================
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     else:
#         print(f'Sonning kvadrati - {son**2} ga teng.')
#         
# =============================================================================

# CONTINUE OPERATORI

# =============================================================================
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")
# =============================================================================
    
#

# =============================================================================
# son = 0
# while son < 10:
#     son = son +1
#     if son%2 != 0:
#         continue
#     else:
#         print(son)
# =============================================================================
        
        
#  ABADIY TSIKL TUZOG'I

# =============================================================================
# # infinite loop
# son = 0
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)
# =============================================================================
    
# 

# =============================================================================
# son = 1
# while son>0: 
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)
# =============================================================================
        


            # AMALIYOT #


#1    Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang. 
  # Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating.
  

# =============================================================================
# qiymat = ''
# while qiymat != 'stop':
#     qiymat = input("\nYaxshi ko'rgan kitobingiz nomini kiriting.\n"
#                    "(Dasturni to'xtatish uchun 'stop' deb yozing!):\n").lower()
#     if qiymat != 'stop':
#         print(f'Qoyil, "{qiymat.title()}" ajoyib kitob.')
# print("Raxmat.")
# =============================================================================


#2  Muzeyga kirish uchun chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
 # 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. 
  # Shunday while tsikl yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. 
   # Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
   
   
# =============================================================================
# ishora = True
# while ishora:
#     yosh = input("Yoshingizni kiritinig.(Dastur to'xtashi uchun 'exit' yoki 'quit' deb yozing):\n")
#     if yosh == 'exit' or yosh == 'quit':
#         ishora = False
#     else:
#         yosh = int(yosh)
#         if yosh < 7:
#             narx = 2000
#         elif yosh < 18:
#             narx = 3000
#         elif yosh < 65:
#             narx = 10000
#         else: 
#             narx = 0
#         print(f'Siz uchun kirish narxi - {narx} so\'m.')
# print("Dastur to'xtadi.")
# =============================================================================


#   Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)
   

# =============================================================================
# while True:
#     yosh = input("Yoshingizni kiritinig.(Dastur to'xtashi uchun 'exit' yoki 'quit' deb yozing):\n")
#     if yosh == 'exit' or yosh == 'quit':
#         break
#     else:
#         yosh = int(yosh)
#         if yosh < 7:
#             narx = 2000
#         elif yosh < 18:
#             narx = 3000
#         elif yosh < 65:
#             narx = 10000
#         else: 
#             narx = 0
#         print(f'Siz uchun kirish narxi - {narx} so\'m.')
# print("Dastur to'xtadi.")
# =============================================================================

#

# =============================================================================
# yosh = ''
# while yosh != 'exit' and yosh != 'quit':
#     yosh = input("Yoshingizni kiritinig.(Dastur to'xtashi uchun 'exit' yoki 'quit' deb yozing):\n").lower()
#     if yosh != 'exit' and yosh != 'quit':
#         yosh = int(yosh)
#         if yosh < 7:
#             narx = 2000
#         elif yosh < 18:
#             narx = 3000
#         elif yosh < 65:
#             narx = 10000
#         else: 
#             narx = 0
#         print(f'Siz uchun kirish narxi - {narx} so\'m.')
# print('Dastur to\'xtadi.')
# =============================================================================


#3    Quyidagi dasturda bir nechta mantiqiy xatolar bor. 
 # Jumladan, xusisiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni to'g'rilang ?
 

# =============================================================================
# print("Kiritilgan sonning ildizini qaytaruvchi dastur.\n")
# 
# savol = "Musbat son kiriting. "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing):\n"
# 
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         qiymat = float(qiymat)
#         if qiymat < 0:
#             continue 
#         else:
#             ildiz = float(qiymat)**(0.5)
#             print(f"{qiymat} ning ildizi {ildiz} ga teng")
# print('Dastur to\'xtadi.')       
# =============================================================================
    

   



        
        
        

        
        
    



   




        

        
    


















































