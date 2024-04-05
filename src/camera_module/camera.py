import time
import os

from src.camera_module.image_loader import ImageLoader
from src.network_module.network_controller import NetworkController


def process_camera(config):
	network_controller = NetworkController(config)
	image_loader = ImageLoader()

	end = False
	while not end:
		dir = os.listdir("data")
		print(dir)
		src = f"data/{dir[0]}"
		img = image_loader.load_img(src)
		network_controller.send_message(img)
		time.sleep(3)
