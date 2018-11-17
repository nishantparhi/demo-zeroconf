import socket
from zeroconf import ServiceInfo, Zeroconf

info = ServiceInfo("_service._tcp.local.",
                   "Nishant's Server._service._tcp.local.",
                   socket.inet_aton("127.0.0.1"), 9191, 0, 0,
                   {}, "ash-2.local.")

zeroconf = Zeroconf()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 9191))
server.listen(1)
zeroconf.register_service(info)
connection, address = server.accept()

while True:
    buffer = connection.recv(128)
    print(buffer)
    connection.send(buffer)

zeroconf.unregister_service(info)
connection.close()
server.close()
zeroconf.close()
