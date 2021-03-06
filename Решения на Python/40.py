﻿# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-40. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
Вам необходимо написать программу распознавания чисел, записанных
прописью. Сначала на вход программе подается обучающий блок, состоящий 
из 27 строк. Первые 9 строк содержат слова «один», «два», ..., «девять»,
следующие 9 строк - слова «одиннадцать», «двенадцать», ...
«девятнадцать», следующие 9 строк - слова «десять», «двадцать», ...,
«девяносто». Все слова записаны маленькими русскими буквами без лишних 
пробелов в начале и в конце строки.
Затем на вход программе подается значение N - количество записей,
которые необходимо обработать. Следующие N строк содержат записанные
словами числа. Каждое число записано по-русски, маленькими буквами, без
ошибок. Если число состоит из нескольких слов, между словами находится 
ровно один пробел, лишних пробелов в начале и в конце строк нет.
Напишите эффективную программу, которая определит сумму тех входных
чисел, которые находятся в интервале от 1 до 99.
Размер памяти, которую использует Ваша программа, не должен зависеть от 
длины исходного списка.
Перед текстом программы кратко опишите используемый вами алгоритм 
решения задачи.
Пример входных данных (обучающий блок показан в примере с сокращениями):
    один
    два
    …
    девяносто 
   5
   двадцать восемь
   два миллиона
   четырнадцать
   сто двадцать три
   тысяча девятьсот восемьдесят четыре 
Пример выходных данных для приведённого выше примера входных данных:
   42
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/40.in")

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10, 20, 30, 40, 50, 60, 70, 80, 90]
numVal = {}
for i in range(27):
    numVal[input()] = nums[i]
N = int(input())    
S = 0
for i in range(N):
    cur = input().split()
    val = 0
    for w in cur:        
        if not w in numVal.keys():
            val = 0
            break
        else:
            val = val + numVal[w]
    S += val             

print(S)

sys.stdin = save_stdin