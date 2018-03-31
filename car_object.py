from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pydub import AudioSegment
from pydub.playback import play
from playsound import *

import numpy as np
from math import *
import time
def Init():
    #glOrtho(-10,10,-10,10,-10,10)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(50, 1, 1.3, 80)
    gluLookAt(-10, 50, 0, 0, 0, 0, 1, 0, 0)
    glClearColor(1, 1, 1, 1)
x=0
y=0
z =0
color = 0
co = -1
move = 0
cnt = 0
acc = 0
val = 0
def draw():
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glPopAttrib()
    glPopMatrix()


def car():



    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

##################

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glColor3f(1, 0, 0)
    glScale(1, .25, .5)
    glTranslate(0, 0, 0)
    glutSolidCube(5)
    glPopAttrib()
    glPopMatrix()
    ######################3

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(1.5,1,.548)
    glTranslate(0,5*.25,0)
    glScale(0.5,.25,0.5)
    glutSolidCube(5)
    glPopAttrib()
    glPopMatrix()
##################


    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 1)
    glTranslate(2.25,-2.5*.25,2.5*.5)
    glutWireTorus(.12,.4,12,8)
    glPopAttrib()
    glPopMatrix()
#################


    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glTranslate(2.25,-2.5*.25,-2.5*.65)
    glColor(0, 0, 1)
    glRotate(0,0,0,1)
    glutWireTorus(.12,.4,12,8)
    glPopAttrib()
    glPopMatrix()
##############

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glTranslate(-2.25,-2.5*.25,2.5*.5)
    glColor(0, 0, 1)
    glRotate(0,0,0,1)
    glutWireTorus(.12,.4,12,8)
    glPopAttrib()
    glPopMatrix()
##########33
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glTranslate(2.25,-2.5*.25,-2.5*.55)
    glRotate(0,0,0,1)
    glColor(0, 0, 1)
    glutWireTorus(.12,.4,12,8)
    glPopAttrib()
    glPopMatrix()
#################


    glPopAttrib()
    glPopMatrix()

x=0
def Anime():
    global x
    glMatrixMode(GL_MODELVIEW)
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()


    glTranslate(x,0,0)
    car()
    x+=.01
    if x > 15:
        x = -30


    glFlush()

def keyup(key, xx, yy):
    global move, val
    if key == b"d" or key == b"a":
        move = 0
    if key ==b"w":
        val = -val
    if key == b"s":
        val = 0

def keyboard(key, xx, yy):
    # Allows us to quit by pressing 'q'
    # We can animate by "a" and stop by "s"
    global co, move,val

    if key == b"w":
        # Notice we are making anim = 1
        # What does this mean? Look at the idle function
        val = .02
    if key == b"s":
        # STOP the ball!
        val = -.04
    if key == b"d" or key == b"a":
        if key == b"a":
            move = -1
        else:
            move = 1

    if key == b"q":
        sys.exit()



def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600,600)
    glutCreateWindow(b"hey")
    glutKeyboardFunc(keyboard)
    glutKeyboardUpFunc(keyup)
    Init()
    glutDisplayFunc(Anime)
    glutIdleFunc(Anime)
    glutMainLoop()

main()