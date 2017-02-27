
import math
import random


def print_matrix( matrix ):
    for y in range(len(matrix[0])):
        s=""
        for x in range(len(matrix)):
            s+=str(matrix[x][y])
            s+="\t"
        print s
    print


def ident( matrix ):
    for n in range(len(matrix)):
        matrix[n][n] = 1

def scalar_mult( matrix, s ):
    for x in range(len(matrix)):
        for y in range(len(matrix[0])):
            matrix[x][y] *= s

#m1 * m2 -> m2
def matrix_mult( m1, m2 ):
    temp = new_matrix(cols = len(m2))
    for c in range(len(m2)):
        for r in range(4):
            for n in range (4):
                temp[c][r] += m2[c][n]*m1[n][r]
    for c in range(len(m2)):
        for r in range(4):
            m2[c][r] = temp[c][r]
    




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m

print("making new 4x4 matrix")
m = new_matrix()
print_matrix(m)

print("\nconverting matrix to identity")
ident(m)
print_matrix(m)

print("\ncreating random 4x4 matrix")
n = new_matrix(cols = 3)
for c in range(3):
    for r in range(4):
        n[c][r] = random.randint(1,10)
for c in range(4):
    for r in range(4):
        m[c][r] = random.randint(1,10)

print_matrix(m)


print("\ncreating random 3x4 matrix")
print_matrix(n)

print("\nmultiplying 4x4 matrix and 3x4 matrix")
matrix_mult(m, n)
print("newly multiplied 3x4:")
print_matrix(n)

print("\nmultiplying random 4x4 matrix by 10")
scalar_mult(m, 10)
print_matrix(m)
