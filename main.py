from display import *
from draw import *
from matrix import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
    
#(x-249)^2 + (y-249)^2 = 250

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



for n in range(500):
    n2=math.sqrt(250**2-(n-250)**2)+250
    plot(screen, [255,0,0],int(n),int(n2))
    plot(screen, [255,0,0],int(n),499-int(n2))
    plot(screen, [255,0,0],int(n2),int(n))
    plot(screen, [255,0,0],499-int(n2),int(n))
    n+=1

n=0
m = []

while(n<=250):
    add_edge(m,0,249+n,0,n,499,0) 
    #draw_line(0,249+n,n,499,screen, color)
    add_edge(m,249+n,499,0,499,499-n,0)
    #draw_line(249+n,499,499,499-n,screen, color)
    add_edge(m,499,249-n,0,499-n,0,0)
    #draw_line(499,249-n,499-n,0,screen, color)
    add_edge(m,249-n,0,0,0,n,0) 
    #draw_line(249-n,0,0,n,screen, color)
    n+=10

draw_matrix(m, screen, color)
display(screen)
