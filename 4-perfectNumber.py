def perfectNumber(n):
    res = []
    for i in range(1,n):
        if n%i==0:
            res.append(i)
    if sum(res) == n:
        print("Perfect Number!")
    
perfectNumber(496)
