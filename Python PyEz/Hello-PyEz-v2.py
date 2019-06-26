import getpass
from jnpr.junos import Device

host = None
uname = None
pw = None

if host == None:
    host = input('Hostname or IP:')
if uname == None:
    uname = input('Username')
if pw == None:
    pw = getpass.getpass()

dev = Device(host=host, user=uname, password=pw)
dev.open()
pprint(dev.facts)
dev.close()