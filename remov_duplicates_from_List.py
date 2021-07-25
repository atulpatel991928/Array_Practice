data =[10,20,30,40,50,30,50,60,50,50,90]
def remove_duplicates(duplicate):
    noduplist =[]
    for element in duplicate:
        if element not in noduplist:
            noduplist.append(element)
    return noduplist
print(remove_duplicates(data))

