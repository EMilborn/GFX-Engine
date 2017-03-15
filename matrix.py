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

def scale(dX, dY, dZ, tM):
    scale = new_matrix()
    scale[0][0] = dX
    scale[1][1] = dY
    scale[2][2] = dZ
    scale[3][3] = 1
    matrix_mult(scale, tM)

def translate(dX, dY, dZ, tM):
    trans = new_matrix()
    ident(trans)
    trans[3][0] = dX
    trans[3][1] = dY
    trans[3][2] = dZ
    matrix_mult(trans, tM)

def rotation(axis, deg, tM):
    rot = new_matrix()
    ident(rot)
    angle = deg * math.pi / 180
    c = math.cos(angle)
    s = math.sin(angle)
    if axis == "x":
        rot[0][0] = c
        rot[1][1] = c
        rot[0][1] = -s
        rot[1][0] = s
    if axis == "y":
        rot[1][1] = c
        rot[2][2] = c
        rot[1][2] = -s
        rot[2][1] = s
    if axis == "z":
        rot[0][0] = c
        rot[2][2] = c
        rot[2][0] = -s
        rot[0][2] = s
    matrix_mult(rot, tM)

def circle(edges, cx, cy, cz, r):
    #s = 100
    
    #for n in range(s):
     #   x = math.cos(math.pi*2*n/s)
      #  x*=r
       # x+=cx
        #y = math.sin(math.pi*2*n/s)
       # y*=r
        #y+=cx
    pass

def hermite(edges, x0, y0, x1, y1, rx0, ry0, rx1, ry1):
    s = 100
    pass

def bezier(edges, x0, y0, x1, y1, x2, y2, x3, y3):
    s = 100
    pass
