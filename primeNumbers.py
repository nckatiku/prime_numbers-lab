import math

def primeNumbers(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: 
            return False;
    return n>1;

print (2)
for n in range(3, 50):
    if primeNumbers(n):
        print(n)