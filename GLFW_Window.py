import glfw

class GLFW_Window():

    def __init__(self):
        pass

    def Create_Window(self,Width=500,Height=500,Window_Name="GLFW_Window",X_Pos=200,Y_Pos=200):

        if not glfw.init():
            raise Exception("Check GLFW")

        Window = glfw.create_window(Width,Height,Window_Name,None,None)

        if not Window :
            raise Exception("Window Create Failure")

        glfw.set_window_pos(Window,X_Pos,Y_Pos)

        glfw.make_context_current(Window)

        while not glfw.window_should_close(Window):

            glfw.poll_events()

            glfw.swap_buffers(Window)

        glfw.terminate()


