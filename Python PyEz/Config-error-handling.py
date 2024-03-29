from jnpr.junos.device import Device
from jnpr.junos.utils.config import Config
from pprint import pprint
from jnpr.junos.exception import *

junos_hosts = ['172.25.11.1','1.1.1.1']
Device.auto_probe = 10

for ip in junos_hosts:
    try:
        dev = Device(host=ip, user='lab', password='lab123')
        dev.open()
        config = Config(dev)
        config.lock()
        config.load(path='add_snmp.conf', merge=True)
        config.pdiff()
        config.commit()
        config.unlock()
        dev.close()
    except ConnectionTimeoutError as e:
        print('Connection time out!')