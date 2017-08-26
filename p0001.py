def multiples():
    counterthree = 0
    counterfive = 0
    total = 0


    for n in range(1000):
        if n %3 == 0:
            counterthree += n

        elif n %5 == 0:
            counterfive +=n

    total += counterfive 
    total += counterthree
    return total


print multiples()

def p0001fast(a,b,n):
    len_a = (n-1)/a
    len_b = (n-1)/b
    len_ab = (n-1)/(a*b)

    sum_a = a * len_a * (len_a + 1)/2
    sum_b = b * len_b * (len_b + 1)/2  
    sum_ab = a * b * len_ab * (len_ab + 1)/2   

    total = sum_a + sum_b - sum_ab   
    return total

print p0001fast(3,5,1000)