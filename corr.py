h = [1,2,3,4,5]
#h = h[::-1]
x = [1,2,3,4,5]
y = []
n = len(h)
i = 0

j = 1
sum1 = 0

while j < n:
    i = 0
    k = j
    while i < n - j:
        sum1 = sum1 + x[i]*h[k]
        i = i + 1
        k = k + 1
    y.append(sum1)
    j = j + 1
    sum1 = 0     
j = 1
sum1 = 0
y = y[::-1]

for i in range(0,n):
    sum1 = sum1 + h[i]*x[i]
y.append(sum1)

#rev = []
sum1 = 0

while j < n:
    i = 0
    k = j
    while i < n - j:
        sum1 = sum1 + h[i]*x[k]
        i = i + 1
        k = k + 1
    y.append(sum1)
    j = j + 1
    sum1 = 0     
#y = y + rev

print "X: " + str(x)
print "h : " + str(h)
print "y : " + str(y)

