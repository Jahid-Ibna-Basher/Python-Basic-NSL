
f = lambda  x : x*x
x = list(map(f,[i for i in range(9)]))

def is_even(i):return i%2==0 

even = lambda x: x%2==0

print(x,list(filter(is_even,x)),list(filter(even,x)),sep='\n')
