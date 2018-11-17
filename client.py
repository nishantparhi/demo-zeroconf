import socket
from time import sleep
from zeroconf import ServiceBrowser, Zeroconf

finished = False

class MyListener:
    def remove_service(self, zeroconf, type, name):
        print(f"Service {name} removed")
    def add_service(self, zeroconf, type, name):
        info = zeroconf.get_service_info(type, name)
        print(f"Service {name} added and service info: {info}")
        address = ".".join(map(str, info.address))
        self.connect((address, info.port))
    def connect(self, sock):
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(sock)
        while True:
            client.send(input("send message to server: ").encode() + b" ")
            response = client.recv(1024)
            if response == b"exit\n":
                break
        client.close()
        global finished
        finished = True


zeroconf = Zeroconf()
listener = MyListener()
browser = ServiceBrowser(zeroconf, "_service._tcp.local.", listener)


while not finished:
    sleep(0.4)
zeroconf.close()
