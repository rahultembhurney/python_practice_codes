

a = []
counts = int(input("Enter the length of list: "))

for b in range(counts):
    count = int(input("Enter a number: "))
    a.append(count)


(print(a))

greatest = 0
max_index = 0


for i in range(len(a)):
    max_index = i
    for j in range(i+1, len(a)):
        if a[max_index] > a[j]:
            max_index = j
    a[max_index], a[j] = a[j], a[max_index]
    print(a)


print(a[-1])
