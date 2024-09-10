# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 15:46:25 2024

@author: Saidus_work
"""

# Foydalanuvchidan ikita son kiritishni so'rang, 
 # sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring.
 
son1 = float(input('Birinchi sonni kiriting: '))
son2 = float(input('Ikkinchi sonni kiriting: '))
if son1 == son2:
    print(f'Siz kiritgan sonlar - {int(son1)} va {int(son2)} teng.')
elif son1 > son2:
    print(f'Siz kiritgan sonlar - {int(son1)} katta {int(son2)} dan.')
elif son1 < son2:
    print(f'Siz kiritgan sonlar - {int(son1)} kichik {int(son2)} dan.')























