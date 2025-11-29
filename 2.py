def modify_list(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst[i] = lst[i] // 2
        else:
            lst[i] = lst[i] * 2
    return lst

nums = eval(input("Enter integer list: "))
print(modify_list(nums))
