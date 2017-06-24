#!/usr/bin/env python
import sys

n = int(input("Enter maximum value\n"))
i = 1
ans = 0
sys.stdout.write("The multiples of 3 and 5 are: \t")
while i <= n:
    a = i
    i = i % 15
    if i == 0:
        sys.stdout.write("%d\t" % (a))
        ans = ans + a;
    i = a + 1
print("\nThe sum of multiples of 3 and 5 are: %d" %(ans))