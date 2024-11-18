from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

points=[]
W_Width, W_Height = 500,500
speed = 0.01
create_new = False
freeze=False
blink=0
class point:
    def __init__(self):
        self.x=0
        self.y=0
        self.z=0


def crossProduct(a, b):
    result=point()
    result.x = a.y * b.z - a.z * b.y
    result.y = a.z * b.x - a.x * b.z
    result.z = a.x * b.y - a.y * b.x

    return result

def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a,b

def draw_points(x, y, color):
    glColor3f(color[0],color[1],color[2])
    if blink>0:
        glColor3f(0,0,0)
    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def create_points():
    global points
    for coordinate in points:
        draw_points(coordinate[0],coordinate[1],coordinate[4])


def keyboardListener(key, x, y):
    global freeze
    if key==b" ":
        if freeze==True:
            freeze=False
        else:
            freeze=True
    glutPostRedisplay()

def specialKeyListener(key, x, y):
    global speed
    if freeze==False:
        if key==GLUT_KEY_UP:
            speed *= 2
            print("Speed Increased")
        if key== GLUT_KEY_DOWN:		#// up arrow key
            speed /= 2
            print("Speed Decreased")
        glutPostRedisplay()

def mouseListener(button, state, x, y):	#/#/x, y is the x-y of the screen (2D)
    glutPostRedisplay()
    global points
    if freeze==False:
        if button==GLUT_RIGHT_BUTTON:
            if(state == GLUT_DOWN):    # 		// 2 times?? in ONE click? -- solution is checking DOWN or UP
                c_X, c_y = convert_coordinate(x,y)
                coordinate=[c_X,c_y]
                movement= [1,-1]
                coordinate.append(random.choice(movement))
                coordinate.append(random.choice(movement))
                color=(random.random(),random.random(),random.random())
                coordinate.append(color)            
                points.append(coordinate)

        if button==GLUT_LEFT_BUTTON:
            if state==GLUT_DOWN:
                global blink
                blink=1000


def display():
    global blink
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glClearColor(0,0,0,0);	
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,200,	0,0,0,	0,1,0)
    glMatrixMode(GL_MODELVIEW)
    create_points()
    glutSwapBuffers()


def animate():
    global blink
    if freeze==False:
        glutPostRedisplay()
        global points
        for coordinate in points:
            if coordinate[0] >= 250 or coordinate[0] <= -250:
                coordinate[2] = -coordinate[2]
            if coordinate[1] >= 250 or coordinate[1] <= -250:
                coordinate[3] = -coordinate[3]
            coordinate[0]+=(coordinate[2]*speed)
            coordinate[1]+=(coordinate[3]*speed)
        if blink>0:
            blink-=1
def init():
    #//clear the screen
    glClearColor(0,0,0,0)
    #//load the PROJECTION matrix
    glMatrixMode(GL_PROJECTION)
    #//initialize the matrix
    glLoadIdentity()
    #//give PERSPECTIVE parameters
    gluPerspective(104,	1,	1,	1000.0)
    # **(important)**aspect ratio that determines the field of view in the X direction (horizontally). The bigger this angle is, the more you can see of the world - but at the same time, the objects you can see will become smaller.
    #//near distance
    #//far distance


glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color

# glutCreateWindow("My OpenGL Program")
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()

glutDisplayFunc(display)	#display callback function
glutIdleFunc(animate)#what you want to do in the idle time (when no drawing is occuring)
glutKeyboardFunc(keyboardListener)
glutSpecialFunc(specialKeyListener)
glutMouseFunc(mouseListener)

glutMainLoop()		#The main loop of OpenGL
