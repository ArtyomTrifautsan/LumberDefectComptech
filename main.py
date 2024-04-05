from multiprocessing import Process
import json, time


from src.network_module.network_controller import NetworkController
from src.camera_module.image_loader import ImageLoader

from src.camera_module.camera import process_camera
from src.nn_module.nn_runner import process_nn
from src.GUI_module.gui import process_gui


def main():
	config_data = load_config(r"C:\Users\1\Documents\VSCode\Python\comptech\rep\LumberDefectComptech\config\config.json")
	child_processes = []

	for gui in config_data["guis"]:
		gui_process = Process(target=process_gui, args=(gui,))
		child_processes.append(gui_process)

	for neural_network in config_data["neural_networks"]:
		neural_network_process = Process(target=process_nn, args=(neural_network,))
		child_processes.append(neural_network_process)

	for camera in config_data["cameras"]:
		camera_process = Process(target=process_camera, args=(camera,))
		child_processes.append(camera_process)
		
	for i in child_processes:
		i.start()
		print(f"proccess with pid {i.pid} started")
		time.sleep(1)

	for i in child_processes:
		i.join()


def load_config(config_file_name):
    config_data = []
    with open(config_file_name) as file:
        config_data = json.load(file)
    return config_data


if __name__ == '__main__':
    main()
