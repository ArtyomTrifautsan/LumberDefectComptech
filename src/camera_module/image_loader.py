import os

import cv2
import numpy as np
import matplotlib.pyplot as plt


class ImageLoader:

	def __init__(self):
		self.byte_imgs = []


	def load_images(self, src):
		files = os.listdir(src)
		for img_file in files:
			
			print(f"file: {src}/{img_file}")
			byte_imgs = self.load_img(f"{src}/{img_file}")
			self.byte_imgs.append(byte_imgs)
		
		return self.byte_imgs


	def load_img(self, src):
		img = cv2.imread(src)[:, :, ::-1]
		byte_img = img.tobytes()

		return byte_img


	def byte_to_img(self, byte_img):
		decoded_arr = np.frombuffer(byte_img, dtype=np.uint8)
		decoded_img = decoded_arr.reshape(468, 1280, 3)

		return decoded_img
