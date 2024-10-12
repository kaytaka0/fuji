import yaml
from databank import *
from utility import utils

config = {
    "apiVersion": "v1",
    "kind": "Service",
    "metadata": {
        "name": "elasticsearch",
        "namespace": FUJI_NAMESPACE,
        "labels": {
            "app": "elasticsearch"
        }
    },
    "spec": {
        "type": "NodePort",
        "ports": [
            {
                "name": "http",
                "port": 9200,
                "targetPort": 9200,
                "nodePort": 31920,
                "protocol": "TCP"
            },
            {
                "name": "transport",
                "port": 9300,
                "targetPort": 9300,
                "nodePort": 31930,
                "protocol": "TCP"
            }
        ],
        "selector": {
            "app": "elasticsearch"
        }
    }
}

with open(utils.get_yaml_output_filename(__file__), 'w') as f:
        yaml.dump(config, f, default_flow_style=False)