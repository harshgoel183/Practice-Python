import socket
import sys #so that you can run system commands


# create socket (allows 2 comp to connect)
def socket_create():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as msg:
        print("Socket creation error: "+str(msg))


# Bind socket to port and w8 for client
def socket_bind():
        try:
            global host
            global port
            global s
            print("Binding socket to port: "+str(port))
            s.bind((host, port))
            s.listen(5)#allow server to accept connection
                        # 5 represents no of connection taking
                        #place before refusing any conn
        except socket.error as msg:
            print("Socket creation error: "+str(msg)+"\n"+"retrying...")
            socket_bind()
# Establish a connection with client(socket must be listening)
def socket_accept():
    conn, address = s.accept()
    print("Connection has been established | "+"IP "+address[0]+" | Port "+ str(address[1]))
    send_commands(conn)#once client is connected it is going to sit and w8 for our command
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:#since we have to send it
                                    #across connection, it needs
                                    #to be in bytes
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")#1024 is buffer size
            print(client_response, end="")

def main():
    socket_create()
    socket_bind()
    socket_accept()

main()
