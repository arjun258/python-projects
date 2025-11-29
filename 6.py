def search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i
    return -1

L = eval(input("Enter list: "))
item = eval(input("Enter element to search: "))

pos = search(L, item)
print(pos)
