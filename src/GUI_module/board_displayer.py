import numpy as np

class BoardDisplayer():
    ''' класс app_kernel'''
    def __init__(self):
        self.current_image = np.zeros((480, 640, 3), dtype=np.uint8)
        self.marked_image = np.zeros((480, 640, 3), dtype=np.uint8)
        self.current_defects_list = ["", [], []]

    def draw_defects(self, defects_list):
        self.marked_image = self.current_image.copy()
        for defect in defects_list:
            a = self.marked_image[defect[1][1], defect[1][0]:defect[2][0]]
            self.marked_image[defect[1][1], defect[1][0]:defect[2][0]] = \
                [[0] * 3] * abs(defect[2][0]-defect[1][0])
            self.marked_image[defect[1][1]:defect[2][1], defect[1][0]] = \
                [[0] * 3] * abs(defect[2][1] - defect[1][1])
            self.marked_image[defect[2][1], defect[1][0]:defect[2][0]] = \
                [[0] * 3] * abs(defect[2][0]-defect[1][0])
            self.marked_image[defect[1][1]:defect[2][1], defect[2][0]] = \
                [[0] * 3] * abs(defect[2][1]-defect[1][1])

    def set_image(self, new_image):
        self.current_image = np.array(new_image)

    def get_current_image(self):
        return self.current_image

    def get_marked_image(self):
        '''
        возвращает изображение с отрисованными метками дефектов 
        '''
        return self.marked_image

    def set_defects_list(self, new_list):
        self.current_defects_list = new_list

    def get_defects_list(self):
        return self.current_defects_list