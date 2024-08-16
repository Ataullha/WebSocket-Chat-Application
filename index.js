// Get references to the chat area and input box
const chat = document.getElementById("chat");
const messageInput = document.getElementById("message");

// Create a new WebSocket connection to the server
const socket = new WebSocket("ws://localhost:6789");

// Function that gets called when a message is received from the server
socket.onmessage = function(event) {
    // Create a new div element to display the message
    const message = document.createElement("div");
    message.textContent = event.data; // Set the content of the message
    chat.appendChild(message); // Add the message to the chat area

    // Automatically scroll to the bottom of the chat area
    chat.scrollTop = chat.scrollHeight;
};

// Function to send a message to the server
function sendMessage() {
    const message = messageInput.value; // Get the value of the input box
    socket.send(message); // Send the message to the server
    messageInput.value = ""; // Clear the input box after sending
}