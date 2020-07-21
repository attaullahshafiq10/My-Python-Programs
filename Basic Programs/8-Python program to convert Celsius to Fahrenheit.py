# Formula = T(℉) = T(℃) x 9/5 + 32
# or
# T(℉) = T(℃) x 1.8 + 32




# Code
# Collect input from the user  
celsius = float(input('Enter temperature in Celsius: '))  
  
# calculate temperature in Fahrenheit  
fahrenheit = (celsius * 1.8) + 32  
print('%0.1f  Celsius is equal to %0.1f degree Fahrenheit'%(celsius,fahrenheit))