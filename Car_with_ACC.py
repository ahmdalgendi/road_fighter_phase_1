from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound

import numpy as np
from math import *
import time
def Init():
    #glOrtho(-10,10,-10,10,-10,10)
    glMatrixMode(GL_PROJECTION)
    gluPerspective(50,1,1.3,80)
    gluLookAt(-10,50,0,0,0,0,1,0,0)
    glClearColor(1,1,1,1)
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


def Anime():
    global x,y,co,color, z, move, cnt, acc, val
    if z >18 or z< -18:
        playsound("/home/ahmdalgendi/PycharmProjects/road_fight_phase 1/car.wav")
        z=0
        x=0
        move =0
        acc=0
        val=0

    time.sleep(0.0166666667)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)


    for i in range(-100,80, 10):
        glLoadIdentity()
        glColor(0, 0, 0)
        glScale(.5, 0.001, .2)
        glTranslate(i, 0, 0)
        glutSolidCube(4)
        #glFlush()
    glPopAttrib()
    glPopMatrix()


    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)


    glLoadIdentity()
    glTranslate(x,5*.25,0+z)
    glScale(0.5,.25,0.5)
    glutSolidCube(5)

##################
    glColor3f(0,0,0)

    glLoadIdentity()
    glTranslate(x+2.25,-2.5*.25,2.5*.5+z)
    glRotate(y,0,0,1)
    glutWireTorus(.12,.4,12,8)

    glLoadIdentity()
    glTranslate(x+2.25,-2.5*.25,-2.5*.65+z)
    glRotate(y,0,0,1)

    glutWireTorus(.12,.4,12,8)

    glLoadIdentity()
    glTranslate(x-2.25,-2.5*.25,2.5*.5+z)
    glRotate(y,0,0,1)
    glutWireTorus(.12,.4,12,8)

    glLoadIdentity()
    glTranslate(x-2.25,-2.5*.25,-2.5*.55+z)
    glRotate(y,0,0,1)

    glutWireTorus(.12,.4,12,8)

#################

    glColor3f(0,color+.5,1)
    glLoadIdentity()
    glTranslate(x+2.25,-2.5*.25,0.1+z)
    glutSolidSphere(.25,10,40)

    glLoadIdentity()
    glTranslate(x+2.25,-2.5*.25,-1+z)
    glutSolidSphere(.25,10,40)


    if(x > 25 ):
        x=-25
    if x <-28:
        x = 24

    x-=acc * co
    y+= .4*co
    z+= .39 * move

    acc+=val
    if acc >.8:
        acc=.8
    if val<0:
        if acc < 0:
            acc =0
    print(acc)

    glPopAttrib()
    glPopMatrix()
    glColor(0,0,1)
    glScale(100, .001 , 10)
    glutWireCube(4)

    glFlush()

def keyup(key, xx, yy):
    global move
    if key == b"d" or key == b"a":
        move = 0
    if key ==b"w":
        val = 0
    if key == b"s":
        val = 0

def keyboard(key, xx, yy):
    # Allows us to quit by pressing 'q'
    # We can animate by "a" and stop by "s"
    global co, move,val

    if key == b"w":
        # Notice we are making anim = 1
        # What does this mean? Look at the idle function
        val = .05
    if key == b"s":
        # STOP the ball!
        val = -.02
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