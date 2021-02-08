# Problem Statement

# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is
# entered, print out the largest and smallest of the numbers. If the user enters anything other than a valid number
# catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10,
# and 4 and match the output below.

smallest = None
largest = None
total = 0
count = 0
averg = 0

while True:
    try:
        n = input("Enter a number: ")

        if n == "done":
            break
        # elif not type(int(n)) is int:
        #     raise Exception
        n = int(n)

        if smallest is None:
            smallest = n

        if largest is None:
            largest = n

        if n < smallest:
            smallest = n

        if n > largest:
            largest = n

        total += n
        count += 1

        # if
    except:
        print("Invalid input")
        continue

print("Maximum is ", largest)
print("Minimum is", smallest)
# print("sum is", total)
# print("Average is ", total/count)