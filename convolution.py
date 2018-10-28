h = [2,1,1,2]
h = h[::-1] #folding h
x = [0,1,2,3]
y = []
n = len(h)
i = 0
while i < n:
    k = i
    j = n -1
    sum1 = 0
    while k >= 0:
        sum1 = sum1 + h[j]*x[k]
        k = k - 1
        j = j - 1
    i = i + 1
    y.append(sum1)


max1 = len(h) - 1
while max1 > 0:
    j = len(x) - 1
    sum1 = 0
    i = max1 - 1
    while i >= 0 :
        sum1 = sum1 + h[i]*x[j]
        j = j - 1
        i = i - 1
    y.append(sum1)
    max1 = max1 - 1

print " X: " + str(x)
print "h : " + str(h)
print "y : " + str(y)