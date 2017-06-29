#!/usr/bin/env python

frequency = {}
file = open("file.txt","r")
for word in file:
    count = frequency.get(word, 0)
    frequency[word] = count + 1
    frequency_list = frequency.keys()

for word in frequency_list:
   if frequency[word] == 1:
       print(word)
file.close()