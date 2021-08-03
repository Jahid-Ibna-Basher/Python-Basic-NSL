
txt = "To change any funcitonality of a function but not change the code, decorator is used to modify and extend the code"
def print_list(arr):
    print(arr)
    
def list_to_string(function):
    def printx(arr):
        function('.'.join([str(i) for i in arr]))
        
    return printx

PrintList = list_to_string(print_list)

PrintList([i for i in range(10)])
