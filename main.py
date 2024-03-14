import socket
import threading
from pymongo import MongoClient
from datetime import datetime
import json


def handle_client(connection, address):
    print(f"Підключення з {address} встановлено")

    # Створення буфера для збору даних
    data_buffer = ""

    try:
        # Отримання даних від клієнта
        while True:
            data = connection.recv(1024).decode("utf-8")
            if not data:
                break
            data_buffer += data

        # Конвертація отриманих даних у словник
        data_dict = json.loads(data_buffer)

        # Підключення до MongoDB і вставка даних
        client = MongoClient("localhost", 27017)
        db = client["messages_db"]
        collection = db["messages"]

        post = {
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "username": data_dict.get("username"),
            "message": data_dict.get("message"),
        }

        collection.insert_one(post)
        print("Повідомлення збережено в MongoDB")
    except Exception as e:
        print(f"Виникла помилка: {e}")
    finally:
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
