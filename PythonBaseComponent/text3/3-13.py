digits=(1,2,3,4)
for i in digits:
     for j in digits:
          if j==i:
               continue
          for k in digits:
               if k==i or k==j:
                    continue
               print(i*100+j*10+k)
