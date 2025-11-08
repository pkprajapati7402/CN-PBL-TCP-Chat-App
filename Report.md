# TCP-Based Multi-Client Chat Application with GUI
## Computer Networks - PBL Mini Project Report

---

## ABSTRACT

This project implements a real-time chat application using TCP socket programming in Python. The application follows a client-server architecture where multiple clients can connect to a central server and communicate with each other through a graphical user interface (GUI). The server handles concurrent client connections using multi-threading, enabling simultaneous message broadcasting to all connected clients. The client-side application is built using Python's Tkinter library, providing an intuitive and user-friendly interface for messaging. This project demonstrates fundamental concepts of computer networks including TCP/IP protocol, socket programming, multi-threading, client-server architecture, and network communication over LAN.

**Keywords:** TCP/IP, Socket Programming, Client-Server Architecture, Multi-threading, GUI, Network Communication

---

## INTRODUCTION

In the modern era of digital communication, understanding the underlying principles of network communication is essential for computer science students. Chat applications serve as an excellent practical example to demonstrate how devices communicate over a network using standard protocols.

This project focuses on implementing a TCP-based chat application that allows multiple users on the same Local Area Network (LAN) to communicate in real-time. The Transmission Control Protocol (TCP) is a connection-oriented protocol that ensures reliable, ordered, and error-checked delivery of data between applications running on hosts communicating over an IP network.

### Key Features:
- **Multi-client support:** Multiple users can connect simultaneously
- **Real-time messaging:** Instant message delivery and broadcasting
- **Graphical User Interface:** User-friendly Tkinter-based GUI for clients
- **Thread-based architecture:** Non-blocking operations for smooth user experience
- **Cross-platform compatibility:** Works on Windows, Linux, and macOS
- **LAN-based communication:** Devices on the same Wi-Fi network can communicate

### Technologies Used:
- **Python 3.x:** Core programming language
- **Socket Library:** For network communication
- **Threading Library:** For concurrent client handling
- **Tkinter Library:** For GUI development

---

## PROBLEM STATEMENT

Traditional communication between computers on a local network often requires third-party applications or internet connectivity. There is a need for a simple, lightweight, and educational chat application that:

1. Demonstrates fundamental networking concepts using TCP protocol
2. Allows multiple clients to communicate simultaneously without internet dependency
3. Provides a user-friendly graphical interface for non-technical users
4. Handles multiple concurrent connections efficiently
5. Ensures reliable message delivery using TCP's connection-oriented approach
6. Works seamlessly across different devices on the same LAN

The challenge is to implement a robust client-server architecture that can handle:
- Multiple simultaneous client connections
- Real-time message broadcasting
- Client connection and disconnection events
- Thread-safe operations to prevent race conditions
- GUI responsiveness while handling network operations

---

## OBJECTIVE

### Primary Objectives:
1. **Implement TCP Socket Programming:** Create a server-client application using Python's socket library with TCP protocol
2. **Develop Multi-threaded Server:** Enable the server to handle multiple client connections concurrently
3. **Create GUI-based Client:** Design an intuitive graphical interface using Tkinter for user interaction
4. **Establish Real-time Communication:** Enable instant message broadcasting to all connected clients
5. **Demonstrate Network Concepts:** Practically implement concepts like IP addressing, port binding, and data transmission

### Secondary Objectives:
1. Handle graceful connection and disconnection of clients
2. Implement nickname-based user identification
3. Provide visual feedback for user actions
4. Ensure thread-safe operations for data consistency
5. Create a scalable architecture for future enhancements

### Learning Outcomes:
- Understanding of TCP/IP protocol stack
- Practical knowledge of socket programming
- Experience with multi-threaded applications
- GUI development skills
- Client-server architecture implementation
- Network debugging and troubleshooting

---

## METHODOLOGY

### System Architecture

The application follows a **Client-Server Architecture** with the following components:

