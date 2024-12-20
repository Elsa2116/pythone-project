def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= 1
        return result
n = int(input("enter a number to calculate :"))
print(f"the factorial of {n} is {factorial(n)}")







def sum_of_even_nums():
    total=0
    for i in range(1,51):
        if i % 2 == 0:
            total += i
            return total
        print(f"the sum of all even nums between 1 and 50 is{sum_of_even_nums}")









