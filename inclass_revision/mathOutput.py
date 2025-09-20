import calc
from myModule.module import valueCal
import math as mt
import datetime as dt

print("-------- method 1 module import --------")
# method 1 module import
print(calc.add(10, 15))
print(calc.sub(25, 10))

print("-------- method 2 module import --------")
# method 2 module import
from calc import add, sub
print(add(100, 250))
print(sub(300, 250))

print("-------- method 3 module import --------")
# method 3 module import
from calc import *
print(add(50, 40))
print(sub(50, 40))

print("-------- calculate value --------")
print(valueCal(2, 3, 1))

print(add(50, 40))

print("-------- square value --------")
print(mt.sqrt(9))

print("-------- current time and date --------")
print(dt.datetime.now())
