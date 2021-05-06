import openstack
import os

class Connection( object ):
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
