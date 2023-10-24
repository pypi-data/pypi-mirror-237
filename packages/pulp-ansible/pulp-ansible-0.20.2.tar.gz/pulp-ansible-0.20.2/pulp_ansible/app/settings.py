import socket

from dynaconf import settings

LOGGING = {
    "loggers": {
        "pulp_ansible.app.tasks.collection.import_collection": {
            "level": "INFO",
            "handlers": ["collection_import"],
            "propagate": False,
        }
    },
    "handlers": {
        "collection_import": {
            "level": "DEBUG",
            "class": "pulp_ansible.app.logutils.CollectionImportHandler",
            "formatter": "simple",
        }
    },
    "dynaconf_merge": True,
}

ANSIBLE_API_HOSTNAME = "https://" + socket.getfqdn()
ANSIBLE_CONTENT_HOSTNAME = settings.CONTENT_ORIGIN + "/pulp/content"
ANSIBLE_SIGNATURE_REQUIRE_VERIFICATION = True
ANSIBLE_SIGNING_TASK_LIMITER = 10
ANSIBLE_DEFAULT_DISTRIBUTION_PATH = None
ANSIBLE_URL_NAMESPACE = ""
ANSIBLE_COLLECT_DOWNLOAD_LOG = False
ANSIBLE_COLLECT_DOWNLOAD_COUNT = False
ANSIBLE_AUTHENTICATION_CLASSES = settings.REST_FRAMEWORK["DEFAULT_AUTHENTICATION_CLASSES"]
ANSIBLE_PERMISSION_CLASSES = settings.REST_FRAMEWORK["DEFAULT_PERMISSION_CLASSES"]

DRF_ACCESS_POLICY = {
    "dynaconf_merge_unique": True,
    "reusable_conditions": ["pulp_ansible.app.global_access_conditions"],
}
