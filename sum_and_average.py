'''list = [2, 3, 4]
product = 1

for item in list:
	product = product * item
print(product)


original_list = [10, 22, 44, 23, 4]
new_list = list(original_list)
print(original_list)
print(new_list)'''

#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 6,7,8,9,10]
#print(x[::2])
















def sum(arr):
    sum=0
    arr.sort();
    print(arr)
    print(arr[-1] + arr[-2]);
    for i in arr:
        sum=sum+i;
    print(sum)
    avg= sum / len(arr)
    print(avg)

if __name__ == "__main__":
    arr = [7,17]
    print(arr)

    sum(arr)




