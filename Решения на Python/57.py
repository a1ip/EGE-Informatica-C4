# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-57. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
57)	По каналу связи передаются положительные целые числа, не превышающие
1000, – результаты измерений, полученных в ходе эксперимента (количество 
измерений известно заранее). После окончания эксперимента передаётся
контрольное значение – наибольшее число R, удовлетворяющее следующим условиям:
1) R – сумма двух различных переданных элементов последовательности 
(«различные» означает, что нельзя просто удваивать переданные числа, суммы 
различных, но равных по величине элементов допускаются);
2) R – нечётное число.
Если чисел, соответствующих приведённым условиям, нет, считается, что R = –1.
В результате помех при передаче как сами числа, так и контрольное значение
могут быть искажены.
Напишите эффективную, в том числе по используемой памяти, программу (укажите 
используемую версию языка программирования, например, Free Pascal 2.6.4),
которая будет проверять правильность контрольного значения.
Программа должна напечатать отчёт по следующей форме:
Вычисленное контрольное значение:…
Контроль пройден (или – контроль не пройден)
Если удовлетворяющее условию контрольное значение определить невозможно 
(то есть при R = –1), то выводится только фраза «Контроль не пройден».
Перед текстом программы кратко опишите используемый Вами алгоритм решения.
На вход программе в первой строке подаётся количество чисел N. В каждой из 
последующих N строк записано одно натуральное число, не превышающее 1000. В 
последней строке записано контрольное значение.
Пример входных данных:
  6
  100 
  8
  33
  45
  19
  90
  145
Пример выходных данных для приведенного выше примера входных данных:
  Вычисленное контрольное значение: 145
  Контроль пройден.
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/57.in")

chet = 0; nechet = 0; R = -1
N = int(input())
for i in range(N):
    x = int(input())
    if x % 2 == 0 and x > chet: chet = x
    if x % 2 != 0 and x > nechet: nechet = x
if chet > 0 and nechet > 0:
    R = chet + nechet
R0 = int(input())

if R > 0: 
  print('Вычисленное контрольное значение: ', R)
if R > 0 and R == R0:
    print('Контроль пройден.')
else:
    print('Контроль не пройден.');

sys.stdin = save_stdin