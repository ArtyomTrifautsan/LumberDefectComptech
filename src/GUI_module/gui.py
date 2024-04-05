import time
import json
import cv2
import numpy as np
import matplotlib.pyplot as plt

from src.network_module.network_controller import NetworkController
from src.camera_module.image_loader import ImageLoader

import io


def process_gui(config):
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
