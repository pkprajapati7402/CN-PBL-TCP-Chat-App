# Python Chat Application using Socket Programming (TCP) with GUI

Create two Python files: server.py and client.py

---

## server.py
- Use Python's socket and threading libraries.
- The server should:
  1. Listen on host '0.0.0.0' and port 5555.
  2. Accept multiple client connections.
  3. Receive messages from clients and broadcast them to all other clients.
  4. Print to console when a client connects or disconnects.
- Keep the code simple and clear, without GUI or encryption.

---

## client.py
- Use Python's socket, threading, and tkinter libraries.
- The client should:
  1. Ask for a nickname.
  2. Connect to the server using its IP address and port (example: 192.168.x.x, 5555).
  3. Open a Tkinter window with:
     - A text area to show messages (read-only).
     - An entry box to type a message.
     - A Send button.
  4. Send messages to the server and display received messages in the text area.
  5. Use a separate thread to receive messages, so the GUI stays responsive.

---

## Setup
- Run server.py on Laptop A (the host).
- Run client.py on Laptop A and on Laptop B (both on the same Wi-Fi).
- Laptop B must set the server IP in client.py to Laptop A’s local IP address.
- After running both clients, they can chat through the GUI.

---

## Output
- Provide complete working code for both files: server.py and client.py
- Do not include any extra features or explanations.
