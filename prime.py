def is_prime():
    number = int(input("Enter an integer: "))
    if number == 1:
       return False
    elif number == 2:
        return True
    else:
        for i in range(2,number):
            if number % i == 0:
                return False
        return True
print(is_prime())
