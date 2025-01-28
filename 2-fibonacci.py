def fibonacci(n):
    a=0
    b=1
    for _ in range(n-2):
        res = a + b
        a = b
        b = res
    print(res)

fibonacci(7)
