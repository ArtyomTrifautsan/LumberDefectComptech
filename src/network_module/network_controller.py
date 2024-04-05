import zmq


class NetworkController:

	def __init__(self, config):
		input_ip = config["input_address"]["ip"]
		input_port = config["input_address"]["port"]
		input_address = f"tcp://{input_ip}:{input_port}"

		output_ip = config["output_address"]["ip"]
		output_port = config["output_address"]["port"]
		output_address = f"tcp://{output_ip}:{output_port}"

		self.context = zmq.Context()

		self.input_socket = self.context.socket(zmq.PULL)
		self.input_socket.bind(input_address)

		self.output_socket = self.context.socket(zmq.PUSH)
		self.output_socket.connect(output_address)


	def accept_message(self):
		#print("<Receiver: wainig for message>")
		message = self.input_socket.recv_multipart()[0]
		#print("Receiver: ok")
		return message


	def send_message(self, message):
		#print(f"send: {message}")
		self.output_socket.send(message)

