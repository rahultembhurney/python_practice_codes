'''Here we will use iterative methods to generate a fibonacci sequence
Logic: 1) Assign first 2 numbers manually
       2) Use For loop generate numbers further '''


from tkinter import Y

n = int(input("Enter required number of series: "))
x = 0
y = 1
exp = []
for i in range(0, n):
    if i <= 1:
        result = i
        exp.append(i)
    else:
        result = x + y
        x = y
        y = result
        exp.append(result)
    print(result)  # <------ This will print as individual int
print(exp)  # <------ This will print as a list
