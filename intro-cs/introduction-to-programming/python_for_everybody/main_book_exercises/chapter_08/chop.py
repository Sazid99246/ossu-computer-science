def chop(list):
    del list[0]
    del list[-1]
    
def middle(list):
    del list[0]
    del list[-1]
    return list

print(middle([1, 2, 3, 4, 5]))