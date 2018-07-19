import heapq
import random
data = list(range(10))
random.shuffle(data)
print(data)
heap = []
for n in data:           
    heapq.heappush(heap, n)
print(heap)
heapq.heappush(heap, 0.5)      
print(heap)
print('Pop:', heapq.heappop(heap))    
print('Pop:', heapq.heappop(heap))
print(heap)
print('Pop:', heapq.heappop(heap))
print(heap)
print('\n')
myheap = [1, 2, 3, 5, 7, 8, 9, 4, 10, 333]
heapq.heapify(myheap)        
print(myheap)
heapq.heapreplace(myheap, 6) 
print(myheap)
print(heapq.nlargest(3, myheap))   
print(heapq.nsmallest(3, myheap))    
