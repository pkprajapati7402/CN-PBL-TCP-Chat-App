import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox, simpledialog

class ChatClient:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nickname = None
        self.running = False
        
    def connect(self, host, port):
        try:
            self.client.connect((host, port))
            return True
        except Exception as e:
            messagebox.showerror("Connection Error", f"Could not connect to server: {e}")
            return False
    
    def receive(self):
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
    
    def send_message(self, message):
        try:
            full_message = f'{self.nickname}: {message}'
            self.client.send(full_message.encode('utf-8'))
            self.display_message(full_message)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to send message: {e}")
    
    def display_message(self, message):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, message + '\n')
        self.text_area.config(state=tk.DISABLED)
        self.text_area.see(tk.END)
    
    def on_send(self):
        message = self.message_entry.get()
        if message:
            self.send_message(message)
            self.message_entry.delete(0, tk.END)
    
    def on_closing(self):
        self.running = False
        try:
            self.client.close()
        except:
            pass
        self.window.destroy()
    
    def create_gui(self):
        self.window = tk.Tk()
        self.window.title(f"Chat - {self.nickname}")
        self.window.geometry("500x600")
        
        # Text area for messages
        self.text_area = scrolledtext.ScrolledText(self.window, state=tk.DISABLED, wrap=tk.WORD)
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Frame for entry and button
        input_frame = tk.Frame(self.window)
        input_frame.pack(padx=10, pady=5, fill=tk.X)
        
        # Message entry
        self.message_entry = tk.Entry(input_frame)
        self.message_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))
        self.message_entry.bind('<Return>', lambda event: self.on_send())
        
        # Send button
        send_button = tk.Button(input_frame, text="Send", command=self.on_send, width=10)
        send_button.pack(side=tk.RIGHT)
        
        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        
    def run(self):
        # Get nickname
        self.nickname = simpledialog.askstring("Nickname", "Choose a nickname:", parent=None)
        if not self.nickname:
            return
        
        # Get server details
        server_ip = simpledialog.askstring("Server IP", "Enter server IP address:", 
                                          initialvalue="127.0.0.1", parent=None)
        if not server_ip:
            return
        
        server_port = simpledialog.askinteger("Server Port", "Enter server port:", 
                                              initialvalue=5555, parent=None)
        if not server_port:
            return
        
        # Connect to server
        if not self.connect(server_ip, server_port):
            return
        
        self.running = True
        
        # Create GUI
        self.create_gui()
        
        # Start receive thread
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.daemon = True
        receive_thread.start()
        
        # Start GUI main loop
        self.window.mainloop()

if __name__ == '__main__':
    client = ChatClient()
    client.run()
