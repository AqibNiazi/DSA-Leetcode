#  O(2n)
# we simplify our big(O) by dropping constant.
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)
print_items(10)
    