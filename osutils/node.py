from __future__ import print_function
from osutils.common import Connection
import re


class Node(object):
    def __init__(self):
        self.client = Connection().client

    @classmethod
    def filter_by_server_name(cls, pattern, query):
        self = cls()
        pattern = re.compile(pattern)
        query["instance_name"] = "instance_info.display_name"
        _result = Node.get_metadata(query)
        result = []
        for r in _result:
            instance_name = r["value"].pop("instance_name")
            if instance_name and pattern.match(instance_name):
                result.append(dict(key=instance_name, value=r["value"]))
        return result

    @classmethod
    def get_metadata(cls, query):
        self = cls()
        result = []
        kwargs = {}
        for node in self.client.baremetal.nodes(details=True, **kwargs):
            _result = {}
            for k, q in query.items():
                args = q.split(".")
                intermediate = node
                for arg in args:
                    if arg == "*":
                        intermediate = intermediate.keys()
                        break
                    elif arg == "":
                        continue
                    else:
                        intermediate = intermediate.get(arg, {})
                _result[k] = intermediate or None
            result.append(dict(key=node.name, value=_result))
        return result
