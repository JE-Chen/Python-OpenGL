import glfw

class GLFW_Window():

    def __init__(self,Width=500,Height=500,Window_Name="GLFW_Window",X_Pos=200,Y_Pos=200):
        if not glfw.init():
            raise Exception("Check GLFW")

        self.Window = glfw.create_window(Width, Height, Window_Name, None, None)

        if not self.Window:
            glfw.terminate()
            raise Exception("Window Create Failure")

        glfw.set_window_pos(self.Window, X_Pos, Y_Pos)

        glfw.make_context_current(self.Window)

    def Show_Window(self):

        while not glfw.window_should_close(self.Window):

            glfw.poll_events()

            glfw.swap_buffers(self.Window)

        glfw.terminate()


