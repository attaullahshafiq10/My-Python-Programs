# Python Program to check if a Number is Positive, Negative or Zero
# Positive Numbers: A number is known as a positive number if it has a greater value than zero. i.e. 1, 2, 3, 4 etc.
# Negative Numbers: A number is known as a negative number if it has a lesser value than zero. i.e. -1, -2, -3, -4 etc




# Code
num = float(input("Enter a number: "))  
  
if num > 0:  
 print("{0} is a positive number".format(num))  
elif num == 0:  
   print("{0} is zero".format(num))   
else:  
   print("{0} is negative number".format(num)) 