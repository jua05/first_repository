def is_prime_number(x):
    if x <= 1:
        print("ERROR: The input value should be larger than 1")
    elif x>1 & x<55:
        print("히히힛")
    else:
        for num in range(2, x):
            if x % num == 0:
                print("The number {num1} is not a prime number.".format(num1=x))
                return
    print("The number {num1} is a prime number.".format(num1=x))
