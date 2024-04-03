import zmq


class Router:

	def __init__(
			self, 
			egress_camera,
			egress_neural_network,
			ingress_neural_network,
			ingress_composition,
			egress_composition,
			ingress_gui
		):
		self.egress_camera = egress_camera
		self.egress_neural_network = egress_neural_network
		self.ingress_neural_network = ingress_neural_network
		self.ingress_composition = ingress_composition
		self.egress_composition = egress_composition
		self.ingress_gui = ingress_gui


	def run(self):
		self.context = zmq.Context()

		self.connect_to_camera_proxy()

		end = False
		while not end:
			msg_from_camera_proxy = self.camera_output_socket.recv()

			print(f"Gotten message from camera: {msg_from_camera_proxy}")


	def connect_to_camera_proxy(self):
		self.camera_output_socket = self.context.socket(zmq.PULL)
		self.camera_output_socket.bind(self.egress_camera)


	def connect_to_neural_network_proxy(self):
		pass


	def connect_to_composition_proxy(self):
		pass


	def connect_to_gui(self):
		pass


	def get_data_from_cameras(self):
		pass


	def pull_data_to_neural_network(self):
		pass


	def pull_data_to_composition(self):
		pass
