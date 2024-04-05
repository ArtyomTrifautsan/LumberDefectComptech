import json

data = {
    "cameras": [
        {
            "name":"camera1", 
            "input_address": {"ip": "127.0.0.1", "port": "61500"},
            "output_address": {"ip": "127.0.0.1", "port": "61501"},
        },
    ],
    "neural_networks": 
    [
        {
            "name":"nn1",
            "input_address": {"ip": "127.0.0.1", "port": "61501"},
            "output_address": {"ip": "127.0.0.1", "port": "61502"},
        },
    ],
	"guis": 
    [
        {
            "name":"gui",
            "input_address": {"ip": "127.0.0.1", "port": "61502"},
            "output_address": {"ip": "127.0.0.1", "port": "61503"},
        },
    ],
    "compositions": 
    [
        {
            "name":"composition1",
            "input_address": {"ip": "127.0.0.1", "port": "61503"},
            "output_address": {"ip": "127.0.0.1", "port": "61504"},
        },
    ],
}

with open('config/config.json', 'w') as fp:
	json.dump(data, fp, indent=4)