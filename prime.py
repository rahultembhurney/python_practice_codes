# a prime number is divisible by only  1 and itself
# 1 is not a primary number
'''
logic used: 
1) check if its divisible with one(obvious)
2) check if its divisible by any other number except itself
'''


def prime(a):
    if a == 1:
        return f"1 is neither composit nor prime"
    if a % 1 == 0:
        for n in range(2, a):
            if a % n == 0:
                return f"Not a prime"
        else:
            return f"prime"


print(prime(3))
