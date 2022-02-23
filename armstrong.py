def armstrong(number):
    temp = number
    total = 0
    while number != 0:
        total += (number % 10)**3
        number = number//10
    if total == temp:
        return f"{temp} is an armstrong number"
    else:
        return f"{temp} isnt an armstrong number"


print(armstrong(371))
