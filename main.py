from display import *
from draw import *
import math

screen = new_screen()
color = [ 0, 255, 0 ]
    
#(x-249)^2 + (y-249)^2 = 250

n=0

while(n<=499):
    n2=math.sqrt(250**2-(n-249)**2)+249
    plot(screen, [255,0,0],int(n),int(n2))
    plot(screen, [255,0,0],int(n),-int(n2))
    plot(screen, [255,0,0],int(n2),int(n))
    plot(screen, [255,0,0],-int(n2),int(n))
    n+=.1

n=0
while(n<=250):
    draw_line(0,249+n,n,499,screen, color)
    draw_line(249+n,499,499,499-n,screen, color)
    draw_line(499,249-n,499-n,0,screen, color)
    draw_line(249-n,0,0,n,screen, color)
    n+=10
    
display(screen)
save_extension(screen, 'pic2.png')
