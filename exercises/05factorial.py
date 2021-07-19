# Write a function to compute the `factorial` of a number.
# Given a whole number n, a factorial is the product of all
# whole numbers from 1 to n.
# 5! = 5 * 4 * 3 * 2 * 1
#
# Example function call
#
# factorial(5)
#
# > 120
#

def factorial(n):
  if n is None or type(n) is not int or n < 0:
   print('invalid value for n')
   return -1
   
  total = 1

  for i in range(1, n+1):
    total *= i

  print(total)

factorial(5)

