import glfw
from OpenGL.GL import *

class GLFW_Window():

    def __init__(self,Width=500,Height=500,Window_Name="GLFW_Window",X_Pos=200,Y_Pos=200):
        if not glfw.init():
            raise Exception("Check GLFW")

        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR,3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)

        self.Window = glfw.create_window(Width, Height, Window_Name, None, None)

        if not self.Window:
            glfw.terminate()
            raise Exception("Window Create Failure")

        glfw.set_window_pos(self.Window, X_Pos, Y_Pos)

        glfw.make_context_current(self.Window)

        glViewport(X_Pos, Y_Pos, Width, Height)

        self.Clear_Color()


    def Clear_Color(self,R=0.24,G=0.22,B=0.22,A=1):
        glClearColor(R,G,B,A)

    def Show_Window(self):

        while not glfw.window_should_close(self.Window):

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glfw.swap_buffers(self.Window)

            glfw.poll_events()

        glfw.terminate()


