def fibonacci(n):
    a=0
    b=1
    print(a,b,end=" ")
    for _ in range(n-2):
        res = a + b
        a = b
        b = res
        print(res,end=" ")
    

fibonacci(7)
