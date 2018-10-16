import math

P = int(input("Principle: "))

r = int(input("Interest rate: "))/100

t = int(input("Years: "))

result = P * ((math.e)**(r * t))

print(result)