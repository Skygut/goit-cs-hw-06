import socket
import threading


def handle_client(connection, address):
    print(f"Підключення з {address} встановлено")
    # Тут ви можете додати логіку для обробки даних від клієнта
    connection.close()


def start_server(port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("", port))
    server.listen()
    print(f"Socket сервер слухає на порту {port}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()


# Запуск Socket сервера на порту 5000
start_server(5000)
