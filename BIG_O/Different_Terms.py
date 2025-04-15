def print_numbers(a,b):
    for i in range(a):
        print(i)
    for j in range(b):
        print(j)
        
print_numbers(4,4) 

# bio O for this function is O(a+b)
# because we have two different input terms a and b.    

def nested_loop(a,b):
    for i in range(a):
     for j in range(b):
        print(i,j)
        
nested_loop(4,5)
# bio O for this function is O(a*b)
# because we have two different input terms a and b.
# and they are nested in a loop.
# so we multiply them.
# and we have two different input terms a and b.