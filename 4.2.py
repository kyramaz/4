x = [42, 39, 73, 56, 88, 5, 36, 62, 12, 27]
y = [7, 94, 3, 45, 62, 18, 51, 39, 10, 77]
count = 0

for i in range(len(x)):
    for j in range (len(y)):
        if x[i] == y[j]:
            count += 1

print(count)
