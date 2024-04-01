import json

data = {
    "router": {
        "name":"router",
        "ingress": "tcp://127.0.0.1:8499" 
    },
    "camera": {
        "name":"camera_proxy",
        "ingress": "tcp://127.0.0.1:8500",
        "egress": "tcp://127.0.0.1:8501"
    },
    "neural_network": {
    	"name":"camera_proxy",
        "ingress": "tcp://127.0.0.1:8503",
        "egress": "tcp://127.0.0.1:8504"
    },
    "composition": {
    	"name":"camera_proxy",
        "ingress": "tcp://127.0.0.1:8505",
        "egress": "tcp://127.0.0.1:8506"
    },
    "gui": {
    	"name":"camera_proxy",
        "ingress": "tcp://127.0.0.1:8507",
        "egress": "tcp://127.0.0.1:8508"
    }
}

with open('data.json', 'w') as fp:
	json.dump(data, fp, indent=4)
