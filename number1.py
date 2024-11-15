from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
raindrops=[] #empty list to store rain coordinates
flag=False #flag to check if raindrops are generated, since redisplay function generate the coordinates again and again
rain_direction = 0 #controls the rain direction, 0 means it is going downwards
mode="morning" #for switching the mode between night and morning
W_Width, W_Height = 500,500 #whole screen size

def convert_coordinate(x,y):
    global W_Width, W_Height
    a = x - (W_Width/2)
    b = (W_Height/2) - y 
    return a,b

def draw_points(x, y, s):
    glPointSize(s)
    glBegin(GL_POINTS)
    glVertex2f(x,y)
    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
    

def drawAxes(): #1(i)
    #green roof using triangles
    glColor3f(0,1,0)
    glBegin(GL_TRIANGLES)
    glVertex2d(-173,0)
    glVertex2d(0,98)
    glVertex2d(173,0)
    glEnd()

    #white roof using triangles
    glColor3f(1,1,1)
    glBegin(GL_TRIANGLES)
    glVertex2d(-150,0)
    glVertex2d(0,85)
    glVertex2d(150,0)
    glEnd()

    #base using lines
    glLineWidth(10)
    glColor3f(0,1,0)
    glBegin(GL_LINES)

    glVertex2d(-155,0) #top side of square
    glVertex2d(155,0) #top side of square

    glVertex2d(-155,0) #left side of square
    glVertex2d(-155,-155) #left side of square
    
    glVertex2d(-160,-160) #bottom side of square
    glVertex2d(160,-160) #bottom side of square

    glVertex2d(155,-155) #right side of square
    glVertex2d(155,0) #right side of square
    glEnd()

    #door using lines
    glLineWidth(2)
    glColor3f(0,1,0)
    glBegin(GL_LINES)

    glVertex2d(-70,-160) #left side of door
    glVertex2d(-70,-70) #left side of door

    glVertex2d(-71,-70) #top side of door
    glVertex2d(-19,-70) #top side of door

    glVertex2d(-20,-70) #right side of door
    glVertex2d(-20,-160) #right side of door
    
    glEnd()

    #door handle using points
    glColor3f(0,1,0)
    draw_points(-30,-115,3)

    #window using lines
    glLineWidth(2)
    glColor3f(0,1,0)
    glBegin(GL_LINES)
    glVertex2d(50,-80) #left side of window
    glVertex2d(50,-30) #left side of window

    glVertex2d(49,-30) #top side of window
    glVertex2d(101,-30) #top side of window

    glVertex2d(100,-30) #right side of window
    glVertex2d(100,-80) #right side of window

    glVertex2d(50,-55) #Horizontal line of window
    glVertex2d(100,-55) #horizontal line of window
    
    glVertex2d(75,-30) #vertical line of window
    glVertex2d(75,-80) #vertical line of window

    glVertex2d(49,-80) #bottom line of window
    glVertex2d(101,-80) #bottom line of window

    glEnd()

def generateRaindrops():
    global raindrops, flag, mode, rain_direction
    glColor3f(0,0,0)
    if mode=="night":
        glColor3f(1,1,1)
    else:
        glColor3f(0,0,0)

    glLineWidth(3)
    glBegin(GL_LINES)
    for i in range(0,150):
        if flag!=True:
            x=random.randint(-250,250)
            y_start=random.randint(-10,500)
            y_end= y_start-random.randint(20,40)
            rain_coordinate=[x,y_start,y_end]
            raindrops.append(rain_coordinate)

        else:
            glVertex2f(raindrops[i][0], raindrops[i][1])
            glVertex2f(raindrops[i][0]+rain_direction, raindrops[i][2])    
    glEnd()

    flag=True



def animate():
    glutPostRedisplay()
    global raindrops, rain_direction,mode
    for rain_coordinate in raindrops:
        if rain_coordinate[1] <= 0:
            rain_coordinate[1] += 500
            rain_coordinate[2] += 500
        else:
            rain_coordinate[1] -= 1
            rain_coordinate[2] -= 1        
        


def keyboardListener(key, x, y): #1(iii)

    global mode
    if key==b'1':
        mode="night"
        print("switched to night mode")
    if key==b'2':
        mode="morning"
        print("switched to morning mode")
    
    glutPostRedisplay()

def specialListener(key,x,y):
    global rain_direction
    if key==GLUT_KEY_LEFT:
        rain_direction -= 1
        print("Rain direction set to left")
    elif key==GLUT_KEY_RIGHT:
        rain_direction += 1
        print("Rain direction set to right")
    glutPostRedisplay()


def mouseListener(button, state, x, y):
    print(x,y)
    # global rain_direction
    # if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
    #         rain_direction = -1
    #         print("Rain direction set to left")
    # elif button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN:
    #         rain_direction = 1
    #         print("Rain direction set to right")
    # glutPostRedisplay()

def display():
    global mode
    if mode=="morning":
        glClearColor(1,1,1,1)
    else:
        glClearColor(0,0,0,1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,200,0,0,0,0,1,0)
    generateRaindrops()
    drawAxes()
    glutSwapBuffers()


def init():
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(104,1,1,1000.0)



glutInit()
glutInitWindowSize(W_Width, W_Height)
glutInitWindowPosition(0, 0)
glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color
wind = glutCreateWindow(b"OpenGL Coding Practice")
init()
glutDisplayFunc(display)	#display callback function
glutKeyboardFunc(keyboardListener)
glutMouseFunc(mouseListener)
glutSpecialFunc(specialListener)
glutIdleFunc(animate)


glutMainLoop()		#The main loop of OpenGL
