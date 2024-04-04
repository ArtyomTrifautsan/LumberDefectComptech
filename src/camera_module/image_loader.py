import os

import cv2
import numpy as np
import matplotlib.pyplot as plt


class ImageLoader:

	def __init__(self):
		self.binary_imgs = []


	def load_images(self, src):
		files = os.listdir(src)
		for img_file in files:
			
			print(f"file: {src}/{img_file}")
			binary_img = self.load_img(f"{src}/{img_file}")
			self.binary_imgs.append(binary_img)
		
		return self.binary_imgs


	def load_img(self, src):
		img = cv2.imread('data/photo_5208655493428531943_y.jpg')[:, :, ::-1]
		byte_img = img.tobytes()

		return byte_img


	def binary_to_img(self, binary_img):
		decoded_arr = np.frombuffer(binary_img, dtype=np.uint8)
		decoded_img = decoded_arr.reshape(468, 1280, 3)

		return decoded_img
