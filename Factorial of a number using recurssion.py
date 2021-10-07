def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)

num = 7

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")

else:
   print(f"The factorial of {num} is {recur_factorial(num)}")
