# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 14:37:29 2024

@author: Saidus_work
"""


            # NESTING #
        

# Lug'atlar ro'yxati.

car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }


car = car0
print(f"{car['model'].title()}, {car['rang']} rangda,\
 {car['yil']} - yil, {car['narh']} $ .")
 
car = car1
print(f"{car['model'].title()}, {car['rang']} rangda,\
 {car['yil']} - yil, {car['narh']} $ .")
 
car = car2
print(f"{car['model'].title()}, {car['rang']} rangda,\
 {car['yil']} - yil, {car['narh']} $ .")
 
#

cars = [car0, car1, car2]
for car in cars:
    print(f'\n{car["model"].title()},'
          f'{car["rang"]} rangda, '
          f'{car["yil"]} - yil, '
          f'{car["narh"]}$ .')
    
#

print(cars[2])

print(cars[1]['model'])

print(cars[2]['korobka'])

print(f'{cars[1]["model"].title()}'
      f' {cars[1]["rang"]} rangda.')

#

malibus = []
for n in range(10):
    new_car = {
        'model':'malibu',
        'rang':None,
        'yil':2020,
        'narx':None,
        'km':0,
        'korobka':'avto'
        }
    malibus.append(new_car)
print(malibus)

#

for malibu in malibus[:3]:
    malibu['rang'] = 'qizil'
print(malibus)

for malibu in malibus[3:6]:
    malibu['rang'] = 'qora'
print(malibus)

for malibu in malibus[6:]:
    malibu['rang'] = 'qora'
    malibu['korobka'] = 'mexanika'
print(malibus)

for malibu in malibus:
    if malibu['korobka'] == 'avto':
        malibu['narx'] = 40000
    else:
        malibu['narx'] = 35000
        
for malibu in malibus:
    print(malibu)

# Lug'at ichida ro'yxat.

dasturchilar = {
    'ali':['python','c++'],
    'vali':['html','css','js'],
    'hasan':['php','sql'],
    'husan':['python','php'],
    'maryam':['c++','c#']
    }

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ", end = ' ')
    for til in tillar:
        print(til.upper(), end = '  ')
    
    
# Lug'at ichida lug'at.

hamkasblar = {
    'ali':{'familiya':'valiyev',
           'tyil':1995,
           'malumot':'oliy',
           'tillar':['python','c++']
           },
    'vali':{'familiya':'aliyev',
            'tyil':2001,
            'malumot':"o'rta-maxsus",
            'tillar':['html', 'css', 'js']},
    'hasan':{'familiya':'husanov',
             'tyil':1999,
             'malumot':'maxsus',
             'tillar':['python','php']}
    }

for ism, info in hamkasblar.items():
    print(f"\n{ism.title()} {info['familiya'].title()}, "
          f'{info["tyil"]} - yida tug`ilgan , '
          f'ma\'lumoti {info["malumot"]}.\n'
          'Quyidagi tillarni biladi: ')
    for til in info['tillar']:
        print(til.upper())

           

            # AMALIYOT #
            

#1   Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi 
 # ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, 
  # va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.


shaxs0 = {
    "ism":"aleksandr pushkin",
    "t_yil":1799,
    "millat":"rus"
    }

shaxs1 = {
    "ism":"elon musk",
    "t_yil":1971,
    "millat":"ingliz"
    }

shaxs2 = {
    "ism":"shah rukh khan",
    "t_yil":1965,
    "millat":"hind"
    }

shaxs3 = {
    "ism":"anvar narzullayev",
    "t_yil":1983,
    "millat":"o'zbek"
    }

shaxslar = [shaxs0, shaxs1, shaxs2, shaxs3]

for shaxs in shaxslar:
    print(f'\n{shaxs["ism"].title()} {shaxs["t_yil"]} - yilda tug\'ilgan, ' 
          f'millati - {shaxs["millat"]}.')
    


#2    Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. 
 # For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.
 
 
shaxs0 = {
    "ism":"aleksandr pushkin",
    "t_yil":1799,
    "millat":"rus",
    "asarlar":['Boris Godunov', 'Dubrovskiy', 'Kavkaz asiri']
    }

shaxs1 = {
    "ism":"elon musk",
    "t_yil":1971,
    "millat":"ingliz",
    "asarlar":["The Elon Musk Method", "Elon Musk: Tesla, SpaceX"]
    }

shaxs2 = {
    "ism":"shah rukh khan",
    "t_yil":1965,
    "millat":"hind",
    "asarlar":['Pathaan', 'Fan', 'Jawan']
    }

shaxs3 = {
    "ism":"anvar narzullayev",
    "t_yil":1983,
    "millat":"o'zbek",
    "asarlar":['Data science va sun\'iy intellkt', 'Pythonda dasturlash asoslari']
    }

shaxslar = [shaxs0, shaxs1, shaxs2, shaxs3]

for shaxs in shaxslar:
    ism = shaxs["ism"]
    asarlar = shaxs["asarlar"]
    print(f'\n{ism.title()} ning mashxur asarlari quyidagilar: ')
    for asar in asarlar:
        print(asar)


#3    Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. 
 # Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'atga saqlang. 
  # Natijani konsolga chiqaring.

dostlar_kinosi = {
    "abbos" : ['terminator', 'josuslar', 'muxlis'],
    "nodir" : ['urush va jang', 'ezel', 'pikey'],
    "qodir" : ['taksi', 'tezlik', 'pathaan']
    }

for ism, kinolar in dostlar_kinosi.items():
    print(f"\n{ism.title()} ning sevimli kinolari: ")
    for kino in kinolar:
        print(kino.upper())

#4 Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni 
  # lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

davlatlar = {
    'Uzbekistan' : {
        'poytaxti' : 'toshkent',
        'aholisi' : 37000000,
        'pul birligi' : "so'm",
        'davlat tili' : "o'zbek tili"
        },
    'Rossiya' : {
        'poytaxti' : 'moskva',
        'aholisi' : 144000000,
        'pul birligi' : "rubl",
        'davlat tili' : "rus tili"
        },
    'Angliya' : {
        'poytaxti' : 'london',
        'aholisi' : 68000000,
        'pul birligi' : "funt sterling",
        'davlat tili' : "ingliz tili"
        },
    'Koreya' : {
        'poytaxti' : 'seul',
        'aholisi' : 51814400,
        'pul birligi' : "von",
        'davlat tili' : "koreys tili"
        }
    }

# =============================================================================
# for davlat, info in davlatlar.items():
#     poytaxt = info['poytaxti']
#     aholi = info['aholisi']
#     pul = info['pul birligi']
#     til = info['davlat tili']
#     print(f'\n{davlat.upper()} ning poytaxti - {poytaxt.title()} shahri, '
#           f'aholisi - {aholi} kishi, pul birligi - {pul.upper()}, '
#           f'davlat tili - {til.title()}.')
# =============================================================================



#5    Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, 
  # foydalanuvchi so'ragan davlat haqida ma'lumot bering. 
    # Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" 
      # degan xabarni chiqaring.
      
davlat = input('Qaysi davlat haqida ma\'lumot bilmoqchisiz?\n>>>> ').title()
d = davlatlar.get(davlat)
if d == None:
    print(f"{davlat.upper()} haqida ma\'lumot mavjud emas!")
else:
    print(f'{davlat.upper()} ning poytaxti - {d["poytaxti"].title()} shahri, '
      f'aholisi - {d["aholisi"]}, pul birligi - {d["pul birligi"].title()}, '
      f'davlat tili - {d["davlat tili"].title()}.')
   




    










    
   
    

 









    

 

















































