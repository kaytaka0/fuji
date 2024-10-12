import yaml
from databank import *
from utility import utils

config = {
    "apiVersion": "v1",
    "kind": "Service",
    "metadata": {
        "name": "kibana",
        "namespace": FUJI_NAMESPACE,
        "labels": {
            "app": "kibana"
        }
    },
    "spec": {
        "type": "NodePort",
        "ports": [
            {
                "port": 5601,
                "targetPort": 5601,
                "protocol": "TCP"
            }
        ]
    }
}

with open(utils.get_yaml_output_filename(__file__), 'w') as f:
        yaml.dump(config, f, default_flow_style=False)