import time
from threading import Thread

import numpy as np
from PyQt6 import QtCore
from PyQt6.QtWidgets import  QWidget
import cv2


from PyQt6.QtGui import QPixmap, QImage
from PyQt6.QtCore import QByteArray

from .interface import Ui_MainWindow


class MainWindowController(QWidget):
    def __init__(self, app_kernel):
        super().__init__()

        self.app_kernel = app_kernel

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # TODO:
        # установить исходное изображение
        
        # old_imge = '1614431160_99-p-prosto-temnii-fon-116.jpg'
        # pixmap = QPixmap(old_imge)
        # self.ui.Image.setPixmap(pixmap)
        # self.ui.Image.setScaledContents(True)
        # установить изначальные табличные данные

        #устанавливаем таймер, по истечении которого интерфейс будет обновляться
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.__update)
        self.timer.start(100)
       

    def __update(self):
        # print("upd")
        # TODO:
        # установить новое изображение, взятое изображение, взятое из класса app_kernel


        # new_img = cv2.imread('44457.jpg')[:, :, ::-1]
        # height, width, channel = new_img.shape
        # bytesPerLine = channel * width

        # new_img_bytes = new_img.data.tobytes()

        # qImg = QImage(QByteArray.fromRawData(new_img_bytes), 
        #               width=width, 
        #               height=height, 
        #               bytesPerLine = channel * width, 
        #               format= QImage.Format.Format_RGB888)
        # qImg = qImg.rgbSwapped()
        # pixmap = QPixmap.fromImage(qImg)
        # self.ui.Image.setPixmap(pixmap)
        # self.ui.Image.setScaledContents(True)

        new_img = cv2.imread('44457.jpg')[:, :, ::-1]
        height, width, channel = new_img.shape
        bytesPerLine = channel * width

        new_img_bytes = new_img.data.tobytes()

        qImg = QImage.fromData(new_img_bytes)
        qImg = qImg.rgbSwapped()
        pixmap = QPixmap.fromImage(qImg)
        self.ui.Image.setPixmap(pixmap)
        self.ui.Image.setScaledContents(True)
        self.ui.Image.show()


        # установить новые табличные данные, взятые оттуда же
        # new_img = self.app_kernel.get_marked_image()
        
        # ТЕСТОВАЯ КАРТИНКА 
       
        # set new img to label



        pass