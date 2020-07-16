from GlutWindow import GlutWindow
from GLFW_Window import GLFW_Window
class Core():

    def __init__(self):
        try:
            self.GlutWindow=GlutWindow()
            self.GLFW_Window=GLFW_Window()
        except Exception as Errr:
            raise Errr
