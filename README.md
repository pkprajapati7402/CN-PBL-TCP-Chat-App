# TCP Chat Application with GUI 💬

A multi-client chat application built with Python using TCP socket programming and Tkinter GUI. This project demonstrates real-time communication between multiple clients over a Local Area Network (LAN).

![Python](https://img.shields.io/badge/Python-3.6+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![TCP](https://img.shields.io/badge/Protocol-TCP-orange.svg)

## 📋 Overview

This chat application uses a client-server architecture where:
- **Server**: Handles multiple client connections simultaneously using multi-threading
- **Client**: Provides a user-friendly GUI built with Tkinter for sending and receiving messages
- **Protocol**: TCP (Transmission Control Protocol) ensures reliable message delivery

## ✨ Features

- 🔌 **Multi-client Support**: Multiple users can connect and chat simultaneously
- 💬 **Real-time Messaging**: Instant message broadcasting to all connected clients
- 🖥️ **GUI Interface**: Intuitive graphical interface for easy interaction
- 🧵 **Multi-threaded**: Non-blocking operations for smooth performance
- 🌐 **LAN-based**: Works seamlessly on local networks without internet
- 👤 **Nickname System**: Each user is identified by their chosen nickname
- 📡 **Connection Notifications**: Alerts when users join or leave the chat

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually comes pre-installed with Python)
- Two or more devices on the same Wi-Fi network (for multi-device testing)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/pkprajapati7402/CN-PBL-TCP-Chat-App.git
   cd CN-PBL-TCP-Chat-App
   ```

2. **Verify Python installation**
   ```bash
   python --version
   ```

That's it! No additional dependencies required.

## 📖 Usage

### Step 1: Start the Server

On the host machine (Laptop A), run:

```bash
python server.py
```

You should see:
```
Server is listening on 0.0.0.0:5555
```

### Step 2: Find Server IP Address

On the server machine, find the local IP address:

**Windows:**
```powershell
ipconfig
```

**Linux/Mac:**
```bash
ifconfig
```

Look for the IPv4 address (e.g., `192.168.1.100`)

### Step 3: Start Client(s)

On any machine (same or different), run:

```bash
python client.py
```

You'll be prompted to:
1. **Enter Nickname**: Choose your display name
2. **Enter Server IP**: 
   - Use `127.0.0.1` for local testing
   - Use server's local IP (e.g., `192.168.1.100`) for LAN
3. **Enter Port**: Default is `5555`

### Step 4: Start Chatting!

- Type your message in the text box
- Click **Send** or press **Enter**
- Messages appear in the scrollable text area
- All connected clients receive your messages instantly

## 🖼️ Screenshots

### Server Console
```
Server is listening on 0.0.0.0:5555
Connected with ('192.168.1.105', 54321)
Nickname of the client is Alice
Connected with ('192.168.1.106', 54322)
Nickname of the client is Bob
```

### Client GUI
```
┌─────────────────────────────────────┐
│  Chat - Alice               [_][□][X]│
├─────────────────────────────────────┤
│ Alice joined the chat!              │
│ Bob joined the chat!                │
│ Alice: Hello everyone!              │
│ Bob: Hi Alice!                      │
│ Alice: How are you?                 │
│                                     │
├─────────────────────────────────────┤
│ [Type message here...     ] [Send]  │
└─────────────────────────────────────┘
```

## 🛠️ Configuration

### Change Server Port

Edit `server.py`:
```python
PORT = 5555  # Change to your desired port
```

Also update clients to connect to the new port.

### Change Host Address

The server listens on all interfaces by default (`0.0.0.0`). To restrict to localhost only:

```python
HOST = '127.0.0.1'  # Localhost only
```

## 🔧 Troubleshooting

### Connection Refused
- ✅ Ensure the server is running before starting clients
- ✅ Verify the correct IP address and port
- ✅ Check firewall settings (allow port 5555)

### Port Already in Use
- ✅ Close other applications using port 5555
- ✅ Or change the PORT in both server.py and client.py

### GUI Not Responding
- ✅ Restart the client application
- ✅ Check if Tkinter is properly installed

### Can't Connect from Another Device
- ✅ Ensure both devices are on the same Wi-Fi network
- ✅ Use the server's local IP, not 127.0.0.1
- ✅ Disable firewall temporarily to test

## 📁 Project Structure

```
CN-PBL-TCP-Chat-App/
│
├── server.py          # Server-side application
├── client.py          # Client-side GUI application
├── Prompt.md          # Project requirements
├── Report.md          # Detailed technical report
└── README.md          # This file
```

## 🎯 How It Works

1. **Server** listens for incoming connections on port 5555
2. When a **client** connects, server requests a nickname
3. Server creates a dedicated thread to handle each client
4. When a client sends a message, server broadcasts it to all other clients
5. Clients receive messages in a separate thread and update the GUI
6. When a client disconnects, server notifies all remaining clients

## 🧪 Testing

### Local Testing (Single Machine)
```bash
# Terminal 1
python server.py

# Terminal 2
python client.py
# Enter nickname: Alice
# Enter IP: 127.0.0.1
# Enter port: 5555

# Terminal 3
python client.py
# Enter nickname: Bob
# Enter IP: 127.0.0.1
# Enter port: 5555
```

### LAN Testing (Multiple Machines)
1. Start server on Laptop A
2. Find Laptop A's IP address (e.g., 192.168.1.100)
3. Start client on Laptop A using IP: 192.168.1.100
4. Start client on Laptop B using IP: 192.168.1.100
5. Both clients can now chat!

## 💡 Use Cases

- 📚 **Educational**: Learn socket programming and networking concepts
- 🏢 **Office Communication**: Quick messaging within LAN
- 🏠 **Home Network**: Family communication without internet
- 🎓 **Academic Projects**: Computer Networks lab assignments

## 🔮 Future Enhancements

- 🔐 Encryption for secure communication
- 📁 File transfer capabilities
- 💾 Message history and persistence
- 🎨 Enhanced UI with themes
- 📱 Mobile app versions
- 👥 Private messaging between users
- 🏠 Multiple chat rooms

## 📚 Technologies Used

- **Python 3.x** - Core programming language
- **Socket** - Network communication
- **Threading** - Concurrent client handling
- **Tkinter** - GUI framework

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

**Pankaj Kumar Prajapati**
- GitHub: [@pkprajapati7402](https://github.com/pkprajapati7402)
- Repository: [CN-PBL-TCP-Chat-App](https://github.com/pkprajapati7402/CN-PBL-TCP-Chat-App)

## 🙏 Acknowledgments

- Computer Networks course materials
- Python socket programming documentation
- Tkinter GUI tutorials

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Troubleshooting](#-troubleshooting) section
2. Review the detailed [Report.md](Report.md) file
3. Open an issue on GitHub

---

⭐ **If you find this project helpful, please give it a star!** ⭐

*Made with ❤️ for Computer Networks PBL Project*