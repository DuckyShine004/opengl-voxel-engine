from OpenGL.GL import *

class ShapeManager:
    def __init__(self):
        self.__vertices = numpy.array()

    @staticmethod
    def set_draw_mode_fill(is_fill):
        if is_fill:
            glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
        else:
            glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
