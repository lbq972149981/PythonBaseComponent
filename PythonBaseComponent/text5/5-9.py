#5-9
def demo(m,n):
    if m>n:
        m,n=n,m
    p=m*n
    while m!=0:
        r=n%m
        n=m
        m=r
    return (int(p/n),n)
print(demo(20,30))