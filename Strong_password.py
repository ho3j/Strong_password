"""
HOSSEIN JALILI
#HO3J
Strong Password
mehr 1400
ver 1.0
"""
import string
from random import *

while True:
    try:
        size=int(input("How long is your password? \t "))
        break
    except:
        print("Enter number !")
while True:
    try:
        print("""
        1 : \t ascii
        2 : \t digits
        3 : \t symbols
        4 : \t ascii & digits
        5 : \t ascii & symbols
        6 : \t digits & symbols
        7 : \t ascii & digits & symbols
        """)
        i=int(input("Enter type of password :\t"))
        break
    except:
        print("Enter number !")

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation

if i ==1:
    chars = letters
elif i==2:
    chars = digits 
elif i==3:
    chars = symbols
elif i==4:
    chars = letters + digits 
elif i==5:
    chars = letters + symbols
elif i==6:
    chars = digits + symbols
elif i==7 :
    chars = letters + digits + symbols 
else :
    print(" wrong !!! ")

password = "".join(choice(chars) for x in range(size))
print("your password :\n" + password)
