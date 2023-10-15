x = [312,7656,34,12,98,544,345543,4324,76767,666,545,234354,23]
x_min = min(x)
x_max = max(x)
index_min = x.index(x_min)
index_max = x.index(x_max)
x[index_min], x[index_max] = x[index_max], x[index_min]
print(x)