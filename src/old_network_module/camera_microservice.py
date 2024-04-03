import zmq
import time


class CameraProxy:

	def __init__(self, ingress, egress):
		self.ingress = ingress
		self.egress = egress


	def run(self):
		self.context = zmq.Context()

		self.connect_to_router()

		end = False
		while not end:
			msg = b"Hello, I am a camera!"
			self.router_input_socket.send(msg)
			print(f"Sent message: {msg}")
			time.sleep(2)


	def connect_to_router(self):
		self.router_input_socket = self.context.socket(zmq.PUSH)
		self.router_input_socket.connect(self.egress)


	def load_data_from_cameras(self):
		pass


	def pull_data_to_router(self):
		pass
