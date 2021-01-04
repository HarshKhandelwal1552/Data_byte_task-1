for i in range(1, 101):
    if i % 5 == 0 and i % 3 == 0: # checking the divisibility with 15
        print("FizzBuzz")
    elif i % 3 == 0: # checking the divisibility with 3
        print("Fizz")
    elif i % 5 == 0: # checking the divisibility with 5
        print("Buzz")
    else:
        print(i)
