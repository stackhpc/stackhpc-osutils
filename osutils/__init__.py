from novaclient.client import Client as NovaClient
import ironicclient
import os
import re

class OSNode( object ):

    credentials = dict(
        username = os.environ.get('OS_USERNAME',''),
        password = os.environ.get('OS_PASSWORD',''),
        auth_url = os.environ.get('OS_AUTH_URL',''),
        project_id = os.environ.get('OS_PROJECT_ID',''),
        user_domain_name = os.environ.get('OS_USER_DOMAIN_NAME','')
    )

    def __init__( self ):
        self.ic = ironicclient.client.get_client(api_version=1, **self.credentials)
        self.nc = NovaClient(version=2, **self.credentials)

    @classmethod
    def filter_by_server_name( cls, name, query ):
        self = cls()
        servers = self.nc.servers.list()
        result = []
        args = query.split('.')[1:]
        pattern = re.compile(name)
        for server in servers:
            if pattern.match(server.name): 
                intermediate = self.ic.node.get_by_instance_uuid(instance_uuid=server.id).to_dict()
                for arg in args:
                    if arg == '[]':
                        return intermediate.keys()
                    else:
                        intermediate = intermediate.get(arg, None)
                result.append(dict(key=server.name, value=intermediate))
        return result
