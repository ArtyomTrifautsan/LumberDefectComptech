from src.network_module.network_controller import NetworkController
import time


def process_nn(config):
	network_controller = NetworkController(config)
	
    # Инициализировать нейронную сетьs

	end = False
	while not end:
		message = network_controller.accept_message()
		print(f"[NN]: gotten message: {message}")

		time.sleep(3)
		
		message = b"Hello from nn process"
		network_controller.send_message(message)
