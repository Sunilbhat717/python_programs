import sys

n = int(input("Enter maximum value\n"))

ans = 0
sys.stdout.write("The multiples of 3 and 5 are: \t")
i = 1
while i <= n:
    a = i
    j = i
    j = j % 3
    i = i % 5
    if i == 0 or j == 0:
        sys.stdout.write("%d\t" % (a))
        ans = ans + a
    i = a + 1
print("\nThe sum of multiples of 3 or 5 are: %d" %(ans))
