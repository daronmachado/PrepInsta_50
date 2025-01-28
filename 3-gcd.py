def gcd(p,q):
    for i in range(p,0,-1):
        if q%i == 0:
            if p%i == 0:
                return i
def main():
    p=72
    q=36
    if p<q:
        print(gcd(p,q))
    else:
        print(gcd(q,p))

if __name__ == '__main__':
    main()