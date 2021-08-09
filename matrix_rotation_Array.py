'''def rotate(self, matrix):
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(len(matrix)):
        matrix[i].reverse()'''

m = [[1,2],[3,4],[5,6]]
for column in m :
	print(column)
trans = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in trans:
	print(row)
