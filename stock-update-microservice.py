import zmq
import json

def filter_in_stock(items):
    return [item for item in items if item.get("in_stock", False)]

def run_microservice():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    print("Microservice is running and waiting for requests...")

    while True:
        items = socket.recv_json()
        print("Received items from client...")

        in_stock_items = filter_in_stock(items)

        print("Sending back in-stock items...")
        socket.send_json(in_stock_items)

if __name__ == "__main__":
    run_microservice()
