import re

str = "1007 Lakshman 1008 Karthik 1009-Ramesh -1010 Suresh"
Ramesh =re.findall(r"\d{4}",str)
print(Ramesh)