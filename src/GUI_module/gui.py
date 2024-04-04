import time
import cv2
import numpy as np
import matplotlib.pyplot as plt

from src.network_module.network_controller import NetworkController
from src.camera_module.image_loader import ImageLoader


def process_gui(config):
	#print("Process has started")
	network_controller = NetworkController(config)
	image_loader = ImageLoader()

	# Здесь запускать GUI

	end = False
	while not end:

		# Здесь GUI ожидает и получает данные от нейросети  
  

		byte_img = network_controller.accept_message()
		# print(f"Бинарный вид полученного изображения: {byte_img}")

		img = image_loader.binary_to_img(byte_img)
		#print(f"Декодированный вид полученного изображения: {img}")

		cv2.imshow('win', img)
		cv2.waitKey()
