class Device:
    def __init__(self, device, hostname, ports, mac, ip4, ip6):
        self.device = device
        self.hostname = hostname
        self.ports = ports
        self.mac = mac
        self.ip4 = ip4
        self.ip6 = ip6

    def showInfo(self):
        print("El dispositivo es: " + self.device)
        print("El hostname del dispositivo es: " + self.device)
        print("El dispositivo tiene: " + self.device + " puertos.")
        print("La MAC del dispositivo es: " + self.device)
        print("IPv4: " + self.device)
        print("IPv6: " + self.device)


newDevice = Device("Switch", "S1", 24, "00:15:b2:a1:ac:28", "70.35.74.23", "ca30:a631:3292:6b11:0aaa:0d48:4293:c45e")
newDevice.showInfo()
