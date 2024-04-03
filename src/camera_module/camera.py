from src.network_module.network_controller import NetworkController
import time


def process_camera(config):
	network_controller = NetworkController(config)

	end = False
	while not end:
		time.sleep(3)
		message = b"Hello from camera process"
		network_controller.send_message(message)
