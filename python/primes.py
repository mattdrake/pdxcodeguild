__author__ = 'drake'

# lists out all prime numbers between 2 and integer given by user

# asks user for input for integer
question = input("Please enter a number. ")

# creates new list with no elements to add prime numbers to later
results = []
# creates a range of numbers up to and including integer
for i in range(2, question):
# creates another range for each integer from range above to be checked if divisible by 2 evenly
    for l in range(2, i):
        if i % l == 0:
# if the number is not prime it will be skipped
            break
# if the number is prime it will be added to the empty list created above
    else:
        results.append(i)

print(results)

