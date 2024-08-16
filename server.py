# Import necessary modules
import asyncio
import websockets

# A set to keep track of connected clients
clients = set()

# This function handles new WebSocket connections and messages
async def handler(websocket, path):
    # Add the new client connection to the set of clients
    clients.add(websocket)
    try:
        # Continuously listen for messages from this client
        async for message in websocket:
            # When a message is received, broadcast it to all other clients
            for client in clients:
                # if client != websocket:  # Don't send the message back to the sender
                await client.send(message)
    finally:
        # When the client disconnects, remove it from the set of clients
        clients.remove(websocket)

# Start the WebSocket server on localhost at port 6789
start_server = websockets.serve(handler, "localhost", 6789)

# Run the WebSocket server forever
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()