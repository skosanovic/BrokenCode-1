#!/usr/bin/python3

c1 = int(input('How old are you? '))
#The first "c1" of the next line was a "c2" variable which doesn't exist, I changed it back to c1
if c1 > int(0) and c1  < int(18):
    print('You are a child.')
elif c1 > int(17):
    print('You are an adult.')
#In the next line there was no colon after the "int(0)". I added the colon and the code worked great!
elif c1 == int(0):
    print('You cannot be 0 years old.')
