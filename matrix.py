
import math


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
    pass




def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m


m = new_matrix()
print_matrix(m)
ident(m)
print_matrix(m)
scalar_mult(m, 10)
print_matrix(m)

