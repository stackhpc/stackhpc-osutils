import openstack
import os
import re

class OSNode( object ):
    def __init__( self ):
        credentials = dict(
            region_name = os.environ.get('OS_REGION_NAME',''),
            username = os.environ.get('OS_USERNAME',''),
            password = os.environ.get('OS_PASSWORD',''),
            auth_url = os.environ.get('OS_AUTH_URL',''),
            project_id = os.environ.get('OS_PROJECT_ID',''),
            project_name = os.environ.get('OS_PROJECT_NAME',''),
            user_domain_name = os.environ.get('OS_USER_DOMAIN_NAME',''),
            project_domain_name = os.environ.get('OS_PROJECT_DOMAIN_NAME',''),
        )
        cloud = os.environ.get('OS_CLOUD','')
        if cloud:
            self.client = openstack.connect(cloud=cloud)
        else:
            self.client = openstack.connect(**credentials)

    @classmethod
    def filter_by_server_name(cls, pattern, query, all_projects):
        self = cls()
        servers = self.client.compute.servers(all_projects=all_projects)
        result = []
        args = query.split('.')[1:]
        pattern = re.compile(pattern)
        for server in servers:
            if pattern.match(server.name):
                intermediate = next(self.client.baremetal.nodes(instance_id=server.id, details=True), {})
                for arg in args:
                    if arg == '[]':
                        return intermediate.keys()
                    else:
                        intermediate = intermediate.get(arg, {})
                result.append(dict(key=server.name, value=intermediate))
        return result
