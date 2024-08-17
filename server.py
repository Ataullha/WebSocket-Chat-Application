import asyncio
import websockets

# A set to keep track of connected clients
clients = set()

# This function handles new WebSocket connections and messages
async def handler(websocket):
    # Add the new client connection to the set of clients
    clients.add(websocket)
    print(f"New client connected: {websocket}")
    print(f"Current clients: {clients}")
    
    try:
        # Continuously listen for messages from this client
        async for message in websocket:
            print(f"Received message from {websocket}: {message}")
            # When a message is received, broadcast it to all other clients
            for client in clients:
                print(f"Sending message to {client}")
                await client.send(message)
    finally:
        # When the client disconnects, remove it from the set of clients
        clients.remove(websocket)
        print(f"Client disconnected: {websocket}")
        print(f"Current clients: {clients}")

# Start the WebSocket server on localhost at port 6789
start_server = websockets.serve(handler, "0.0.0.0", 6789)

# Print confirmation that the server has started
print('Server Started!')

# Run the WebSocket server forever
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()