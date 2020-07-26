import datetime

from Models.Window.GLUT_Window import GLUT_Window
from Models.Window.GLFW_Window import GLFW_Window

class Core():

    def __init__(self):
        try:
            self.GLUT_Window=GLUT_Window()
            self.GLFW_Window=GLFW_Window()
        except Exception as Errr:
            raise Errr
        print(datetime.datetime.now(),self.__class__,'Ready',sep=' ')
