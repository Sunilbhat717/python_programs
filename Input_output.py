#!/usr/bin/env python

print("Please enter the following details")
name = input("Enter your name\n")
age = int(input("Enter your age\n"))

while age > 100 or age < 0:
    print("Invalid input..please re-enter the age")
    age = int(input("Enter your age\n"))

ans = 100 - age
print("Hey %s, Good day. You will turn 100 in next %d year" % (name, ans))
