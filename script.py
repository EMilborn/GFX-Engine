import mdl
from display import *
from matrix import *
from draw import *
import os

"""======== first_pass( commands, symbols ) ==========
  Checks the commands array for any animation commands
  (frames, basename, vary)
  
  Should set num_frames and basename if the frames 
  or basename commands are present
  If vary is found, but frames is not, the entire
  program should exit.
  If frames is found, but basename is not, set name
  to some default value, and print out a message
  with the name being used.
  jdyrlandweaver
  ==================== """
def first_pass( commands ):
    frames = 0
    basename = None
    hasVary = False
    for command in commands:
        c = command[0]
        args = command[1:]
        if c == "frames":
            frames = int(args[0])
        if c == "basename":
            basename = args[0]
        if c == "vary":
            hasVary = True

    if frames > 0 and basename == None:
        basename = "Untitled"
        print("basename not foud saving animation as 'Untitled'")
        
    if hasVary:
        if frames <= 0:
            raise Exception("frames not defined")
    return frames, basename, hasVary



def second_pass( commands, num_frames ):
    """======== second_pass( commands ) ==========
  In order to set the knobs for animation, we need to keep
  a seaprate value for each knob for each frame. We can do
  this by using an array of dictionaries. Each array index
  will correspond to a frame (eg. knobs[0] would be the first
  frame, knobs[2] would be the 3rd frame and so on).
  Each index should contain a dictionary of knob values, each
  key will be a knob name, and each value will be the knob's
  value for that frame.
  Go through the command array, and when you find vary, go 
  from knobs[0] to knobs[frames-1] and add (or modify) the
  dictionary corresponding to the given knob with the
  appropirate value. 
  ===================="""
    knobs = [{None:1} for i in range(num_frames)]
    for command in commands:
        c = command[0]
        args = command[1:]
        if c == "vary":
            knob = args[0]
            start_frame = int(args[1])
            end_frame = int(args[2])
            start_val = float(args[3])
            end_val = float(args[4])
            for i in range(len(knobs)):
                value = 0
                if i >= start_frame and i <= end_frame:
                    value = start_val + (((end_val-start_val)*(i-start_frame))/(end_frame-start_frame))
                if not(knob in knobs[i]):
                    knobs[i][knob] = value
    return knobs
                


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

    frames, basename, hasVary = first_pass(commands)
    if (not hasVary) or frames == 0:
    
        ident(tmp)
        stack = [ [x[:] for x in tmp] ]
        screen = new_screen()
        tmp = []
        step = 0.1
        for command in commands:
            print command
            c = command[0]
            args = command[1:]
    
            if c == 'box':
                add_box(tmp,
                        args[0], args[1], args[2],
                        args[3], args[4], args[5])
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, color)
                tmp = []
            elif c == 'sphere':
                add_sphere(tmp,
                        args[0], args[1], args[2], args[3], step)
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, color)
                tmp = []
            elif c == 'torus':
                add_torus(tmp,
                        args[0], args[1], args[2], args[3], args[4], step)
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, color)
                tmp = []
            elif c == 'move':
                tmp = make_translate(args[0], args[1], args[2])
                matrix_mult(stack[-1], tmp)
                stack[-1] = [x[:] for x in tmp]
                tmp = []
            elif c == 'scale':
                tmp = make_scale(args[0], args[1], args[2])
                matrix_mult(stack[-1], tmp)
                stack[-1] = [x[:] for x in tmp]
                tmp = []
            elif c == 'rotate':
                theta = args[1] * (math.pi/180)
                if args[0] == 'x':
                    tmp = make_rotX(theta)
                elif args[0] == 'y':
                    tmp = make_rotY(theta)
                else:
                    tmp = make_rotZ(theta)
                matrix_mult( stack[-1], tmp )
                stack[-1] = [ x[:] for x in tmp]
                tmp = []
            elif c == 'push':
                stack.append([x[:] for x in stack[-1]] )
            elif c == 'pop':
                stack.pop()
            elif c == 'display':
                display(screen)
            elif c == 'save':
                save_extension(screen, args[0])
        return
    knobs = second_pass(commands, frames)
    for i in range(len(knobs)):
        frame = knobs[i]
        tmp = new_matrix()
        ident(tmp)
        stack = [ [x[:] for x in tmp] ]
        screen = new_screen()
        tmp = []
        step = 0.1
        for command in commands:
            c = command[0]
            args = command[1:]
        
            if c == 'box':
                add_box(tmp,
                args[0], args[1], args[2],
                        args[3], args[4], args[5])
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, color)
                tmp = []
            elif c == 'sphere':
                add_sphere(tmp,
                        args[0], args[1], args[2], args[3], step)
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, color)
                tmp = []
            elif c == 'torus':
                add_torus(tmp,
                        args[0], args[1], args[2], args[3], args[4], step)
                matrix_mult( stack[-1], tmp )
                draw_polygons(tmp, screen, color)
                tmp = []
            elif c == 'move':
                knob = args[3]
                val = frame[knob]
                tmp = make_translate(val*args[0], val*args[1], val*args[2])
                matrix_mult(stack[-1], tmp)
                stack[-1] = [x[:] for x in tmp]
                tmp = []
            elif c == 'scale':
                knob = args[3]
                val = frame[knob]
                tmp = make_scale(val*args[0], val*args[1], val*args[2])
                matrix_mult(stack[-1], tmp)
                stack[-1] = [x[:] for x in tmp]
                tmp = []
            elif c == 'rotate':
                knob = args[2]
                val = frame[knob]
                theta = val * args[1] * (math.pi/180)
                if args[0] == 'x':
                    tmp = make_rotX(theta)
                elif args[0] == 'y':
                    tmp = make_rotY(theta)
                else:
                    tmp = make_rotZ(theta)
                matrix_mult( stack[-1], tmp )
                stack[-1] = [ x[:] for x in tmp]
                tmp = []
            elif c == 'push':
                stack.append([x[:] for x in stack[-1]] )
            elif c == 'pop':
                stack.pop()
        save_extension(screen, "anim/%s%03d.png" % (basename,i))
    os.system('convert anim/%s*.png %s.gif' % (basename,basename))
        
        
        
        
    
    
