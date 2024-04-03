from matplotlib import image
from matplotlib import pyplot as plt
import os


class ImageLoader:

	def __init__(self):
		self.imgs = []


	def load_images(self, src):
		files = os.listdir(src)
		for img_file in files:
			print(f"{src}/{img_file}")
			#img = image.imread(f"{src}/{img_file}")


	def load_img(self, src):
		with open(src, "rb") as file:
			image_bytes = file.read()
			return image_bytess