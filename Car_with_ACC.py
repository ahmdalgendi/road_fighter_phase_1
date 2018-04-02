from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pydub import AudioSegment
from pydub.playback import play
import threading as thrd

from playsound import *

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

def print_something():
    playsound("/home/ahmdalgendi/PycharmProjects/road_fight_phase 1/car.wav")

def car_sound():
    while True:
        playsound("/home/ahmdalgendi/PycharmProjects/road_fight_phase 1/formula+1.wav")


carsound = thrd.Thread(target=car_sound, args=[])
carsound.start()

def Anime():
    global x,y,co,color, z, move, cnt, acc, val,a
    if z >18 or z< -18:
        a = thrd.Thread(target=print_something, args=[])
        
        a.start()

        z=0
        x=0
        move =0
        acc=0
        val=0
        for i in range(10):
            glClearColor(1,1,1,1)
            glClear(GL_COLOR_BUFFER_BIT)
            glutSwapBuffers()
            time.sleep(0.1)

    time.sleep(0.01)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    for i in range(min(int(ceil(x-50)),int(ceil (x+100))),max(int(ceil(x-100)),int(ceil (x+70))), 10):
        glLoadIdentity()
        glColor(0, 0, 0)
        glScale(.5, 0.001, .2)
        glTranslate(i, 0, 0)
        glutSolidCube(4)
        #glutSwapBuffers()
    glPopAttrib()
    glPopMatrix()


    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)

    glTranslate(-15, 0, z)
    car()
    if x <-15:
        x = 15

    x+=acc * co
    y+= .4*co
    z+= .5 * move

    acc+=val
    if acc >1:
        acc=1
    if val<0:
        if acc < 0:
            acc =0

    glPopAttrib()
    glPopMatrix()

    glColor(0,0,1)
    glScale(100, .001 , 10)
    glutWireCube(4)
    glutSwapBuffers()

def keyup(key, xx, yy):
    global move, val
    if key == b"d" or key == b"a":
        move = 0
    if key ==b"w":
        val = -val * .4
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
   # glutTimerFunc(.0166666667, Anime)
    glutIdleFunc(Anime)
    glutMainLoop()

main()