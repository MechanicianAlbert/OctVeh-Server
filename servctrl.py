import os
import socket
import vehictrl as vc


PORT = 8888

def get_ip():
    process = os.popen('hostname -I')
    output = process.read()
    process.close()
    return output

def drive_by_order(order):
    print("Order: " + order)
    if order == "W":
        vc.moveFore()
    elif order == "S":
        vc.moveBack()
    elif order == "A":
        vc.moveLeft()
    elif order == "D":
        vc.moveRight()
    elif order == "Q":
        vc.moveForeLeft()
    elif order == "E":
        vc.moveForeRight()
    elif order == "Z":
        vc.moveBackLeft()
    elif order == "C":
        vc.moveBackRight()
    elif order == "SPACE":
        vc.stop()
    pass

def prepare():
    vc.init()
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((get_ip(), PORT))
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
                        reStr = str(buf.decode("utf-8")).strip()
                        if reStr == "0":
                            listen = False
                        else:
                            print("Receive msg from client: " + reStr)
                            drive_by_order(reStr)
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
