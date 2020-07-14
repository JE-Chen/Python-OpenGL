from Window import Window

class Core():

    def __init__(self):
        try:
            self.Window=Window()
        except Exception as Errr:
            raise Errr
