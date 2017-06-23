'''#!/usr/bin/env python
import sys

a = [1,5,6,9,4,5,6,2,8,1,5,45,16,85,2]

sys.stdout.write("Array List are:\t")
print(a)
print()
i = 0
sys.stdout.write("List less than 5 are: \t")
while i < 15:
    if a[i] < 5:
        sys.stdout.write("%d\t" % (a[i]))
        #print("%d\t" % (a[i]))
    i = i + 1
for i in a:
    if i < 5:
        sys.stdout.write("%d\t" % (i))'''
#!/usr/bin/env python

a = [1,5,6,9,4,5,6,2,8,1,5,45,16,85,2]
list_lt_5 = []

for i in a:
    if i < 5:
        list_lt_5.append(i)
print(list_lt_5)