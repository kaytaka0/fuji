import yaml
from databank import *
from utility import utils


config = {
    "apiVersion": "apps/v1",
    "kind": "StatefulSet",
    "metadata": {
        "name": "elasticsearch",
        "namespace": FUJI_NAMESPACE,
        "labels": {
            "app": "elasticsearch"
        }
    },
    "spec": {
        "serviceName": "elasticsearch",
        "replicas": 2,
        "selector": {
            "matchLabels": {
                "app": "elasticsearch"
            }
        },
        "template": {
            "metadata": {
                "labels": {
                    "app": "elasticsearch"
                }
            },
            "spec": {
                "containers": [
                    {
                        "name": "elasticsearch",
                        "image": "docker.elastic.co/elasticsearch/elasticsearch:8.15.2",
                        "ports": [
                            {
                                "containerPort": 9200,
                                "name": "http"
                            },
                            {
                                "containerPort": 9300,
                                "name": "transport"
                            }
                        ],
                        "env": [
                            {
                                "name": "discovery.type",
                                "value": "single-node"
                            },
                            {
                                "name": "xpack.security.enabled",
                                "value": "false"
                            },
                            {"name": "ES_JAVA_OPTS", "value": "-Xms1g -Xmx1g"},
                            {"name": "ELASTIC_PASSWORD", "value": "password"}
                        ],
                        "resources": {
                            "requests": {
                                "memory": "2Gi",
                                "cpu": "1"
                            },
                            "limits": {
                                "memory": "2Gi",
                                "cpu": "1"
                            }
                        },
                        "volumeMounts": [
                            {
                                "name": "data",
                                "mountPath": "/usr/share/elasticsearch/data"
                            }
                        ]
                    }
                ]
            }
        },
        "volumeClaimTemplates": [
            {
                "metadata": {
                    "name": "data"
                },
                "spec": {
                    "accessModes": ["ReadWriteOnce"],
                    "resources": {
                        "requests": {
                            "storage": "10Gi"
                        }
                    }
                }
            }
        ]
    }
}


with open(utils.get_yaml_output_filename(__file__), 'w') as f:
    yaml.dump(config, f, default_flow_style=False)