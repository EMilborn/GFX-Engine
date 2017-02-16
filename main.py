from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]

n=0
while(n<500):
    draw_line(0,n,n,500,screen, color)
    draw_line(n,500,500,500-n,screen, color)
    draw_line(500,500-n,500-n,0,screen, color)
    draw_line(500-n,0,0,n,screen, color)
    n+=10
    

display(screen)

save_extension(screen, 'img.png')
