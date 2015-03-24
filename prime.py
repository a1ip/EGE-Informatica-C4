__author__ = 'iag'

import math

n = int(input())

def isPrime(n):
    if n == 2:
        return True
    j = int(math.sqrt(float(n))) + 1
    for i in range(2,j):
        if not n % i:
            return False
    return True

if isPrime(n):
    print("True")
else:
    print("False")