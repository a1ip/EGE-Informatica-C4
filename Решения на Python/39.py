# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-39. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
Взаимным индексом совпадения строк  S_1 и S_2, которые включают только
латинские буквы, называется величина
             sum[k=1..26] f_1[k]*f_2[k] 
  I(S1,S2) = ------------------------
                      n_1*n_2
где n_1 и n_2 – длины строк S_1 и S_2, а f_i[k] – число вхождений буквы,
имеющей номер k в латинском алфавите, в строку S_i. Например, индекс
совпадений строк «Moloko» и «mAma» равен
                        1*2      1 
  I(«Moloko»,«mAma») = ----- = ----
                        6*4      12
(одна общая буква «m» встречается 1 раз в первой строке и 2 раза во
второй строке). Напишите эффективную программу, которая вводит 
две строки, содержащие (кроме латинских букв) знаки
препинания и пробелы, и вычисляет взаимный индекс совпадения этих строк.
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/39.in")

s1 = input().upper()
s2 = input().upper()

import string
f1 = {}; f2 = {}
for c in string.ascii_uppercase:
    f1[c] = 0
    f2[c] = 0
    
for c in s1:
    if c in string.ascii_uppercase:
        f1[c] += 1
for c in s2:
    if c in string.ascii_uppercase:
        f2[c] += 1

prod = 0
for c in string.ascii_uppercase:
    prod += f1[c]*f2[c]
print("%.3f" % (prod/len(s1)/len(s2)))

sys.stdin = save_stdin