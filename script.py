import mdl
from display import *
from matrix import *
from draw import *

def run(filename):
    """
    This function runs an mdl script
    """
    color = [255, 255, 255]
    tmp = new_matrix()
    ident( tmp )

    p = mdl.parseFile(filename)

    if p:
        (commands, symbols) = p
    else:
        print "Parsing failed."
        return

    ident(tmp)
    transform = [ [x[:] for x in tmp] ]
    screen = new_screen()
    tmp = []
    step = 0.1
    for command in commands:
        line=command[0]
        try:
            args=command[1:]
        except:
            pass
        if line == 'push':
            transform.append(transform[len(transform)-1][:])
            
        if line == 'pop':
            transform = transform[:-1]

        if line == 'circle':
            #print 'CIRCLE\t' + str(args)
            temp = []
            add_circle(temp,
                       float(args[0]), float(args[1]), float(args[2]),
                       float(args[3]), step)
            matrix_mult(transform[-1],temp)
            draw_lines(temp, screen, color)

        elif line == 'hermite' or line == 'bezier':
            #print 'curve\t' + line + ": " + str(args)
            temp = []
            add_curve(edges,
                      float(args[0]), float(args[1]),
                      float(args[2]), float(args[3]),
                      float(args[4]), float(args[5]),
                      float(args[6]), float(args[7]),
                      step, line)
            matrix_mult(transform[-1],temp)
            draw_lines(temp, screen, color) 
            
        elif line == 'line':            
            #print 'LINE\t' + str(args)
            temp=[]
            add_edge( temp,
                      float(args[0]), float(args[1]), float(args[2]),
                      float(args[3]), float(args[4]), float(args[5]) )
            matrix_mult(transform[-1],temp)

        elif line == 'scale':
            #print 'SCALE\t' + str(args)
            t = make_scale(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(transform[-1],t)
            transform[-1]=t

        elif line == 'move':
            #print 'MOVE\t' + str(args)
            t = make_translate(float(args[0]), float(args[1]), float(args[2]))
            matrix_mult(transform[-1],t)
            transform[-1]=t

        elif line == 'rotate':
            #print 'ROTATE\t' + str(args)
            theta = float(args[1]) * (math.pi / 180)
            
            if args[0] == 'x':
                t = make_rotX(theta)
            elif args[0] == 'y':
                t = make_rotY(theta)
            else:
                t = make_rotZ(theta)
            matrix_mult(transform[-1],t)
            transform[-1]=t

        elif line == 'box':
            args1 = [int(i) for i in args if i is not None]
            temp = []
            add_box(temp, args1[0], args1[1], args1[2], args1[3], args1[4], args1[5])
            print len(temp)
            matrix_mult(transform[-1],temp)
            draw_polygons(temp, screen, color)
                
        elif line == 'torus':
            args1 = [int(i) for i in args if i is not None]
           
            temp = []
            add_torus(temp, args1[0], args[1], args[2], args[3], args[4],.1)
            matrix_mult(transform[-1],temp)
            draw_polygons(temp, screen, color)

        elif line == 'sphere':
            print args
            args1 = [int(i) for i in args if i is not None]
            temp = []
            add_sphere(temp, args1[0], args1[1], args1[2], args1[3], .04999999)
            matrix_mult(transform[-1],temp)
            draw_polygons(temp, screen, color)

            
        elif line == 'ident':
            ident(transform)

        elif line == 'apply':
            matrix_mult( transform, edges )

        elif line == 'display' or line == 'save':
            if line == 'display':
                display(screen)
            else:
                save_extension(screen, args[0])

        elif line == 'clear':
            edges = [[]]
            
                
        
run('script.mdl')
