import time
import json
import cv2
import numpy as np
import matplotlib.pyplot as plt

import io

from src.network_module.network_controller import NetworkController
from src.camera_module.image_loader import ImageLoader

from controller import MainWindowController
from PyQt6 import QtCore
from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPixmap

from board_displayer import BoardDisplayer
import sys


def _process_gui(config):
	#print("Process has started")
	network_controller = NetworkController(config)
	image_loader = ImageLoader()

	# Здесь запускать GUI

	end = False
	while not end:
		# Здесь GUI ожидает и получает данные от нейросети  
		byte_data = network_controller.accept_message().decode('utf-8').replace('\'', '\"')
		data = json.loads(byte_data)
		# print(f"Бинарный вид полученного изображения: {byte_img}")
		#print(f"data from gui.py: {data}")
		print(type(data))

		numpy_img = np.array(data["numpy_img"], dtype=np.uint8)[:, :, ::-1]
		#img = image_loader.byte_to_img(byte_img)
		#print(f"Декодированный вид полученного изображения: {img}")
  
		cv2.imshow('win', numpy_img)
		cv2.waitKey()


def process_gui(config):
	network_controller = NetworkController(config)

	board_displayer = BoardDisplayer()
	app = QApplication(sys.argv)
	w1 = MainWindowController(app_kernel=board_displayer)  # = QtWidgets.QMainWindow()
	w1.show()  # MainWindow.show()
	app.exec()
