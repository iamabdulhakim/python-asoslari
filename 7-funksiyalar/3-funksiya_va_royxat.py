# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 15:11:10 2024

@author: Saidus_work
"""

            # FUNKSIYA VA RO'YXAT #
            

# Funksiyaga ro'yxat uzatish

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#         baholar[ism] = int(baho)
#     return baholar

# talabalar = ["ali", "vali", "hasan", "husan"]
# baholar = bahola(talabalar)
# print(baholar)

# Funksiyaga o'zgartirish kiritish

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar)
# print(talabalar)

# Asl ro'yxatga o'zgartirish kiritishning oldini olish.

# talabalar = ['ali', 'vali', 'hasan', 'husan']
# baholar = bahola(talabalar[:])
# print(talabalar)


            # AMALIYOT #
            
            
#1  Matnlardan iborat ro'yxat qabul qilib, 
# ro'yxatdagi har bir matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.

def katta_harf(matnlar):
    n = list(range(len(matnlar)))
    for i in n:
        matnlar[i] = matnlar[i].title()
     
buyumlar = ["mashina", "raketa", "telefon"]
katta_harf(buyumlar)
print(buyumlar)


#2  Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan 
# va yangi ro'yxat qaytaradigan qilib o'zgartiring.

def katta_harf(matnlar):
    matnlar1 = []
    for matn in matnlar:
        matn = matn.title()
        matnlar1.append(matn)
    return matnlar1

mashinalar = ["zil", "gaz53", "kamaz", "ural", "gazel"]
cars = katta_harf(mashinalar)
print(mashinalar)
print(cars) 



def katta_harf(matnlar):
    matnlar1 = []
    while matnlar:
        matn = matnlar.pop()
        matnlar1.append(matn.title())
    return matnlar1

mashinalar = ["zil", "gaz53", "kamaz", "ural", "gazel"]
cars = katta_harf(mashinalar [:])
print(mashinalar)
print(cars)


#3 Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan foydalanmasdan va asl 
# ro'yxatga o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

def bahola(ismlar):
    baholar = {}
    for ism in ismlar:
        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        baholar[ism.title()] = int(baho)
    return baholar

talabalar = ["ali", "vali", "hasan", "husan"]
baholar = bahola(talabalar)
print(talabalar)
print(baholar)








        







    




















