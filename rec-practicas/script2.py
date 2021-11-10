class IPv4Interface:
    def __init__(self, ip):
        self.ip = ip

    def with_netmask(self):
        netmask = int(self.ip.split("/")[1])
        print('.'.join([str((0xffffffff << (32 - netmask) >> i) & 0xff) for i in [24, 16, 8, 0]]))


newInterface = IPv4Interface("192.168.1.2/24")
newInterface.with_netmask()

newInterface2 = IPv4Interface("192.168.1.2/30")
newInterface2.with_netmask()
