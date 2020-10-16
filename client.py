import socket


def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((socket.gethostname(), 12345))

    echo_data = "hello server!"
    print(f"Sending server: {echo_data}")
    client.send(echo_data.encode('utf-8'))

    echo_from_server = client.recv(1024)
    print(f"Received from server: {echo_from_server}")

    client.close()


if __name__ == '__main__':
    main()
