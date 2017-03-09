from display import *
from matrix import *

def draw_line( x0, y0, x1, y1, screen, color ):
    x0 = int(x0)
    y0 = int(y0)
    x1 = int(x1)
    y1 = int(y1)

    if (x0 > x1):
        draw_line(x1, y1, x0, y0, screen, color)
        return
        
    x=x0
    y=y0
    A = y1-y0
    B = -(x1-x0)
    


    if (A > 0):#octant I or II
        if(A < -B):#octant I
            d = 2*A + B #(A + 2*B)()()()()(A-2*B)(2*A+B) 
            while x < x1:#(y < y1)()()()()(y > y1)(x<x1)
                plot(screen, color, x, y)

                if d > 0:#(d < 0)()()()()(d>0)(d < 0) 
                    y+=1#(x += 1)()()()()(x+=1)(y-=1)
                    d += 2*B#(d += 2*A)()()()()(d+=2*A)(d-=2*B) 

                x+=1#(y += 1)()()()()(y-=1)(x+=1)
                d+=2*A#(d += 2B)()()()()(d-=2B)(d+=2A)
                
        else:#octant II
            d = A + 2*B #(A + 2*B)()()()()(A-2*B)(2*A+B) 
            while y < y1:
                
                plot(screen, color, x, y)

                if d < 0: 
                    x+=1
                    d += 2*A 

                y+=1
                d+=2*B

    else:
        if(-A > -B):#octant VII
            d = A - 2*B #(A + 2*B)()()()()(A-2*B)(2*A+B) 
            while y > y1:#(y < y1)()()()()(y > y1)(x<x1)
                plot(screen, color, x, y)

                if d > 0:#(d < 0)()()()()(d>0)(d < 0) 
                    x+=1#(x += 1)()()()()(x+=1)(y-=1)
                    d += 2*A#(d += 2*A)()()()()(d+=2*A)(d-=2*B) 

                y-=1#(y += 1)()()()()(y-=1)(x+=1)
                d-=2*B#(d += 2B)()()()()(d-=2B)(d+=2A)

        else:#octant VIII
            d = 2*A + B #(A + 2*B)()()()()(A-2*B)(2*A+B) 
            while x < x1:#(y < y1)()()()()(y > y1)(x<x1)
                plot(screen, color, x, y)

                if d < 0:#(d < 0)()()()()(d>0)(d < 0) 
                    y-=1#(x += 1)()()()()(x+=1)(y-=1)
                    d -= 2*B#(d += 2*A)()()()()(d+=2*A)(d-=2*B) 

                x+=1#(y += 1)()()()()(y-=1)(x+=1)
                d+=2*A#(d += 2B)()()()()(d-=2B)(d+=2A)


            
    plot(screen, color, x1, y1)

def add_point(m, x, y, z):
    m.append([x, y, z, 1])

def add_edge(m, x1, y1, z1, x2, y2, z2):
    add_point(m, x1, y1, z1)
    add_point(m, x2, y2, z2)

def draw_matrix(m, screen, color):
    for i in range(len(m)/2):
        x1 = m[2*i][0]
        y1 = m[2*i][1]
        x2 = m[2*i+1][0]
        y2 = m[2*i+1][1]
        draw_line(x1,y1,x2,y2,screen, color)

