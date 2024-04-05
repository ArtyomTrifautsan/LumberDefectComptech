import time
from threading import Thread

import numpy as np
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget, QTableWidgetItem
import cv2
import json


from PyQt6.QtGui import QPixmap, QImage

from src.GUI_module.interface import Ui_MainWindow


class MainWindowController(QWidget):
    def __init__(self, app_kernel, network_controller):
        super().__init__()

        self.app_kernel = app_kernel
        self.network_controller = network_controller

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #new_img = cv2.imread('44457.jpg')
        # height, width, channel = new_img.shape
        # self.set_data_table()
        # self.app_kernel.set_image(new_img)
        # self.app_kernel.draw_defects(self.app_kernel.current_defects_list)
        # qImg = QImage(self.app_kernel.get_marked_image().data, width, height, width * channel, QImage.Format.Format_BGR888)
        # pixmap = QPixmap.fromImage(qImg)
        # self.ui.Image.setPixmap(pixmap)
        # self.ui.Image.setScaledContents(True)
        # print("label displayed")

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

    def get_new_data(self, deffects):
        new_list = []
        for deffect in deffects:
            deffect_type = deffect['deffect_type']
            t1 = [deffect['coordinates'][0], deffect['coordinates'][1]]
            t2 = [deffect['coordinates'][2], deffect['coordinates'][3]]
            new_list.append([deffect_type, t1, t2])
            #print(t1, t2)
        #new_image = list_new_data[0]
        #self.app_kernel.set_image(new_image)
        self.app_kernel.set_defects_list(new_list)

    def __update(self):
        # print("upd")
        # TODO:
        # установить новое изображение, взятое изображение, взятое из класса app_kernel

        byte_data = self.network_controller.accept_message().decode('utf-8').replace('\'', '\"')
        jdata = json.loads(byte_data)

        numpy_img = np.array(jdata["numpy_img"], dtype=np.uint8)[:, :, ::-1]
        #print("===Start data===")
        #print(jdata["deffects"])
        self.get_new_data(jdata['deffects'])
        #print(self.app_kernel.get_defects_list())
        #print("===Start data===")
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

