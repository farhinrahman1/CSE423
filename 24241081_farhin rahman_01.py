# from OpenGL.GL import *
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import random

# #task-1 
# raindrops=[] #empty list to store rain coordinates
# flag=False #flag to check if raindrops are generated, since redisplay function generate the coordinates again and again
# rain_direction = 0 #controls the rain direction, 0 means it is going downwards
# mode="morning" #for switching the mode between night and morning
# W_Width, W_Height = 500,500 #whole screen size

# def convert_coordinate(x,y):
#     global W_Width, W_Height
#     a = x - (W_Width/2)
#     b = (W_Height/2) - y 
#     return a,b

# def draw_points(x, y, s): #used for the door knob
#     glPointSize(s)
#     glBegin(GL_POINTS)
#     glVertex2f(x,y)
#     glEnd()

# def iterate(): #used for the viewport of the 2D drawing 
#     glViewport(0, 0, 500, 500)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
#     glMatrixMode (GL_MODELVIEW)
#     glLoadIdentity()
    

# def drawAxes(): #1(i)
#     #green roof using triangles
#     glColor3f(0,1,0)
#     glBegin(GL_TRIANGLES)
#     glVertex2d(-173,0)
#     glVertex2d(0,98)
#     glVertex2d(173,0)
#     glEnd()

#     #white inner roof using triangles
#     glColor3f(1,1,1)
#     glBegin(GL_TRIANGLES)
#     glVertex2d(-150,0)
#     glVertex2d(0,85)
#     glVertex2d(150,0)
#     glEnd()

#     #base using lines
#     glLineWidth(10)
#     glColor3f(0,1,0)
#     glBegin(GL_LINES)

#     glVertex2d(-155,0) #top side of square
#     glVertex2d(155,0) #top side of square

#     glVertex2d(-155,0) #left side of square
#     glVertex2d(-155,-155) #left side of square
    
#     glVertex2d(-160,-160) #bottom side of square
#     glVertex2d(160,-160) #bottom side of square

#     glVertex2d(155,-155) #right side of square
#     glVertex2d(155,0) #right side of square
#     glEnd()

#     #door using lines
#     glLineWidth(2)
#     glColor3f(0,1,0)
#     glBegin(GL_LINES)

#     glVertex2d(-70,-160) #left side of door
#     glVertex2d(-70,-70) #left side of door

#     glVertex2d(-71,-70) #top side of door
#     glVertex2d(-19,-70) #top side of door

#     glVertex2d(-20,-70) #right side of door
#     glVertex2d(-20,-160) #right side of door
    
#     glEnd()

#     #door handle using points
#     glColor3f(0,1,0)
#     draw_points(-30,-115,3)

#     #window using lines
#     glLineWidth(2)
#     glColor3f(0,1,0)
#     glBegin(GL_LINES)
#     glVertex2d(50,-80) #left side of window
#     glVertex2d(50,-30) #left side of window

#     glVertex2d(49,-30) #top side of window
#     glVertex2d(101,-30) #top side of window

#     glVertex2d(100,-30) #right side of window
#     glVertex2d(100,-80) #right side of window

#     glVertex2d(50,-55) #Horizontal line of window
#     glVertex2d(100,-55) #horizontal line of window
    
#     glVertex2d(75,-30) #vertical line of window
#     glVertex2d(75,-80) #vertical line of window

#     glVertex2d(49,-80) #bottom line of window
#     glVertex2d(101,-80) #bottom line of window

#     glEnd()

# def generateRaindrops(): #it draws the raindrops
#     global raindrops, flag, mode, rain_direction #globally declared so that we can use them outside the function
#     glColor3f(0,0,0) #black color for raindrops
#     if mode=="night": #if night mode is on, then white color for raindrops
#         glColor3f(1,1,1)
#     else: #else black color for raindrops
#         glColor3f(0,0,0)

#     glLineWidth(3) #line width of raindrops
#     glBegin(GL_LINES)
#     for i in range(0,150): #generating 150 raindrops
#         if flag!=True: #if raindrops are not generated yet, then generate them
#             x=random.randint(-250,250) #random x coordinate
#             y_start=random.randint(-10,500) #random y coordinate from the top
#             y_end= y_start-random.randint(20,40) #random y coordinate for the bottom of the raindrop by subtracting a random value from y-start to give a length
#             rain_coordinate=[x,y_start,y_end] #storing the coordinates in a list, a list will represent 1 raindrop
#             raindrops.append(rain_coordinate) #appending the 150 raindrops to the list

#         else: #this handles the direction of the raindrop
#             glVertex2f(raindrops[i][0], raindrops[i][1]) #x and y-start coordinate of the raindrop
#             glVertex2f(raindrops[i][0]+rain_direction, raindrops[i][2]) #x and y-end, here x is added with rain_direction to change the direction of the raindrop
#             #for example, if rain_direction is 1, then the raindrop will move to the right, if -1, then to the left. if x is 0, then it will go straight downwards
#     glEnd()

#     flag=True #bar bar same coordinates create korbena 



# def animate(): #updates the position of all the raindrops
#     glutPostRedisplay() #redraws, continous movement of the raindrops
#     global raindrops, rain_direction
#     for rain_coordinate in raindrops: #each rain coordinate is a list of 3 elements, x, y-start, y-end
#         if rain_coordinate[1] <= 0: #if y start is less than or equal to 0, then it means the raindrop has reached the bottom. So, we need to reset the raindrop
#             rain_coordinate[1] += 500
#             rain_coordinate[2] += 500
#         else: #if the y-start is greater than 0 hasn't reached the bottom yet, then we need to move the raindrop downwards
#             rain_coordinate[1] -= 1
#             rain_coordinate[2] -= 1        
        


# def keyboardListener(key, x, y): #1(iii) for switching between night and morning mode

#     global mode
#     if key==b'1':
#         mode="night"
#         print("switched to night mode")
#     if key==b'2':
#         mode="morning"
#         print("switched to morning mode")
    
#     glutPostRedisplay()

# def specialListener(key,x,y):
#     global rain_direction
#     if key==GLUT_KEY_LEFT:
#         rain_direction -= 1
#         print("Rain direction set to left")
#     elif key==GLUT_KEY_RIGHT:
#         rain_direction += 1
#         print("Rain direction set to right")
#     glutPostRedisplay()

# def display():
#     global mode
#     if mode=="morning":
#         glClearColor(1,1,1,1)
#     else:
#         glClearColor(0,0,0,1)
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()
#     gluLookAt(0,0,200,0,0,0,0,1,0)
#     generateRaindrops()
#     drawAxes()
#     glutSwapBuffers()


# def init():
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     gluPerspective(104,1,1,1000.0)



# glutInit()
# glutInitWindowSize(W_Width, W_Height)
# glutInitWindowPosition(0, 0)
# glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGB) #	//Depth, Double buffer, RGB color
# wind = glutCreateWindow(b"OpenGL Coding Practice")
# init()
# glutDisplayFunc(display)	#display callback function
# glutKeyboardFunc(keyboardListener)
# glutSpecialFunc(specialListener)
# glutIdleFunc(animate)


# glutMainLoop()		#The main loop of OpenGL







#task-2
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
