
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 19:57:58 2024

@author: Saidus_work
"""

        # TO'PLAMLAR #

# To'plam bilan tanishish

#       
sonlar = {1,2,3}
print(sonlar)

ismlar = {'anvar', 'ali', 'umar'}
print(ismlar)

#
sonlar = {1,2,3,3,4,4,5,6,5}
print(sonlar)

sonlar1 = {4,5,6,5,1,3,4,7,2,3,8}
print(sonlar1)

cars = {'zil', 'kamaz', 'gazel', 'zil', 'ural', 'mers', 'gazel'}
print(cars)

#
a = set()
b = set()

# =============================================================================
# #
# sonlar = {1,2,3,3,4,4,5,6,5}
# print(sonlar[0])
# =============================================================================

#
mevalar = ['olma', 'anjir', 'olma', 'uzum', 'olma', 'uzum']
mevalar = set(mevalar)
print(mevalar)

mevalar = list(mevalar)
print(mevalar)

# to'plamga element qo'shish

mevalar = {'olma', 'anjir', 'uzum'}
mevalar.add('banan')
print(mevalar)

mevalar.update(['anor', 'qovun'])
print(mevalar)
mevalar.update(['sliva'])
print(mevalar)
mevalar.update({'kivi'})
print(mevalar)

# to'plamdan element o'chirish

mevalar = {'anjir', 'olma','uzum','banan', 'anor'}

mevalar.discard('anjir')
print(mevalar)
 
mevalar.remove('banan')
print(mevalar)

#

sonlar = {1,2,3,4,5,6}

sonlar.discard(7)
print(sonlar)

# =============================================================================
# sonlar.remove(7)
# print(sonlar)
# 
# =============================================================================

#

sonlar = {1,2,3,4,5,6}
son = sonlar.pop()
print(son)
print(sonlar)


# To'plam ustida amallar

A = {1,2,3,4}
B = {3,4,5,6}
J = {7,8,9,10}
C = A | B | J
print(C)

D = A.union(B,J)
print(D)

#

A = {1,2,3,4}
B = {3,4,5,6}

print(A & B)

print(A.intersection(B))

#

A = {1,2,3,4}
B = {3,4,5,6}

print(A - B)

print(B.difference(A))

#

A = {1,2,3,4}
B = {3,4,5,6}

print(A ^ B)

print(A.symmetric_difference(B))


            # AMALIYOT #
            
#1    Uch xil ranglar nomi saqlangan to'plam yarating.

ranglar = {'yashil', 'sariq', 'qizil'}
print(ranglar)

#2    To'plamga .add() va .update() metodlari yordamida ranglar qo'shing.

ranglar.add("ko'k")
print(ranglar)

ranglar.update(['oq', 'qora'])
print(ranglar)

#3    Quyidagi ikki to'plam uchun umumiy elementlarni ajratib olib, yangi to'plam yarating.

set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

print(set1 & set2)

set3 = set()
set3.update(set1 & set2)
print(set3)


#4    Yuqoridagi ikki to'plam orasidagi farqlarni konsolga chiqaring.

set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

print(set1 - set2)
print(set2.difference(set1))

#5    Ikki to'plam orasidagi simmetrik farqni toping.

set1 = {10,20,30,40,50}
set2 = {30,40,50,60,70}

print(set1 ^ set2)
print(set2.symmetric_difference(set1))

#6    Sotib olinishi kerak bo'lgan mahsulotlarning qay biri do'konda bor ekanini 
  # alohida ro'yxatga (list) saqlang.

# bozorlik - sotib olinishi kerak bo'lgan narsalar.
# mahsulotlar - do'kondagi mavjud mahsulotlar.


bozorlik = ['choy', 'non', 'kartoshka', 'tuxum', 'sut']
mahsulotlar = ['non', 'sut', 'tuxum', 'olma', 'un', 'tuz']
bozorlik = set(bozorlik)
mahsulotlar = set(mahsulotlar)

list1 = []
list1 = set()

list1.update(bozorlik.intersection(mahsulotlar))
list1 = list(list1)
print(list1)

# =============================================================================
# # ASLIDA 2 RO'YXATDAGI 1 XIL ELEMENTLARNI TOPISH UCHUN - for mahsulot in bozorlik:
#     #                                                      if mahsulot in mahsulotlar:
#         #     birxil_elemetlar[]                             birxil_elemetlar.append(mahsulot)  
#             #                                                 print( birxil_elemetlar)  
#  SHU USUL QULAYROQ.
# 
# =============================================================================
                  

#7    Do'konda mavjud bo'lmagan mahsulotlar ro'yxatini yarating.

bozorlik = ['choy', 'non', 'kartoshka', 'tuxum', 'sut']
mahsulotlar = ['non', 'sut', 'tuxum', 'olma', 'un', 'tuz']
bozorlik = set(bozorlik)
mahsulotlar = set(mahsulotlar)

dokonda_yoqlar = set()
dokonda_yoqlar.update(bozorlik - mahsulotlar)
dokonda_yoqlar = list(dokonda_yoqlar)
print(dokonda_yoqlar)

#8    Do'kon egasi so'ralgan mahsulotlarni olib keldi, mahsulotlar ro'yxatiga 
# yangi mahsulotlar qo'shing.


mahsulotlar = list(mahsulotlar)
for m in dokonda_yoqlar:
    mahsulotlar.append(m)
print(mahsulotlar)









  
  







 



 























