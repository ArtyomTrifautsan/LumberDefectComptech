import json

data = {
    "cameras": [
        {
            "name":"camera1", 
            "input_address": {"ip": "127.0.0.1", "port": "8500"},
            "output_address": {"ip": "127.0.0.1", "port": "8501"},
        },
    ],
    "neural_networks": 
    [
        {
            "name":"nn1",
            "input_address": {"ip": "127.0.0.1", "port": "8501"},
            "output_address": {"ip": "127.0.0.1", "port": "8502"},
        },
    ],
	"guis": 
    [
        {
            "name":"gui",
            "input_address": {"ip": "127.0.0.1", "port": "8502"},
            "output_address": {"ip": "127.0.0.1", "port": "8503"},
        },
    ],
    "compositions": 
    [
        {
            "name":"composition1",
            "input_address": {"ip": "127.0.0.1", "port": "8503"},
            "output_address": {"ip": "127.0.0.1", "port": "8504"},
        },
    ],
}

with open('data.json', 'w') as fp:
	json.dump(data, fp, indent=4)
