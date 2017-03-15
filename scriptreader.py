from display import *
from matrix import *
from draw import *


def interpret(fileN):
    script = open(fileN, "r").read()
    edges = []
    trans = new_matrix()
    ident(trans)
    commands = script.split("\n")
    i = 0
    screen = new_screen()
    while i < len(commands):
        if commands[i] == "":
            i+=1
        else:
            dI = 0
            try:
                dI = intComm(screen, commands[i], commands[i+1].split(" "), edges, trans)
            except IndexError:
                dI = intComm(screen, commands[i], [], edges, trans)
            if not dI:
                raise SyntaxError("issue in line " + str(i+1) + " or its input line")
            i += dI
        
def intComm(screen, command, a, edges, trans):
    print command
     print a
    try:
        if command == "line":
            for n in range(len(a)):
                a[n] = float(a[n])
            add_edge(edges,
                     a[0],
                     a[1],
                     a[2],
                     a[3],
                     a[4],
                     a[5])
            return 2
        
        if command == "ident":
            
            ident(trans)
            return 1
        
        if command == "scale":
            for n in range(len(a)):
                a[n] = float(a[n])
            scale(a[0],a[1],a[2],trans)
            return 2
        
        if command == "move":
            
            translate(float(a[0]),
                      float(a[1]),
                      float(a[2]),
                      trans)
            return 2
        
        if command == "rotate":
            rotation(a[0],
                     float(a[1]),
                     trans)
            return 2
        
        if command == "apply":
            matrix_mult(trans, edges)
            return 1
        
        if command == "display":
            draw_matrix(edges, screen,  [255, 255, 255])
            display(screen)
            return 1
        
        if command == "save":
            draw_matrix(edges, screen,  [255, 255, 255])
            save_ppm(screen, a[0])
            return 2

        if command == "circle":
            for n in range(len(a)):
                a[n] = float(a[n])
                
            circle(edges, a[0], a[1], a[2], a[3])
            return 2

        if command == "hermite":
            for n in range(len(a)):
                a[n] = float(a[n])
            hermite(edges, a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7])
            return 2

         if command == "bezier":
            for n in range(len(a)):
                a[n] = float(a[n])
            bezier(edges, a[0], a[1], a[2], a[3], a[4], a[5], a[6], a[7])
            return 2
        
        return 0

    except:
        return 0
        
        
                         
                         
        
            
        
        
        
        
        
    



        
