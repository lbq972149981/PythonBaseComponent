#5-4
def demo(lis,k):
   x=lis[:k]
   x.reverse()
   y=lis[k:]
   y.reverse()
   r=x+y
   r.reverse()
   print(x)
   print(y)
   print(r)
lit=(list(range(1,21)))
print(lit)
demo(lit,9)