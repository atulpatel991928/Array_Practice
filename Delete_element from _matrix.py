'''import numpy as np

a = np.arange(12).reshape(3, 4)
print(a)

a_del = np.delete(a, 1, 0)
print(a_del)'''
import numpy as np
a = np.array([[1, 2, 3, 4],
			[5, 6, 7, 8],
			[9, 10, 11, 12]])
print(a)
column_to_be_added = np.array([90 ,60 ,50])
result1 = np.hstack((a , np.atleast_2d(column_to_be_added).T))
print ("resultant array", str(result1))

row_to_be_added = np.array([30, 40 , 50, 60, 70])
result2 = np.vstack ((result1 , row_to_be_added))
print(str(result2))



#data = np.delete(a, 0, 0)
#print(data)

#data = np.delete(a, 1, 0)
#print(data)

#data = np.delete(a, 2, 0)
#print(data)

#data=np.append(a, 2, 1)
#print(data)
