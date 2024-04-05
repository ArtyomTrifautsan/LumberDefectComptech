import time
import os

from src.camera_module.image_loader import ImageLoader
from src.network_module.network_controller import NetworkController


def process_camera(config):
	network_controller = NetworkController(config)
	image_loader = ImageLoader()

	end = False
	while not end:
		time.sleep(5)

		images = image_loader.load_images(r"C:\Users\1\Documents\VSCode\Python\comptech\rep\LumberDefectComptech\data")

		for img in images:
			network_controller.send_message(img)
			time.sleep(3)
