import socket
import pymongo
import json

PORT = 6000
# Підключення до MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["messages"]


def socket_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", PORT))
        s.listen()
        print(f"Сокет сервер слухає порт {PORT}")
        conn, addr = s.accept()
        with conn:
            print(f"Підключено {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                try:
                    # Спроба декодувати та розібрати дані
                    data_dict = json.loads(data.decode("utf-8"))
                    print(data_dict)
                    # Спроба зберегти дані в MongoDB
                    collection.insert_one(data_dict)
                    print("Дані збережено в MongoDB")
                except (json.JSONDecodeError, pymongo.errors.PyMongoError) as e:
                    print(f"Помилка при обробці даних: {e}")


if __name__ == "__main__":
    socket_server()
