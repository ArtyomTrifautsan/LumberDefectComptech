import time
import cv2
import numpy as np
import matplotlib.pyplot as plt
import json

from src.network_module.network_controller import NetworkController
from src.camera_module.image_loader import ImageLoader
from ultralytics import YOLO


def process_nn(config):
	network_controller = NetworkController(config)
	image_loader = ImageLoader()
	
    # Инициализировать нейронную сеть здесь
	#model = YOLO('yolov8n.yaml')
	#model = YOLO("/home/artyomtrifautsan/IT/python/LumberDefectComptech/src/nn_module/best.pt")


	end = False
	while not end:
		byte_img = network_controller.accept_message()
		numpy_img = image_loader.byte_to_img(byte_img)

		time.sleep(5)

		test_data = {
			"numpy_img": numpy_img.tolist(),
			"defects": [
				["type1", [70, 70], [120, 120]],
				["type2", [180, 170], [190, 250]],
				["type3", [250, 270], [300, 300]],
			]
		}
		byte_data = str.encode(json.dumps(test_data))

		network_controller.send_message(byte_data)

        # Здесь нейронка ожидает приход данных, обрабатывает их и возвращает сюда же
