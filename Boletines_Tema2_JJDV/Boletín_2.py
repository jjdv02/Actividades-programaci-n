'''
Created on 24 nov 2022

@author: jjdon
'''
'''
print("Ejercicio 1")
n=5
resultado=1
while n>1:
    resultado*=n
    n-=1
print("The factorial of",n,"is",resultado,)


print("Ejercicio 2")

year=int(input("Introduce a year date:"))

def LeapYear(number):
    return number%4==0 or number%100!=0 or number%400==0

print(LeapYear)

print("Ejercicio 3")

print("Ejercicio 4")

print("Ejercicio 5")

print("Ejercicio 6")

print("Ejercicio 7")
'''
def isPrime(numero):
    primenumber=True
    if numero>0:
        for i in range(2, numero):
            if numero%i==0:
                primenumber=False
    else:
        primenumber=None
        
    return f"{numero} is prime? {primenumber}"

print(isPrime(5))
print(isPrime(-3))
print(isPrime(45))

print("Ejercicio 8")

print("Ejercicio 9")

print("Ejercicio 10")






