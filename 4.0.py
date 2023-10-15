x = [312,7656,34,12,98,544,345543,4324,76767,666,545,234354,23]
y = list()
for i in range(len(x)):
    if x[i] > x[i-1]:
        y.append(x[i])
print(y)