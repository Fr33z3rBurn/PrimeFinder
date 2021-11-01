# taking input from user
number = 2**43112609-1

# prime number is always greater than 1
while True:
    for i in range(2, number):
        print("Checking", i)
        if (number % i) == 0:
            break
    else:
        print(number, "is a prime number")
    number += 1

# if the entered number is less than or equal to 1
# then it is not prime number
else:
    print(number, "is not a prime number")
