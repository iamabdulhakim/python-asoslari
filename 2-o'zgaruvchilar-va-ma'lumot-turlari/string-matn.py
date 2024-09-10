# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 06:24:08 2024

@author: Saidus_work
"""

# =============================================================================
# 
# 
# # String-matn
# 
# shahar = 'кукан'
# viloyat = 'фаргона'
# 
# matn = 'men yangi 📱 oldim'
# smayl = '😁'
#   
# # string ustida amallat
# 
# ism = 'Ahmad'
# print('Mening ismim '+ism)
# 
# ism = 'Ahad'
# familiya = 'Qayum'
# print(ism + familiya)
# print(ism + ' ' + familiya)
# 
# # f-string
# 
# ism = 'Ahad'
# familiya = 'Qayum'
# ism_sharif = f'{ism} {familiya}'
# print(ism_sharif)
# 
# ism = "James"
# familiya = "Bond"
# print(f'Mening ismim {familiya}.{ism} {familiya}')
# 
# # Maxsus belgilar 
# 
# print('Hello world')
# print('Hello\tworld')
# print('Hello\nworld')
# 
# # String metodlar
# 
# ism = 'james'
# familiya = 'bond'
# ism_sharif = f'{ism} {familiya}'
# print(ism_sharif.upper())
# ism_sharif = ism_sharif.upper()
# 
# print(ism_sharif.lower())
# print(ism_sharif.title())
# print(ism_sharif.capitalize())
# 
# ism_sharif = ism_sharif.title()
# 
# meva = '   olma   '
# print(meva)
# print('Men ' + meva.lstrip() + ' yaxshi ko`raman' )
# print("Men " + meva.rstrip() + " yaxshi ko'raman")
# print("Men "+ meva.strip() + " yaxshi ko'raman " )
# print("Men" + meva + "yaxshi ko'raman")
# 
# 
# =============================================================================

# INPUT

# =============================================================================
# 
# # ism = input('Ismingiz nima? ')
# # print('Assalomu alaykum ' + ism )
# 
# ism = input('Ismingiz nima?\n>>>')
# print('Assalomu alaykum ' + ism.upper())
# viloyat = input('Qayerdansiz?n>>>')
# print(viloyat + ' juda go`zal shahar')
# 
# 
# =============================================================================

# Amaliyot 


# Python da quyidagi o'zgaruvchilarni yarating:
    
kocha = "Bog'bon"
mahalla = "Sag'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

# Yuqoridagi o'zgaruvchilarni jamlab  konsolga chiqaring:
    
print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati.")

# yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidadnd so'rang:

# =============================================================================
# print('Iltimos, quyidagi ma\'lumotlarni kiriting!')
# kocha = input("ko'changizni kiriting:")
# mahalla = input("mahallangizni kiriting:")
# tuman = input("tumaningizni kiriting:")
# viloyat = input("viloyatingizni kiriting:")
# 
# =============================================================================
#print(f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati.")

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatordan yoz:
    
#print(f"{kocha} ko'chasi,\n{mahalla} mahallasi,\n{tuman} tumani,\n{viloyat} viloyati.")
 
# Yuqoridagi matnni f-string yordamida, yangi, manzil deb nomlangan o'zgaruvchiga yuklang

manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati."
print(manzil)

# manzil o'zgaruvchisiga biz yuqorida o'rgangan metodlarni qo'llab ko'ring.

manzil = manzil.lower()
print(manzil)
print(manzil.title())
print(manzil.capitalize())
print(manzil.upper())
print(manzil.lower())




































