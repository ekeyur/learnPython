mat1 = [[2,-3,5],[6,3,8]]
mat2 = [[6,8,7],[2,5,3]]

def mat_sum(l1,l2):
    l3 = []
    for i in xrange(0,len(l1)):
        row = []
        for j in xrange(0,len(l1[0])):
            row.append(l1[i][j] + l2[i][j])
        l3.append(row)
    print l3

mat_sum(mat1,mat2)
