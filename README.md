# Stock Update Microservice for Lily

This microservice filters a list of grocery items to return only those currently in stock. It uses ZeroMQ for request-reply communication over a local socket.

## How to programmatically REQUEST data

Your main program must connect to the microservice using ZeroMQ. 
Request data format: Send a list of item objects (in JSON format) via a REQ socket.

Each item in the list should be a dictionary like:
```
{
  "name": "Apple",
  "price": 0.99,
  "in_stock": True
}
```
Example request call:
```
import zmq
import json

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

items = [
    {"name": "Apple", "price": 0.99, "in_stock": True},
    {"name": "Banana", "price": 0.99, "in_stock": False}
]

socket.send_json(items)
```
## How to programmatically RECEIVE data

After sending, the program waits for a JSON response that includes only the items currently in stock.

Example call:
```
response = socket.recv_json()
print("Filtered in-stock items:", response)
```

## UML Sequence Diagram

![UML Sequence Diagram](https://github.com/user-attachments/assets/3ffdda39-f489-4816-b723-e6c7a7be7159)

