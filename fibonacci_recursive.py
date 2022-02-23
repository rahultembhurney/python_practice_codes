'''in fibonacci sequence you'll need to add 1st and 2nd number manually'''
n = int(input("Enter the number of series: "))


def recursive_fibo(num):
    if num == 0:
        return num

    elif num == 1:
        return num

    else:
        return recursive_fibo(num-2) + recursive_fibo(num-1)


for i in range(0, n):
    print(recursive_fibo(i))
