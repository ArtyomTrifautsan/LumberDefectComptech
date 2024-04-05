import time
import cv2
import numpy as np
import matplotlib.pyplot as plt
import yaml
import json

from src.network_module.network_controller import NetworkController
from src.camera_module.image_loader import ImageLoader
from ultralytics import YOLO


def process_nn(config):
	network_controller = NetworkController(config)
	image_loader = ImageLoader()
	
    # Инициализировать нейронную сеть здесь
	model = YOLO('yolov8n.yaml')
	model = YOLO(r"C:\Users\1\Documents\VSCode\Python\comptech\best.pt")


	end = False
	while not end:
		byte_img = network_controller.accept_message()
		numpy_img = image_loader.byte_to_img(byte_img)


		#print(byte_img)

        # Здесь нейронка ожидает приход данных, обрабатывает их и возвращает сюда же
		decoded_arr = cv2.imdecode(np.frombuffer(byte_img, dtype=np.uint8), -1)
		#print(decoded_arr)
		result = model(decoded_arr)[0]


		with open(r"C:\Users\1\Documents\VSCode\Python\comptech\rep\LumberDefectComptech\src\nn_module\defects.yaml") as file_categories:
			info = yaml.load(file_categories, Loader=yaml.FullLoader)
		categories = info["names"]
		# file_json = open("example.json",mode="w")
		data_to_json = {}
		data_to_json["deffects"] = []



		box = result.boxes
		for i in range(box.xyxy.shape[0]):
			cords = box.xyxy[i].tolist()
			class_id = box.cls[i].tolist()
			name_of_category = categories[class_id]
			data_to_json["deffects"].append({"deffect_type": name_of_category, 
            		'coordinates': cords})
		#json.dump(data_to_json, fp=file_json)
  

		data_to_json["numpy_img"] = numpy_img.tolist()
		str_data = str(data_to_json)
		byte_data = str_data.encode('utf-8')  # str.encode(json.dumps(data_to_json),)
		network_controller.send_message(byte_data)

		print(data_to_json['deffects'])