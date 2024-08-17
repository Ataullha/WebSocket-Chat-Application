# WebSocket Chat Application

This is a simple WebSocket-based chat application. It allows multiple clients to connect to a server and send messages to each other in real-time.

## Prerequisites

- Python 3.7 or higher
- `pip` (Python package installer)

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/Ataullha/WebSocket-Chat-Application.git
cd WebSocket-Chat-Application
```

### 2. Install Dependencies

Install the required Python packages using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Run the WebSocket Server

Start the WebSocket server using the following command:

```bash
python server.py
```

This will start the server on `localhost` at port `6789`.

### 4. Open the Chat Client

Open `index.html` in your web browser:

```bash
start index.html  # On Windows
```

Alternatively, you can manually open `index.html` by double-clicking the file.

### 5. Start Chatting!

- Type your message in the input box at the bottom of the page.
- Click the "Send" button or press Enter to send your message.
- Your message will be broadcast to all connected clients (open multiple browser tab to verify locally).
