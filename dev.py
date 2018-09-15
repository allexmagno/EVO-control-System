import threading
from time import sleep


a = [1,1,2,3,4,4]
b = [2]
print(len(a), len(b))
del a[5]
del b[0]

if len(a) > 0:
    print(a)

if len(b) == 0:
    print(b)

