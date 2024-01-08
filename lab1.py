from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import pyautogui

# Display callback function
def display():
    glClearColor(1.0, 1.0, 1.0, 1.0)  # Set background color to white
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    render_Scene()
    glFlush()
    glutSwapBuffers()

def render_Scene():
    glColor3f(1.0, 0.0, 0.0)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, -0.5)
    glVertex2f(-0.5, 0.5)
    glVertex2f(0.5, 0.5)
    glVertex2f(0.5, -0.5)
    glEnd()

def reshape(width, height):
    glutReshapeWindow(500, 500)  # Set the window size to 500x500 pixels
    screen_width, screen_height = pyautogui.size()
    glutPositionWindow((screen_width - 500) // 2, (screen_height - 500) // 2)

def window_info():
    window_x = glutGet(GLUT_WINDOW_X)
    window_y = glutGet(GLUT_WINDOW_Y)
    window_width = glutGet(GLUT_WINDOW_WIDTH)
    window_height = glutGet(GLUT_WINDOW_HEIGHT)

    print(f"Window Position: ({window_x}, {window_y})")
    print(f"Window Size: ({window_width}, {window_height})")

# Initialize GLUT
glutInit()
# Initialize the window with double buffering and RGB colors
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
# Set the window size to 500x500 pixels
glutInitWindowSize(500, 500)
# Create the window and give it a title
glutCreateWindow("My First OpenGL Window")
# Set the initial window position to (50, 50)
glutInitWindowPosition(50, 50)
# Define callbacks
glutDisplayFunc(display)
glutReshapeFunc(reshape)
glutIdleFunc(window_info)  # Update window information on idle
# Begin event loop
glutMainLoop()
