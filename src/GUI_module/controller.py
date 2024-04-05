import time
from threading import Thread

import numpy as np
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem
import cv2
import json


from PyQt6.QtGui import QPixmap, QImage

from .interface import Ui_MainWindow


class MainWindowController(QWidget):
    def __init__(self, app_kernel):
        super().__init__()

        self.app_kernel = app_kernel

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        new_img = cv2.imread('44457.jpg')
        height, width, channel = new_img.shape
        self.set_data_table()
        self.app_kernel.set_image(new_img)
        self.app_kernel.draw_defects(self.app_kernel.current_defects_list)
        qImg = QImage(self.app_kernel.get_marked_image().data, width, height, width * channel, QImage.Format.Format_BGR888)
        pixmap = QPixmap.fromImage(qImg)
        self.ui.Image.setPixmap(pixmap)
        self.ui.Image.setScaledContents(True)
        print("label displayed")

        # TODO:
        # установить исходное изображение
        # установить изначальные табличные данные

        #устанавливаем таймер, по истечении которого интерфейс будет обновляться
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.__update)
        self.timer.start(100)

    def set_data_table(self):
        self.ui.data.clear()
        list_defects = self.app_kernel.get_defects_list()
        for number_defect in range(len(list_defects)):
            self.ui.data.setItem(number_defect, 0, QTableWidgetItem(list_defects[number_defect][0]))
            self.ui.data.setItem(number_defect, 1, QTableWidgetItem(f'Точка 1: {str(list_defects[number_defect][1])} Точка 2: {str(list_defects[number_defect][2])}'))
        self.ui.data.show()

    def get_new_data(self, list_new_data):
        #new_image = list_new_data[0]
        new_list = list_new_data
        #self.app_kernel.set_image(new_image)
        self.app_kernel.set_defects_list(new_list)

    def __update(self, network_controller):
        # print("upd")
        # TODO:
        # установить новое изображение, взятое изображение, взятое из класса app_kernel

        byte_data = network_controller.accept_message().decode('utf-8').replace('\'', '\"')
        data = json.loads(byte_data)

        numpy_img = np.array(data["numpy_img"], dtype=np.uint8)[:, :, ::-1]
        print(data["defects"])
        data_to_json = {"defect_of_type": [""]}

        data = [["wewewr", [100, 110], [200, 200]], ["23431", [110, 60], [200, 300]], ["323143", [100, 40], [333, 222]]]
        self.get_new_data(data)
        self.set_data_table()
        new_img = numpy_img
        self.app_kernel.set_image(new_img)
        height, width, channel = new_img.shape
        #self.app_kernel.set_image(new_img)
        self.app_kernel.draw_defects(self.app_kernel.get_defects_list())
        qImg = QImage(self.app_kernel.get_marked_image().data, width, height, width * channel,
                      QImage.Format.Format_BGR888)
        pixmap = QPixmap.fromImage(qImg)
        self.ui.Image.setPixmap(pixmap)
        self.ui.Image.setScaledContents(True)

