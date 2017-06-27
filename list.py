import sys

n = int(input("Enter maximum value\n"))

sum = 0
sys.stdout.write("The multiples of 3 and 5 are: \t")
for i in list(range(n)):
    if i % 3 == 0 or i % 5  == 0:
        sys.stdout.write("%d\t" % (i))
        sum = sum + i
print("\nThe sum of multiples of 3 or 5 are: %d" %(sum))