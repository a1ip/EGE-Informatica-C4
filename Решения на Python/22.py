# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-22. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
На вход программе подается строка (длиной не более 200 символов), в
которой нужно зашифровать все английские слова (словом называется
непрерывная последовательность английских букв, слова друга от друга
отделяются любыми другими символами, длина слова не превышает 20
символов). Строка заканчивается символом #, других символов # в строке
нет. Каждое слово зашифровано с помощью циклического сдвига на длину
этого слова. Например, если длина слова равна K, каждая буква в слове
заменяется на букву, стоящую в английском алфавите на K букв дальше
(алфавит считается циклическим, то есть, за буквой Z стоит буква A).
Строчные буквы при этом остаются строчными, а прописные – прописными.
Символы, не являющиеся английскими буквами, не изменяются.
Требуется написать программу, которая будет выводить на экран текст
зашифрованного сообщения. Например, если исходный текст был таким:
    Day, mice. "Year" is a mistake# 
то результат шифровки должен быть следующий:
    Gdb, qmgi. "Ciev" ku b tpzahrl#
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/22.in")

import string
def encode ( word ):
    K = len(word)
    L = len(string.ascii_uppercase)
    encWord = ""
    for letter in word:
        n = string.ascii_uppercase.find(letter)
        if n >= 0:
            letter = string.ascii_uppercase[(n + K) % L]
        n = string.ascii_lowercase.find(letter)
        if n >= 0:
            letter = string.ascii_lowercase[(n + K) % L]
        encWord = encWord + letter
    return encWord

s = input().split('#')[0]

letters = string.ascii_uppercase + string.ascii_lowercase
i = 0
while i < len(s):
    if s[i] in letters: 
        j = i+1
        while j < len(s) and s[j] in letters: j += 1
        word = encode(s[i:j])
        s = s[0:i] + word + s[j:]
        i = j
    else:
        i += 1
print(s + '#')

sys.stdin = save_stdin