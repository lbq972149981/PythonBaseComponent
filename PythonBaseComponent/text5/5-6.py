#5-6
import random
def demo(lst):
    m=min(lst)
    result = (m,)
    for index ,value in enumerate(lst):
        if value==m:
            result = result+(index,)
    return result
x=[random.randint(1,20) for i in range(10)]
print(x)
print(demo(x))
