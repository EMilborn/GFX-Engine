from display import *
from matrix import *

COMMANDS = ["line", "ident", "scale", "move", "rotate", "apply", "display", "save"]
ARG_NUMS = [6, 0, 3, 3, 2, 0, 0, 1]

def interpret(script):
    edges = []
    trans = ident(new_matrix())
    commands = script.split(str="\n")
    i = 0
    while i < len(commands):
        dI = intComm(screen, commands[i], commands[i+1].split(str=" "), edges, trans)
        if (not dI):
            raise SyntaxError("issue in line " + str(i+1) + " or " + str(i+2))
        i += dI
        
def intComm(screen, command, inputs, edges, trans):
    if 
    



        
