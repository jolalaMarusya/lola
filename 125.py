a = [0,0]
b = [1,1]
c = [2,4]

k = (c[1] - a[1]) // (c[0] - a[0])

b = c[1] - k * c[0]

b1 = (c[1] - k * c[0]) + 5
b2 = (c[1] - k * c[0]) - 5

print(k)