```
┌─────────────────────────────────────────────────────────────┐
│                     SERVER (Laptop A)                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Main Thread: Accept Connections                     │  │
│  │  - Listens on 0.0.0.0:5555                          │  │
│  │  - Accepts new client connections                    │  │
│  └──────────────────┬───────────────────────────────────┘  │
│                     │                                        │
│  ┌─────────────────┴────────────────────────────────────┐  │
│  │  Client Handler Threads (One per client)             │  │
│  │  - Thread 1: Handle Client 1                         │  │
│  │  - Thread 2: Handle Client 2                         │  │
│  │  - Thread 3: Handle Client 3                         │  │
│  │  - Receive messages and broadcast to all             │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                              │
                    TCP Connections (Port 5555)
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
   ┌────▼─────┐         ┌────▼─────┐         ┌────▼─────┐
   │ CLIENT 1 │         │ CLIENT 2 │         │ CLIENT 3 │
   │(Laptop A)│         │(Laptop B)│         │(Laptop C)│
   └──────────┘         └──────────┘         └──────────┘
```

### Connection Type: **TCP (Transmission Control Protocol)**

**Why TCP?**
- **Reliable:** Guarantees delivery of messages in order
- **Connection-oriented:** Establishes a stable connection before data transfer
- **Error-checking:** Built-in mechanisms for error detection and correction
- **Flow control:** Manages data transmission rate to prevent overflow

### System Flowchart

```
                    SERVER FLOW
                         │
                         ▼
              ┌──────────────────────┐
              │   Start Server       │
              │   Bind to 0.0.0.0    │
              │   Port: 5555         │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Listen for         │
              │   Connections        │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Accept Client      │
              │   Connection         │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Request Nickname   │
              │   (Send 'NICK')      │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Receive Nickname   │
              │   Add to Lists       │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Broadcast Join     │
              │   Message            │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Create Handler     │
              │   Thread for Client  │
              └──────────┬───────────┘
                         │
                    ┌────┴────┐
                    │         │
                    ▼         ▼
         ┌──────────────┐   Return to
         │  Receive     │   Accept Loop
         │  Messages    │
         └──────┬───────┘
                │
                ▼
         ┌──────────────┐
         │  Broadcast   │
         │  to Others   │
         └──────────────┘


                    CLIENT FLOW
                         │
                         ▼
              ┌──────────────────────┐
              │   Start Client       │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Input Nickname     │
              │   (GUI Dialog)       │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Input Server IP    │
              │   and Port           │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Connect to Server  │
              │   socket.connect()   │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Receive 'NICK'     │
              │   Send Nickname      │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │   Create GUI Window  │
              │   (Tkinter)          │
              └──────────┬───────────┘
                         │
                    ┌────┴────┐
                    │         │
                    ▼         ▼
         ┌─────────────────────────┐
         │  Receive Thread         │
         │  - Listen for messages  │
         │  - Update GUI           │
         └─────────────────────────┘
                    │
         ┌─────────────────────────┐
         │  Main GUI Thread        │
         │  - Handle user input    │
         │  - Send messages        │
         └─────────────────────────┘
```

### Implementation Steps

#### Phase 1: Server Development
1. **Socket Creation:** Create a TCP socket using `socket.socket(AF_INET, SOCK_STREAM)`
2. **Binding:** Bind the socket to host `0.0.0.0` (all interfaces) and port `5555`
3. **Listening:** Set the server to listen for incoming connections
4. **Accept Connections:** Accept client connections in a loop
5. **Multi-threading:** Create a new thread for each connected client
6. **Message Broadcasting:** Receive messages from clients and broadcast to all others
7. **Client Management:** Handle client disconnections and remove from active lists

#### Phase 2: Client Development
1. **Socket Creation:** Create a TCP socket for server connection
2. **User Input:** Prompt for nickname, server IP, and port using Tkinter dialogs
3. **Connection:** Establish connection to the server
4. **GUI Creation:** Build the chat interface with:
   - ScrolledText widget for message display (read-only)
   - Entry widget for message input
   - Send button for message submission
