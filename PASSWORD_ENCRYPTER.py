#!/usr/bin/python3
"""
Many user-created passwords are simple and easy to guess. 
This is a program that takes a simple password and makes it stronger 
by replacing characters using special keys (key legend below), 
and by appending "q*s" to the end of the input string.

i > !
a > @
m > M
B > 8
o > .
"""

password = input()
for i in password:
    if 'm' in password:
        password = password.replace('m', 'M')
    if 'i' in password:
        password = password.replace('i', '!')
    if 'a' in password:
        password = password.replace('a', '@')
    if 'B' in password:
        password = password.replace('B', '8')
    if 'o' in password:
        password = password.replace('o', '.')
password = f'{password}q*s'
print(password)

