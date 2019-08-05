import re

data = "12, 14-15,  18, 23- 2" 
numbers = data.replace(",","")
numbers = numbers.replace("-"," ")
res = numbers.split(" ")

print(numbers)