5. **Receive Thread:** Create a separate thread to receive messages from server
6. **Message Handling:** Send user messages and display received messages in GUI
7. **Event Handling:** Handle window closing and disconnection gracefully

#### Phase 3: Testing and Deployment
1. **Local Testing:** Test server and client on the same machine (127.0.0.1)
2. **LAN Testing:** Test across multiple devices on the same Wi-Fi network
3. **Multi-client Testing:** Connect multiple clients simultaneously
4. **Error Handling:** Test disconnection scenarios and error conditions
5. **Performance Testing:** Evaluate message delivery speed and thread efficiency

### Network Configuration

**For Local Testing:**
- Server IP: `127.0.0.1` (localhost)
- Port: `5555`

**For LAN Testing:**
- Server IP: Local IP of server machine (e.g., `192.168.1.100`)
- Port: `5555`
- Ensure all devices are on the same Wi-Fi network
- Check firewall settings to allow connections on port 5555

**To Find Server IP (Windows):**
```powershell
ipconfig
```
Look for "IPv4 Address" under your active network adapter.

### Data Flow

1. **Client sends message:**
   ```
   Client → Server: "Alice: Hello everyone!"
   ```

2. **Server receives and broadcasts:**
   ```
   Server → Client B: "Alice: Hello everyone!"
   Server → Client C: "Alice: Hello everyone!"
   ```

3. **Sender displays their own message:**
   ```
   Client A displays: "Alice: Hello everyone!"
   ```

---

## SOURCE CODE SNIPPETS

### Server Implementation (server.py)

**1. Socket Creation and Binding:**
```python
import socket
import threading

HOST = '0.0.0.0'  # Listen on all network interfaces
PORT = 5555       # Port number

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

# Lists to store active clients and their nicknames
clients = []
nicknames = []
```

**2. Broadcasting Messages:**
```python
def broadcast(message, sender_client=None):
    """Send message to all clients except the sender"""
    for client in clients:
        if client != sender_client:
            try:
                client.send(message)
            except:
                remove_client(client)
```

**3. Client Handler Thread:**
```python
def handle_client(client):
    """Handle individual client in separate thread"""
    while True:
        try:
            # Receive message from client
            message = client.recv(1024)
            if message:
                # Broadcast to all other clients
                broadcast(message, client)
            else:
                remove_client(client)
                break
        except:
            remove_client(client)
            break
```

**4. Main Server Loop:**
```python
def receive():
    """Main loop to accept client connections"""
    print(f'Server is listening on {HOST}:{PORT}')
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')
        
        # Request nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        
        # Store client information
        nicknames.append(nickname)
        clients.append(client)
        
        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
        
        # Create handler thread for this client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()
```

### Client Implementation (client.py)

**1. ChatClient Class Structure:**
```python
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog

class ChatClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nickname = None
        self.running = False
```

**2. Connection to Server:**
```python
def connect(self, host, port):
    """Establish connection to server"""
    try:
        self.client.connect((host, port))
        return True
    except Exception as e:
        messagebox.showerror("Connection Error", 
                           f"Could not connect to server: {e}")
        return False
```

**3. Receive Messages Thread:**
```python
def receive(self):
    """Continuously receive messages from server"""
    while self.running:
        try:
            message = self.client.recv(1024).decode('utf-8')
            if message == 'NICK':
                self.client.send(self.nickname.encode('utf-8'))
            else:
                self.display_message(message)
        except:
            if self.running:
                messagebox.showerror("Error", "Connection lost!")
            self.running = False
            self.client.close()
            break
```

