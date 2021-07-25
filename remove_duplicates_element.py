def Remove(duplicate):
    list = []
    for num in duplicate:
        if num not in list:
            list.append(num)
    return list
duplicate = [2, 4, 10, 20, 5, 2, 20, 4, 50,20,10,50,10]
print(Remove(duplicate))
