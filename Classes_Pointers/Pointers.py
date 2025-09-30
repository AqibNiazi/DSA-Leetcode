# num1=11

# num2=num1

# print("Before num2 value is updated")
# print("num1 =",num1)
# print("num2 =",num2)

# print("Num1 points to ",id(num1))
# print("Num2 points to ",id(num2))

# # # So both values points to same memory address

# num2=22

# print("After num2 value is updated")
# print("num1 =",num1)
# print("num2 =",num2)

# print("Num1 points to ",id(num1))
# print("Num2 points to ",id(num2))

# Now both values points to different address because Intergers are immutable

################################### Dictioneries ##############################

dict1={
    "value":11
}

dict2=dict1

print("\n\nBefore value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) 

dict2['value']=22

print("\nAfter value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2)) 

# Again both dict pointing towards same address but values changed in both dictioneries bcz dict are mutable