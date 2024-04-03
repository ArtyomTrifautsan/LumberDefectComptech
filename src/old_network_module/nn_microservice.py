class NeuralNetworkProxy:

	def __init__(self, ingress, egress):
		self.ingress = ingress
		self.egress = egress


	def run(self):
		self.context = zmq.Context()


	def connect_to_router(self):
		pass


	def get_data_from_router(self):
		pass


	def handle_data_by_neural_network(self):
		pass


	def pull_data_to_router(self):
		pass
