import csv
import os
from collections import Counter
result= []
a = ["a", "b", "a", "c", "c", "a", "c"]
result = Counter(a)
Lresult = len(result)

print (result)

for row in result:
    print(row, result[row])