from src.network_module.network_controller import NetworkController
import time


def process_gui(config):
	#print("Process has started")
	network_controller = NetworkController(config)

	end = False
	while not end:
		#print("Cycle has started")
		message = network_controller.accept_message()
		print(f"[GUI]: gotten message: {message}")
