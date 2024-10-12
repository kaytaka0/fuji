
import yaml
from databank import *
from utility import utils


config = {
    "kind": "Namespace",
    "apiVersion": "v1",
    "metadata": {
        "name": FUJI_NAMESPACE,
        "labels": {
            "name": FUJI_NAMESPACE
        }
    }
}


with open(utils.get_yaml_output_filename(__file__), 'w') as f:
        yaml.dump(config, f, default_flow_style=False)