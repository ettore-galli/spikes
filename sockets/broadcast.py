import socket
import time

if __name__ == "__main__":

    addr_info = socket.getaddrinfo("localhost", 23)

    addr = [a for a in addr_info if "127" in a[-1][0]][0][-1]

    s = socket.socket()
    print(f"connecting to {addr}")
    # s.connect(addr)
    print("connected, receiving...")
    while True:
        content = f"Hello, {str(time.time())}"
        data = s.send(content.encode("utf-8"))
        time.sleep(0.1)
