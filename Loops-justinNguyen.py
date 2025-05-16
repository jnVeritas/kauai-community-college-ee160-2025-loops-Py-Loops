# AMDG

#
# Developer: Justin Nguyen
# Last Edited: 05/15/2025
# Created: 05/15/2025
# Description: Followed the instructions as given the assignment by using for loops for various tasks. Deadline is tomorrow so I toned down on all the extra stuff from previous assignments.
#

# Variables are defined here.
x = 1
changeAmnt = 1000
curNumber = 12
timesIterated = 0

# This prints numbers from 1 to 10 using a while loop.
while x <= 10:
    print(x)
    x = x + 1

print("")

# This prints integers 1 through 10 using a for loop.
for y in range(1,11):
    print(y)

print("")

# This checks the integers from 1 to 50 for their divisibility by 3, 6, and/or 9.
for z in range (1, 51):
    if z % 3 == 0:
        if z % 6 == 0:
            if z % 9 == 0:
                print(str(z) + " is divisible by 3, 6, and 9.")
            else:
                print(str(z) + " is divisible by 3 and 6.")
        else:
            if z % 9 == 0:
                print(str(z) + " is divisibl by 3 and 9.")
            else:
                print(str(z) + " is divisible only by 3.")

# This checks for the iteration number at which the change achieved by dividing by 2 is less than 0.0001.
while changeAmnt >= 0.0001:
    newNumber = curNumber / 2
    changeAmnt = curNumber - newNumber
    curNumber = newNumber
    timesIterated = timesIterated + 1

# This prints out that iteration number.
print("")
print("It took " + str(timesIterated) + " iterations to reach a change less than 0.0001 when repeatedly dividing 12 by 2.")
