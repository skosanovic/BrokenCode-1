#!/usr/bin/python3

c1 = int(input('How old are you? '))

if c1 > int(0) and c1  < int(18):
    print('You are a child.')
elif c1 > int(17):
    print('You are an adult.')
elif c1 == int(0):
    print('You cannot be 0 years old.')
