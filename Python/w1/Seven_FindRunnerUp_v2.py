
n=int(input())
a=list(set([int(i) for i in input().split()]))
mx = a[0]
ru = a[0]

for i in a:
    if i>mx:
        ru = mx
        mx = i
if len(a)>1:
    print(a[:-2])    
    print(ru)
else:
    print('No RunnerUp')
