import time
import cv2
import numpy as np
import matplotlib.pyplot as plt
<<<<<<< HEAD
=======
import yaml
>>>>>>> 5a409f9 (add nn)
import json

from src.network_module.network_controller import NetworkController
from src.camera_module.image_loader import ImageLoader
from ultralytics import YOLO


def process_nn(config):
	network_controller = NetworkController(config)
	image_loader = ImageLoader()
	
    # Инициализировать нейронную сеть здесь
<<<<<<< HEAD
	#model = YOLO('yolov8n.yaml')
	#model = YOLO("/home/artyomtrifautsan/IT/python/LumberDefectComptech/src/nn_module/best.pt")
=======
	model = YOLO('yolov8n.yaml')
	model = YOLO(r"C:\Users\1\Documents\VSCode\Python\comptech\best.pt")
>>>>>>> 5a409f9 (add nn)


	end = False
	while not end:
		byte_img = network_controller.accept_message()
		numpy_img = image_loader.byte_to_img(byte_img)

		time.sleep(5)

<<<<<<< HEAD
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
=======
		network_controller.send_message(byte_img)
		#print(byte_img)
>>>>>>> 5a409f9 (add nn)

        # Здесь нейронка ожидает приход данных, обрабатывает их и возвращает сюда же
		decoded_arr = cv2.imdecode(np.frombuffer(byte_img, dtype=np.uint8), -1)
		#print(decoded_arr)
		result = model(decoded_arr)[0]


		with open(r"C:\Users\1\Documents\VSCode\Python\comptech\rep\LumberDefectComptech\src\nn_module\defects.yaml") as file_categories:
			info = yaml.load(file_categories, Loader=yaml.FullLoader)
		categories = info["names"]
		file_json = open("example.json",mode="w")
		data_to_json = []



		box = result.boxes
		for i in range(box.xyxy.shape[0]):
			cords = box.xyxy[i].tolist()
			class_id = box.cls[i].tolist()
			name_of_category = categories[class_id]
			data_to_json.append({'deffect_type': name_of_category, 
            		'coordinates': cords})
		json.dump(data_to_json, fp=file_json)

		print(data_to_json)