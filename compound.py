def ci(p,r,n):
    if(n==0):
        return 0
    else:
        si=(p*r)/100
        return si+ci(p+si,r,n-1)
p=int(input("principle"))
r=float(input("rate"))
n=int(input("years"))
print("Interest is:"ci(p,r,n))
