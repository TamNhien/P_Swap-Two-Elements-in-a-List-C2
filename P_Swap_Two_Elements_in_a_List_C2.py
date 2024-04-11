def swapPositions(lst, pos1, pos2):
    first = lst.pop(pos1)
    second = lst.pop(pos2-1)
    
    lst.insert(pos1, second)
    lst.insert(pos2, first)
    
    return lst

lst = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(lst, pos1-1, pos2-1))
