
import numpy as np
def frange(start,stop,step):
    i=start
    while i<stop:
        yield i
        i=i+step

start,stop,step = [float(i) for i in input().split()]
print('\n')

print(np.arange(start,stop,step))
print(np.arange(start,stop,step))    
print([start + step * x for x in range(0, 1 + int((stop-start)//step)) if start + step * x<= stop])
      
for i in frange(start,stop,step):
    print(i,end = ' ')
    
print('\n')    
while start <= stop:
    print(start,end = ' ')
    start += step
