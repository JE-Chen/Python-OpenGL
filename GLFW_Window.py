import glfw
from OpenGL.GL import *
from PIL import Image

class GLFW_Window():

    def Default_Size_Change(self, Window, Width, Height):
        print(Window, 'Width: {} Height: {}'.format(Width, Height))
        glViewport(0,0,Width,Height)

    def Set_Size_Change_Function(self, Function):
        self.Default_Size_Function = Function

    def Default_Close(self, Window):
        print(Window,' Closed')

    def Set_Close_Function(self, Function):
        self.Default_Close_Function=Function

    def Clear_Color(self, R=0.24, G=0.22, B=0.22, A=1):
        glClearColor(R, G, B, A)

    def __init__(self,Width=500,Height=500,Window_Name="GLFW_Window",X_Pos=200,Y_Pos=200,Icon='air_01_blue.png'):

        self.Default_Size_Function=self.Default_Size_Change
        self.Default_Close_Function=self.Default_Close

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

        Image_Icon=Image.open(Icon)
        glfw.set_window_icon(self.Window,1,Image_Icon)

        glfw.set_window_close_callback(self.Window,self.Default_Close_Function)

        glfw.set_framebuffer_size_callback(self.Window,self.Default_Size_Function)

        self.Clear_Color()


    def Show_Window(self):

        while not glfw.window_should_close(self.Window):

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

            glfw.swap_buffers(self.Window)

            glfw.poll_events()

        glfw.terminate()


