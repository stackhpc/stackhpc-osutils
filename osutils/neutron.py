from __future__ import print_function
from osutil.common import Connection
from neutronclient.v2_0 import client as nc

class LBaaS( object ):
    def __init__( self ):
        self.client = Connection().client
        self.neutron = nc.Client(session=Connection().client.session)

    @classmethod
    def list_lbs(cls, key='name'):
        keys = ['description',
                'admin_state_up',
                'tenant_id',
                'provisioning_status',
                'vip_subnet_id',
                'listeners',
                'vip_address',
                'vip_port_id',
                'provider',
                'pools',
                'id',
                'operating_status',
                'name']
        if key in keys:
            self = cls()
            lbs = self.neutron.list_lbaas_loadbalancers().get('loadbalancers')
            return {key: [i[key] for i in lbs]}
        else:
            raise KeyError('Available keys are [%s].' % ', '.join(keys))

    @classmethod
    def delete_lbs(cls, names, really_delete=False, cascade=False):
        self = cls()
        if not isinstance(names, list):
            names = [names]
        for lb_name in names:
            lbs = self.neutron.list_lbaas_loadbalancers(name=lb_name).get('loadbalancers')
            for lb in lbs:
                lb_id = lb.get('id')
                print('Loadbalancer ', lb_id)
                if cascade:
                    listeners = lb.get('listeners')
                    pools = lb.get('pools')
                    for l in listeners:
                        listener_id = l.get('id')
                        print('-> Listener ', listener_id)
                        if really_delete:
                            self.neutron.delete_listener(listener_id)
                    for p in pools:
                        pool_id = p.get('id')
                        pool = self.neutron.show_lbaas_pool(pool_id).get('pool')
                        hm_id = pool.get('healthmonitor_id')
                        print('-> Pool ', pool_id, ' -> Health monitor ', hm_id)
                        if really_delete:
                            if hm_id:
                                self.neutron.delete_lbaas_healthmonitor(hm_id)
                            self.neutron.delete_lbaas_pool(pool_id)
                if really_delete:
                    self.neutron.delete_loadbalancer(lb_id)
        if not really_delete:
            print("Phew, that was a dry run. Set really_delete=True for result.")
