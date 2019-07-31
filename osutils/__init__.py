from novaclient.client import Client as NovaClient
import ironicclient
import os
import re

class OSNode( object ):

    credentials = dict(
        region_name = os.environ.get('OS_REGION_NAME',''),
        username = os.environ.get('OS_USERNAME',''),
        password = os.environ.get('OS_PASSWORD',''),
        auth_url = os.environ.get('OS_AUTH_URL',''),
        project_id = os.environ.get('OS_PROJECT_ID',''),
        project_name = os.environ.get('OS_PROJECT_NAME',''),
        user_domain_name = os.environ.get('OS_USER_DOMAIN_NAME',''),
        project_domain_name = os.environ.get('OS_PROJECT_DOMAIN_NAME','')
    )

    def __init__( self ):
        self.ic = ironicclient.client.get_client(api_version=1, **self.credentials)
        self.nc = NovaClient(version=2, **self.credentials)

    @classmethod
    def filter_by_server_name( cls, name, query, search_opts):
        self = cls()
        kwargs = {}
        if search_opts:
            kwargs["search_opts"] = search_opts
        servers = self.nc.servers.list(**kwargs)
        result = []
        args = query.split('.')[1:]
        pattern = re.compile(name)
        for server in servers:
            if pattern.match(server.name):
                try:
                    intermediate = self.ic.node.get_by_instance_uuid(instance_uuid=server.id).to_dict()
                except Exception as e:
                    intermediate = {}
                for arg in args:
                    if arg == '[]':
                        return intermediate.keys()
                    else:
                        intermediate = intermediate.get(arg, {})
                result.append(dict(key=server.name, value=intermediate))
        return result
