import time
import cv2
import numpy as np
import matplotlib.pyplot as plt

from src.network_module.network_controller import NetworkController
from src.camera_module.image_loader import ImageLoader
from ultralytics import YOLO


def process_nn(config):
	network_controller = NetworkController(config)
	image_loader = ImageLoader()
	
    # Инициализировать нейронную сеть здесь
	model = YOLO('yolov8n.yaml')
	model = YOLO("/home/artyomtrifautsan/IT/python/LumberDefectComptech/src/nn_module/best.pt")


	end = False
	while not end:
		byte_img = network_controller.accept_message()
		img = image_loader.binary_to_img(byte_img)

		time.sleep(5)

		network_controller.send_message(byte_img)

        # Здесь нейронка ожидает приход данных, обрабатывает их и возвращает сюда же