**4. GUI Creation:**
```python
def create_gui(self):
    """Create Tkinter GUI interface"""
    self.window = tk.Tk()
    self.window.title(f"Chat - {self.nickname}")
    self.window.geometry("500x600")
    
    # Text area for displaying messages
    self.text_area = scrolledtext.ScrolledText(
        self.window, state=tk.DISABLED, wrap=tk.WORD)
    self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
    
    # Input frame
    input_frame = tk.Frame(self.window)
    input_frame.pack(padx=10, pady=5, fill=tk.X)
    
    # Message entry box
    self.message_entry = tk.Entry(input_frame)
    self.message_entry.pack(side=tk.LEFT, fill=tk.X, 
                           expand=True, padx=(0, 5))
    self.message_entry.bind('<Return>', 
                           lambda event: self.on_send())
    
    # Send button
    send_button = tk.Button(input_frame, text="Send", 
                           command=self.on_send, width=10)
    send_button.pack(side=tk.RIGHT)
```

**5. Sending Messages:**
```python
def send_message(self, message):
    """Send message to server"""
    try:
        full_message = f'{self.nickname}: {message}'
        self.client.send(full_message.encode('utf-8'))
        self.display_message(full_message)
    except Exception as e:
        messagebox.showerror("Error", 
                           f"Failed to send message: {e}")

def on_send(self):
    """Handle send button click"""
    message = self.message_entry.get()
    if message:
        self.send_message(message)
        self.message_entry.delete(0, tk.END)
```

### Key Concepts Demonstrated

**1. TCP Socket Programming:**
- `socket.AF_INET`: IPv4 addressing
- `socket.SOCK_STREAM`: TCP protocol (connection-oriented)
- `bind()`: Associate socket with address
- `listen()`: Enable server to accept connections
- `accept()`: Accept incoming connection
- `connect()`: Connect to server
- `send()`: Send data over TCP connection
- `recv()`: Receive data from TCP connection

**2. Multi-threading:**
- Each client connection handled in separate thread
- GUI runs in main thread while receiving messages in background thread
- Prevents blocking operations from freezing the interface

**3. Encoding/Decoding:**
- `encode('utf-8')`: Convert string to bytes for transmission
- `decode('utf-8')`: Convert bytes back to string

---

## PURPOSE OF WORK

### Educational Purpose
This project serves as a practical implementation of theoretical concepts learned in Computer Networks courses:

1. **Understanding TCP/IP Protocol Stack:**
   - Transport Layer: TCP protocol implementation
   - Application Layer: Chat application protocol
   - Network Layer: IP addressing and routing

2. **Socket Programming:**
   - Creating and managing sockets
   - Client-server communication
   - Connection establishment and termination

3. **Concurrent Programming:**
   - Multi-threading concepts
   - Thread synchronization
   - Race condition prevention

4. **Network Application Development:**
   - Real-world application design
   - Error handling in network applications
   - User interface design for network applications

### Practical Applications

1. **LAN Communication:**
   - Office or home network messaging
   - No internet dependency
   - Privacy and security of local communication

2. **Educational Tool:**
   - Teaching networking concepts
   - Demonstrating client-server architecture
   - Understanding protocol design

3. **Foundation for Advanced Projects:**
   - Base for developing more complex chat applications
   - Understanding required for P2P applications
   - Framework for other network applications

### Skills Developed

1. **Technical Skills:**
   - Python programming
   - Network programming
   - GUI development
   - Debugging network applications

2. **Problem-Solving Skills:**
   - Handling concurrent connections
   - Managing state across multiple clients
   - Error handling and recovery

3. **System Design:**
   - Client-server architecture
   - Protocol design
   - Scalability considerations

---

## FUTURE SCOPE

### Enhancements

**1. Security Features:**
- **Encryption:** Implement SSL/TLS for encrypted communication
- **Authentication:** Add user login system with password protection
- **Access Control:** Implement admin privileges and user permissions

**2. Advanced Features:**
- **Private Messaging:** Direct messaging between two users
- **File Transfer:** Share files between clients
- **Voice/Video Chat:** Integrate multimedia communication
- **Message History:** Store and retrieve chat history
- **Typing Indicators:** Show when someone is typing
- **Read Receipts:** Confirmation of message delivery and reading
- **Emoji Support:** Enhanced text formatting and emojis

