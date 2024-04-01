from multiprocessing import Process
import json, time

from network_module.router_microservice import Router
from network_module.camera_microservice import CameraProxy


def main():
    config_data = load_config("data.json")

    child_processes = []

    router_process = Process(target=process_router, args=(config_data,))
    child_processes.append(router_process)

    camera_process = Process(target=process_camera, args=(config_data,))
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
    return config_data


def process_router(config):
    router = Router(
        egress_camera = config["camera"]["egress"],
        ingress_neural_network = config["neural_network"]["egress"],
        egress_neural_network = config["neural_network"]["ingress"],
        ingress_composition = config["composition"]["ingress"],
        egress_composition = config["composition"]["egress"],
        ingress_gui = config["gui"]["ingress"]
    )

    router.run()


def process_camera(config):
    camera_proxy = CameraProxy(
        config["camera"]["ingress"], 
        config["camera"]["egress"]
    )

    camera_proxy.run()


def process_nn():
    while(1):
        pass


def process_composotion():
    while(1):
        pass


def process_gui():
    while(1):
        pass


if __name__ == '__main__':
    main()
