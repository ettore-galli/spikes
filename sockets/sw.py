import socket


if __name__ == "__main__":

    addr_info = socket.getaddrinfo("towel.blinkenlights.nl", 23)
    addr = addr_info[0][-1]
    s = socket.socket()
    print("connecting...")
    s.connect(addr)
    print("connected, receiving...")
    while True:
        data = s.recv(500)
        print(str(data, "utf8"))
