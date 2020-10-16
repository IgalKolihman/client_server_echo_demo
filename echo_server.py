import socket


def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((socket.gethostname(), 12345))
    server.listen(1)

    print("Listening for a new client connection")
    conn, address = server.accept()
    print("Client connected!")

    print("Waiting for a message from the client...")
    client_data = conn.recv(1024)
    print(f"Received from client: {client_data}")
    conn.send(client_data)


if __name__ == '__main__':
    main()