**3. Group Management:**
- **Multiple Chat Rooms:** Create and join different chat rooms
- **User Profiles:** Add profile pictures and status messages
- **User List:** Display list of online users
- **Kick/Ban Users:** Admin controls for user management

**4. Scalability Improvements:**
- **Database Integration:** Store user data and messages in database
- **Load Balancing:** Distribute load across multiple servers
- **Cloud Deployment:** Host on cloud platforms for internet access
- **Message Queuing:** Implement message queues for better performance

**5. User Interface:**
- **Modern UI Framework:** Use PyQt or Kivy for better aesthetics
- **Dark/Light Theme:** Theme customization
- **Notification System:** Desktop notifications for new messages
- **Sound Alerts:** Audio alerts for messages

**6. Protocol Enhancements:**
- **Message Acknowledgment:** Ensure message delivery confirmation
- **Offline Messages:** Store messages for offline users
- **Presence Information:** Show user online/offline/away status
- **Message Prioritization:** Priority levels for messages

**7. Mobile Application:**
- **Android/iOS Client:** Develop mobile versions
- **Cross-platform Sync:** Synchronize across devices
- **Push Notifications:** Mobile notifications

**8. Analytics and Monitoring:**
- **Server Statistics:** Monitor active connections and performance
- **Message Analytics:** Track message frequency and patterns
- **Error Logging:** Comprehensive logging system
- **Performance Metrics:** Monitor latency and throughput

**9. Compliance and Standards:**
- **XMPP Protocol:** Implement standard messaging protocol
- **WebSocket Support:** Add web-based client support
- **API Development:** REST API for third-party integration

### Migration Paths

**1. From TCP to UDP:**
- Implement UDP version for comparison
- Understand trade-offs between reliability and speed

**2. From Server-based to P2P:**
- Peer-to-peer architecture
- Decentralized communication

**3. From LAN to Internet:**
- Port forwarding configuration
- Dynamic DNS setup
- NAT traversal techniques

---

## CONCLUSION

This project successfully demonstrates the implementation of a **TCP-based multi-client chat application** using Python socket programming and Tkinter GUI. The application effectively showcases fundamental concepts of computer networks including:

### Key Achievements:

1. **Successful Implementation:** Created a fully functional chat application with server and client components
2. **Multi-client Support:** Implemented concurrent client handling using multi-threading
3. **User-Friendly Interface:** Developed an intuitive GUI using Tkinter
4. **Reliable Communication:** Utilized TCP protocol for reliable message delivery
5. **Real-time Broadcasting:** Achieved instant message broadcasting to all connected clients
6. **Error Handling:** Implemented robust error handling for connection issues

### Learning Outcomes:

Through this project, we gained practical experience in:
- **Socket Programming:** Understanding of TCP socket creation, binding, listening, and data transfer
- **Multi-threading:** Managing concurrent operations and thread-safe programming
- **Client-Server Architecture:** Designing and implementing distributed systems
- **Network Protocols:** Deep understanding of TCP/IP protocol stack
- **GUI Development:** Creating responsive and user-friendly interfaces
- **Network Debugging:** Identifying and resolving network communication issues

### Technical Insights:

1. **TCP Advantages:** The choice of TCP protocol ensured reliable, ordered delivery of messages, which is crucial for chat applications
2. **Threading Benefits:** Multi-threading allowed the server to handle multiple clients simultaneously and kept the client GUI responsive
3. **Broadcast Mechanism:** The server's ability to broadcast messages efficiently enabled real-time group communication
4. **Separation of Concerns:** Clear separation between network logic and GUI logic improved code maintainability

### Practical Applications:

The developed application can be used for:
- Educational purposes in networking courses
- LAN-based communication in offices or homes
- Understanding foundation for more complex messaging systems
- Base framework for developing advanced network applications

