
'''args_sum(10,20,30,40) returns sum of k args
print_kwargs(a=1,b=2,c=3) prints kwargs dict
print_arg_args_kwargs(10,20,30,40,b=10,c=50) prints general arg,args, kwargs'''


def args_sum(*args):
    sum=0
    for i in args:
        sum+=i
    return sum


def print_kwargs(**kwargs):   # ** is used to pass dict parameter
    print(kwargs)

def print_arg_args_kwargs(a,*args,**kwargs):  #mixed paramter passing function
    print(a);print(args);print(kwargs)
    
#print_dict(a=1,b=2,c=3)
#print(make_sum(10,20,30,40))
#print_all(10,20,30,40,b=10,c=50)
