L = [8, 24, 27, 48, 2, 16, 9, 7, 84, 91]
amount = 0
for number in L:
    if number % 2 == 0:
        amount += number

print("The sum of the even numbers in the list is :", amount)

