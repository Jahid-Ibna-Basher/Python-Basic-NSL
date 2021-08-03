'''
This broadly means, that functions in Python:
---have types
---can be sent as arguments to another function
---can be used in expression
---can become part of various data structures like dictionaries
'''

def apply(L, f):
    result = []
    for i in range(len(L)):
        result.append(f(L[i]))
 
    return result

def square(a):
    return a*a

def run():
    print(apply([1,-1,3],abs))
    print(apply([1,-1,3],square))