### Limitations Acknowledged:

1. No encryption or security features
2. Limited to LAN communication without additional configuration
3. No message persistence or history
4. Basic user interface without advanced features
5. No file transfer capability

### Final Remarks:

This project has been an excellent learning experience in understanding how modern chat applications work at a fundamental level. The concepts learned here form the foundation for understanding more complex networking applications and distributed systems. The modular design of the application allows for easy extensions and enhancements as outlined in the future scope.

The successful completion of this project demonstrates that with a solid understanding of networking concepts and socket programming, it is possible to create practical, real-world applications that facilitate communication between devices on a network.

---

## REFERENCES

### Books:
1. **Computer Networks (5th Edition)** - Andrew S. Tanenbaum, David J. Wetherall
   - Chapter 6: The Transport Layer (TCP)
   - Chapter 7: The Application Layer

2. **TCP/IP Illustrated, Volume 1: The Protocols** - W. Richard Stevens
   - Understanding TCP protocol in depth

3. **Python Network Programming** - Dr. M. O. Faruque Sarker, Sam Washington
   - Socket programming concepts and examples

### Online Documentation:
4. **Python Official Documentation**
   - Socket Library: https://docs.python.org/3/library/socket.html
   - Threading Library: https://docs.python.org/3/library/threading.html
   - Tkinter Documentation: https://docs.python.org/3/library/tkinter.html

5. **RFC Documents:**
   - RFC 793 - Transmission Control Protocol (TCP)
   - RFC 791 - Internet Protocol (IP)

### Online Resources:
6. **Real Python Tutorials**
   - Socket Programming in Python (Guide)
   - Multi-threaded Programming in Python

7. **GeeksforGeeks**
   - Socket Programming in Python
   - Multi-threading in Python
   - Client-Server Chat Application

8. **Stack Overflow**
   - Various solutions for socket programming issues
   - Tkinter GUI best practices

### Video Tutorials:
9. **Network Chuck** - Networking fundamentals and practical applications
10. **Tech With Tim** - Python socket programming tutorials

### Tools Used:
11. **Python 3.x** - Programming language
12. **VS Code** - Integrated Development Environment
13. **Windows PowerShell** - Command line interface for testing
14. **ipconfig** - Network configuration utility

### Academic Resources:
15. **Computer Networks Course Materials** - University curriculum and lecture notes
16. **IEEE Papers** - Research papers on network communication and chat applications

### GitHub Repositories:
17. Various open-source chat application repositories for reference and inspiration

---

## APPENDIX

### A. Installation and Setup

**Prerequisites:**
```powershell
# Verify Python installation
python --version

# Should be Python 3.6 or higher
```

**Running the Application:**

1. **Start Server:**
```powershell
cd C:\Users\PRINCE\Documents\GitHub\CN-PBL-TCP-Chat-App
python server.py
```

2. **Start Client:**
```powershell
cd C:\Users\PRINCE\Documents\GitHub\CN-PBL-TCP-Chat-App
python client.py
```

### B. Troubleshooting

**Common Issues:**

1. **Port Already in Use:**
   - Change PORT value in server.py to a different number (e.g., 5556)

2. **Connection Refused:**
   - Ensure server is running before starting clients
   - Verify correct IP address and port number
   - Check firewall settings

3. **GUI Not Responding:**
   - Issue with threading - restart the application
   - Ensure tkinter is properly installed

### C. Network Configuration Guide

**Finding Local IP Address:**
```powershell
ipconfig
```
Look for "IPv4 Address" under your Wi-Fi or Ethernet adapter.

**Testing Connectivity:**
```powershell
ping <server_ip_address>
```

---

**Project Repository:** https://github.com/pkprajapati7402/CN-PBL-TCP-Chat-App

**Project Date:** November 2025

**Course:** Computer Networks - PBL Mini Project

---

*End of Report*