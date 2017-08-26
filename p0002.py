
def fibo():
    n = 0
    sum =  0
    total=[1,2]
    while total[n+1] < 4000000:
        total.append(total[n] + total[n+1])
    for n in total:
        if n %2 == 0:
            sum += n
    return sum 

#print fibo()

def p0002fast(n):
    a, b = 0, 1
    while True:
        if a > n:
            return

        yield a
        a, b = b, a+b

fb = p0002fast(4000000)
total = 0
for x in fb:
    if (x%2 == 0):
        total += x

print total
    

