# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 22:30:03 2024

@author: Saidus_work
"""
# =============================================================================
# 
# # LUG'AT BILAN ISHLASH
# 
# car_0 = {'model':'ferrari','rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])
# 
# #
# talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2000}
# print(f'{talaba_0["ism"].title()},\
#  {talaba_0["t_yil"]}-yilda tug\'ulgan,\
#  {talaba_0["yosh"]} yoshda.')
# 
# # YANGI JUFTLIK QO'SHISH
# 
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# talaba_0['sharf'] = 'azimovich'
# print(talaba_0) 
# 
# # BO'SH LUG'AT
# 
# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f'Talaba {talaba_1["ism"].title()} {talaba_1["kurs"]} - kurs.')
#    # Lug'atga kalit so'zlar qanday ketma-ketlikda kiritilsa, shu ketma-ketlik saqlanib qoladi.
# 
# # KALIT SO'Z-QIYMAT JUFTLIGINI O'CHIRISH
# 
# talaba_0 = {'ism': 'murod olimov', 'yosh': 20, 't_yil': 2000,
#             'kurs': 4, 'fakultet': 'informatika', 'sharf': 'azimovich'}
# print(talaba_0)
# del talaba_0['sharf']
# print(talaba_0)
#     
# # LUG'ATNI QATORLARGA BO'LIB YOZISH
# 
# telefonlar = {
#     'ali':'i phone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310',
#     'aziz':'redmi'
#     }
# 
# # .get() METODI
# 
# phone = telefonlar['ali']
# print(f'Alining telefoni - {phone}.')
# 
# # =============================================================================
# # phone = telefonlar['bunyod']
# # print(f'bunyod telefoni - {phone}.')
# # =============================================================================
# 
# phone = telefonlar.get('bunyod', 'Bunday ism mavjud emas!')
# print(phone)
# 
# phone = telefonlar.get('vali', 'Bunday ism mavjud emas!')
# print(phone)
# 
# 
# phone = telefonlar.get('bunyod')
# print(phone)
# 
# 
# =============================================================================
        


        # AMALIYOT #
        
#1   otam (onam, akam, ukam, va hokazo) degan lug'at yarating 
 # va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). 
  # Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring.
  
otam = {'ismi':"Jo'rabek", 't_yil':1981, 'manzil':"Namangan"}
print(f'Otamning ismi {otam["ismi"]}, {otam["t_yil"]} - yilda,\
 {otam["manzil"]} viloyatida tug\'ilgan. ')
    
#2 Oila a'zolaringizning sevimli taomlari lug'atini tuzing. 
  #Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. 
    # Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

sevimli_taomlar = {
    'Murod':'somsa',
    'Nargiza':"sho'rva",
    'Ali':'osh',
    'Salima':'manti',
    'Nodir':'norin'
    }

#
taom1 = sevimli_taomlar['Murod']
taom2 = sevimli_taomlar['Ali']
taom3 = sevimli_taomlar['Salima']
print(f'Murodning sevimli taomi {taom1}, Alining sevimli taomi {taom2},\
 Salimaning sevimli taomi {taom3}.')

#
print(f'Murodning sevimli taomi {sevimli_taomlar["Murod"]},\
 Alining sevimli taomi {sevimli_taomlar["Ali"]},\
 Salimaning sevimli taomi {sevimli_taomlar["Salima"]}.')


#3 Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) 
  # kiriting (masalan integer, float, string, if, else va hokazo) 
    # va qiymat sifatida har birining qisqacha tarjimasini yozing.
    
python = {
    'integer':"butun son",
    'float':"o'nlik son",
    'string':"matn",
    'if':"agar",
    'else':"aks holda",
    'elif':"aks holda agar",
    'true':"rost",
    'talse':"yolg'on",
    'and':"va",
    'or':"yoki"
    }

print(python)


#4 Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi
 # lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, 
  # "Bunday so'z mavjud emas" degan xabarni chiqaring.

# =============================================================================
# word = input('Biror so\'z kiriting: ').lower()
# print(python.get(word, 'Bunday so\'z mavjud emas.'))
# =============================================================================


#5 Yuqoridagi vazifani if-else yordamida qiling 
  # va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
  
python = {
    'integer':"butun son",
    'float':"o'nlik son",
    'string':"matn",
    'if':"agar",
    'else':"aks holda",
    'elif':"aks holda agar",
    'true':"rost",
    'talse':"yolg'on",
    'and':"va",
    'or':"yoki"
    }

word = input("Biror so'z kiriting: ").lower()
if word in python:
    print(f"Siz kiritgan so'zning tarjimasi - {python[word]}")
else:
    print(f"{word} so'zi mavjud emas.")
    

    
    
    


    



      
  
















