import sys

n = int(input("Enter maximum value\n"))
sys.stdout.write("The multiples of 3 and 5 are: \t")
list = ([i for i in range(0,n)if i %3 == 0 or i % 5 == 0]) #1st method
print sum(list)
#sum([i for i in range(0,n)if i % 3 == 0 or i % 5 == 0]) #2nd method
print("\nThe sum of multiples of 3 or 5 are: %d" %(sum))