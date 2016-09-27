mat1 = [[1,2],[3,4]]
mat2 = [[5,6],[7,8]]
result = [[1,1],[1,1]]

result [0][0] = (mat1[0][0] * mat2[0][0]) + (mat1[0][1] * mat2[1][0])
result [0][1] = (mat1[0][0] * mat2[0][1]) + (mat1[0][1] * mat2[1][1])
result [1][0] = (mat1[1][0] * mat2[0][0]) + (mat1[1][1] * mat2[1][0])
result [1][1] = (mat1[1][0] * mat2[0][1]) + (mat1[1][1] * mat2[1][1])

print result
