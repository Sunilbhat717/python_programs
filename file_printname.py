#!/usr/bin/env python

output = set()
file = open("file.txt","r")
for word in file:
    word = word.lower()
    output.add(word)
for uniq in output:
    print(uniq)