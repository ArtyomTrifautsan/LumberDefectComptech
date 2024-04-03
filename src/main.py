from multiprocessing import Process
import json, time


from network_module.network_controller import NetworkController
from camera_module.image_loader import ImageLoader

from camera_module.camera import process_camera
from nn_module.nn_runner import process_nn
from GUI_module.gui import process_gui


def main():
	config_data = load_config("data.json")
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
        #print(config_data)
    return config_data


if __name__ == '__main__':
    main()
