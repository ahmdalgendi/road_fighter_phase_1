from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pygame


def init():
    glClearColor(0.7, 0.7, 0, 1)
    glMatrixMode(GL_MODELVIEW)

    texture = glGenTextures(4)  # Generate 4 textures

    imgload = pygame.image.load("wall.jpg")
    # imgload = pygame.image.load("sky.bmp")
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()

    # "Bind" the newly created texture : all future texture functions will modify this texture
    glBindTexture(GL_TEXTURE_2D, texture[0])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexImage2D(GL_TEXTURE_2D, 0, 4, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img)

    #######################################################################################################

    imgload = pygame.image.load("grass.bmp")
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[1])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR_MIPMAP_LINEAR)  # GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

    glTexImage2D(GL_TEXTURE_2D, 1, 4, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img)
#    glGenerateMipmap(GL_TEXTURE_2D)
    # gluBuild2DMipmaps(GL_TEXTURE_2D, 3, width, height, GL_RGB,GL_UNSIGNED_BYTE, img)

    #######################################################################################################

    imgload = pygame.image.load("wood.jpg")
    img = pygame.image.tostring(imgload, "RGBA", 1)  # try 0)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[2])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)  # GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)  # GL_CLAMP)
    glTexImage2D(GL_TEXTURE_2D, 0, 4, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img)

    #######################################################################################################

    imgload = pygame.image.load("chess.png")
    img = pygame.image.tostring(imgload, "RGBA", 1)
    width = imgload.get_width()
    height = imgload.get_height()
    glBindTexture(GL_TEXTURE_2D, texture[3])
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)  # GL_CLAMP)
    glTexParameter(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)  # GL_CLAMP)
    glTexImage2D(GL_TEXTURE_2D, 0, 4, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img)

    glEnable(GL_TEXTURE_2D)

    glBindTexture(GL_TEXTURE_2D, texture[0])  # try texture[1] & texture[2] & texture[3]


def draw():
    glClear(GL_COLOR_BUFFER_BIT)

    glColor(1, 1, 1)

    glBegin(GL_QUADS)

    glTexCoord(0, 0)
    glVertex(-0.75, -0.75, 0)

    glTexCoord(1, 0)
    glVertex(0.75, -0.75, 0)

    glTexCoord(1, 1)  # 1,1
    glVertex(0.75, 0.75, 0)

    glTexCoord(0, 1)
    glVertex(-0.75, 0.75, 0)

    glEnd()

    glFlush()


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(1000, 1000)
    glutCreateWindow(b"Texture")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()


main()
