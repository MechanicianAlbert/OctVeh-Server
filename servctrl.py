import socket


HOST = '192.168.1.2'
PORT = 8888


def prepare():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen(5)

    keep = True
    while keep:
        try:
            print ('Wait for accept new connection')
            connection, address = sock.accept()
            connection.settimeout(1000)
            listen = True
            try:
                while listen:
                    print ('Listen to connection')
                    buf = connection.recv(1024)
                    if buf:
                        reStr = str(buf.decode("utf-8"))
                        if reStr == "0\n":
                            listen = False
                        else:
                            print("Receive msg from client: " + reStr)
                            connection.send(b"Reply from server: ")
                            connection.send(reStr.encode("utf-8"))
                    else:
                        break
            except socket.timeout:
                print ('Connection time out')
            finally:
                connection.close()
                pass
        except Exception:
            pass


prepare()
