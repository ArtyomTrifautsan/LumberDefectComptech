import numpy as np

class BoardDisplayer():
    ''' класс app_kernel'''
    def __init__(self):
        self.current_image = np.zeros((480, 640, 3), dtype=np.uint8)
        self.marked_image = np.zeros((480, 640, 3), dtype=np.uint8)
        self.current_deffects_list = []
        pass

    def draw_deffects(self, deffects_list):
        '''
        отрисовывает на изображении дефекты
        '''
        marked_image = self.current_image.copy()
        # TODO: implement deffects drawing
        pass

    def set_image(self, new_image):
        self.current_image = new_image
        pass

    def get_marked_image(self):
        '''
        возвращает изображение с отрисованными метками дефектов 
        '''
        return self.marked_image

    def get_deffects_list(self):
        return self.current_deffects_list