#Cianan Conboy 21.2.18
# Project Euler 5 https://projecteuler.net/problem=5


def isdivisible1to20(number):
     for i in range(1, 21): # Range 1-21 goes from 1-20 ( not include 21)
      if number % i != 0:  # to show if the numbers are not divisible by 1-20
            return  False
     return True

number = 20 # As the number always has to be divisible by 20
while True:
    if isdivisible1to20(number):
        break # to stop loop
    number +=20 # to continue loop until number is found

print(number)
