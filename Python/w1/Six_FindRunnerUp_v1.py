
n=int(input())
a=[int(i) for i in input().split()]
mx = a[0]
ru = a[0]
for i in a:
    if i>mx:
        ru = mx
        mx = i
        
print(ru)
