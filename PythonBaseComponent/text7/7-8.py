#coding:utf8
'''
Created on 2017年10月24日

@author: Administrator
'''
import pickle
f= open('sample_pickle.dat','wb')
#n=7
i=13000000
a=99.056
s='中国人民 123abc'
lst = [[1,2,3],[4,5,6],[7,8,9]]
tu=(-5,10,8)
coll={4,5,6}
dic = {'a':'apple','b':'banana','g':'grape','o':'orange'}
try:
    pickle.dump(n,f)
    pickle.dump(i,f)
    pickle.dump(a,f)
    pickle.dump(s,f)
    pickle.dump(lst,f)
    pickle.dump(tu,f)
    pickle.dump(coll,f)
    pickle.dump(dic,f)
except:
    print('写完件异常')
finally:
    f.close()

