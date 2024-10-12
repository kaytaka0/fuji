import yaml
from databank import *
from utility import utils


config = {
    "apiVersion": "apps/v1",
    "kind": "Deployment",
    "metadata": {
        "name": "kibana",
        "namespace": FUJI_NAMESPACE,
        "labels": {
            "app": "kibana"
        }
    },
    "spec": {
        "replicas": 1,
        "selector": {
            "matchLabels": {
                "app": "kibana"
            }
        },
        "template": {
            "metadata": {
                "labels": {
                    "app": "kibana"
                }
            },
            "spec": {
                "containers": [
                    {
                        "name": "kibana",
                        "image": "docker.elastic.co/kibana/kibana:8.15.2",
                        "ports": [
                            {
                                "containerPort": 5601
                            }
                        ],
                        "env": [
                            {
                                "name": "ELASTICSEARCH_HOSTS",
                                "value": "http://elasticsearch:9200"
                            },
                            {
                                "name": "ELASTICSEARCH_USERNAME",
                                "value": ""
                            },
                            {
                                "name": "ELASTICSEARCH_PASSWORD",
                                "value": ""
                            },
                            {
                                "name": "ELASTICSEARCH_SSL_CERTIFICATEAUTHORITIES",
                                "value": ""
                            }
                        ]
                    }
                ]
            }
        }
    }
}

with open(utils.get_yaml_output_filename(__file__), 'w') as f:
        yaml.dump(config, f, default_flow_style=False)