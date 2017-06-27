import sys

n = int(input("Enter maximum value\n"))

ans = 0
sys.stdout.write("The multiples of 3 and 5 are: \t")
for i in range(1,n,1):
    a = i
    j = i
    j = j % 3
    i = i % 5
    if i == 0 or j == 0:
        sys.stdout.write("%d\t" % (a))
        ans = ans + a
print("\nThe sum of multiples of 3 or 5 are: %d" %(ans))