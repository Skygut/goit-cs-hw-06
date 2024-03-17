import socket
import pymongo
import json

# Підключення до MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
collection = db["messages"]


def socket_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("localhost", 5000))
        s.listen()
        print("Socket server listening on port 5000")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                # Обробка отриманих даних
                data_dict = json.loads(data.decode("utf-8"))
                # Зберігання даних у MongoDB
                collection.insert_one(data_dict)
                print("Data saved to MongoDB")


if __name__ == "__main__":
    socket_server()
