mas = ['AAA', 'BDC', 'DKD', 'QKQ', 'PYQ', 'MMO', 'AAA', 'MMO', 'QQQ', 'DDWE']
counts = {}

for i in mas:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1

for count in counts.values():
    print(count, end=' ')