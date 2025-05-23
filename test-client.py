import zmq
import json

def test_microservice():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    test_items = [
        {"name": "Milk", "price": 3.49, "in_stock": True},
        {"name": "Eggs", "price": 2.99, "in_stock": False},
        {"name": "Bread", "price": 1.99, "in_stock": True}
    ]

    print("Making a request to the microservice with a list of items...")
    socket.send_json(test_items)

    print("Waiting for response from microservice...")
    response = socket.recv_json()

    print("Received filtered list of in-stock items:")
    print(json.dumps(response, indent=2))

if __name__ == "__main__":
    test_microservice()
