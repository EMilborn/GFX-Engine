from subprocess import Popen, PIPE

from os import remove, execlp, system#, fork

#constants
XRES = 500
YRES = 500
MAX_COLOR = 255
RED = 0
GREEN = 1
BLUE = 2

DEFAULT_COLOR = [0, 0, 0]

def new_screen( width = XRES, height = YRES ):
    screen = []
    zbuffer = []
    for y in range( height ):
        rowS = []
        rowZ = []
        screen.append( rowS )
        zbuffer.append( rowZ )
        for x in range( width ):
            screen[y].append( DEFAULT_COLOR[:] )
            zbuffer[y].append( float("-inf") )
    
    return screen, zbuffer

def plot( screen, zbuffer, color, x, y, z ):
    newy = YRES - 1 - y
    if ( x >= 0 and x < XRES and newy >= 0 and newy < YRES ):
        if z >= zbuffer[newy][x]:
            screen[newy][x] = color[:]
            zbuffer[newy][x] = z

def clear_screen( screen, zbuffer ):
    for y in range( len(screen) ):
        for x in range( len(screen[y]) ):
            screen[y][x] = DEFAULT_COLOR[:]
            zbuffer[y][x] = float("-inf")

def save_ppm( screen, fname ):
    f = open( fname, 'w' )
    ppm = 'P3\n' + str(len(screen[0])) +' '+ str(len(screen)) +' '+ str(MAX_COLOR) +'\n'
    
    for y in range( len(screen) ):
        row = ''
        
        for x in range( len(screen[y]) ):
            pixel = screen[y][x]
            print pixel
            row+= str( pixel[ RED ] ) + ' '
            row+= str( pixel[ GREEN ] ) + ' '
            row+= str( pixel[ BLUE ] ) + ' '
        ppm+= row + '\n'
    f.write( ppm )
    f.close()

def save_extension( screen, fname ):
    ppm_name = fname[:fname.find('.')] + '.ppm'
    save_ppm( screen, ppm_name )
    p = Popen( ['convert', ppm_name, fname ], stdin=PIPE, stdout = PIPE )
    p.communicate()
    remove(ppm_name)

def display( screen ):
    ppm_name = 'pic.ppm'
    save_ppm( screen, ppm_name )
    p = Popen( ['display', ppm_name], stdin=PIPE, stdout = PIPE )
    p.communicate()
    remove(ppm_name)

def make_animation( name ):
    name_arg = 'anim/' + name + '*.ppm'
    name = name + '.gif'
    print 'Saving animation as ' + name
    #f = fork()
    #if f == 0:
        #execlp('convert', 'convert', '-delay', '3', name_arg, name)
    system("convert %s %s" %(name_arg, name,))
