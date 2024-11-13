import socket
import tkinter as tk
import threading

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12345


class ChatClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.nickname = ""
        self.running = True
        self.chat_window = None
        self.message_box = None
        self.entry_box = None

    def connect_to_server(self):
        try:
            self.client_socket.connect((self.host, self.port))
            print("Conectado al servidor")
        except Exception as e:
            print(f"No se pudo conectar al servidor: {e}")

    def send_message(self, message):
        try:
            self.client_socket.sendall(message.encode("utf-8"))
        except Exception as e:
            print(f"Error al enviar mensaje: {e}")

    def receive_messages(self):
        while self.running:
            try:
                message = self.client_socket.recv(1024).decode("utf-8")
                print(f"Mensaje recibido: {message}")  # Depuración
                if message:
                    self.chat_window.after(0, self.display_message, message)
                else:
                    break
            except (OSError, socket.error) as e:
                print(f"Error al recibir mensaje: {e}")
                break

    def display_message(self, message):
        self.message_box.insert(tk.END, message)
        self.message_box.yview(tk.END)

    def setup_gui(self):
        self.window = tk.Tk()
        self.window.title("Chat Cliente")

        # Ventana de ingreso de nickname
        self.nickname_window = tk.Frame(self.window)
        self.nickname_window.pack(padx=10, pady=10)

        self.nickname_label = tk.Label(self.nickname_window, text="Nick:")
        self.nickname_label.pack(padx=10, pady=10)

        self.nickname_entry = tk.Entry(self.nickname_window)
        self.nickname_entry.pack(padx=10, pady=10)

        self.nickname_button = tk.Button(
            self.nickname_window, text="OK", command=self.set_nickname
        )
        self.nickname_button.pack(padx=10, pady=10)

        self.window.mainloop()

    def set_nickname(self):
        self.nickname = self.nickname_entry.get()
        if self.nickname:
            self.client_socket.sendall(self.nickname.encode("utf-8"))
            self.nickname_window.pack_forget()  # Ocultar la ventana de nickname
            self.create_chat_window()  # Mostrar la ventana de chat

    def create_chat_window(self):
        # Crear y mostrar la ventana de chat dentro de la ventana principal
        self.chat_window = tk.Frame(self.window)
        self.chat_window.pack(padx=10, pady=10)

        self.message_box = tk.Listbox(self.chat_window, height=15, width=50)
        self.message_box.pack(padx=10, pady=10)

        self.entry_box = tk.Entry(self.chat_window, width=40)
        self.entry_box.pack(padx=10, pady=10)

        self.send_button = tk.Button(
            self.chat_window, text="Enviar", command=self.on_send_message
        )
        self.send_button.pack(padx=10, pady=10)

        # Hilo para recibir mensajes
        threading.Thread(target=self.receive_messages, daemon=True).start()

    def on_send_message(self):
        message = self.entry_box.get()
        if message:
            self.send_message(message)
            self.display_message(
                f"{self.nickname}: {message}"
            )  # Mostrar el mensaje en el cliente
            self.entry_box.delete(0, tk.END)


# Ejecutar cliente
if __name__ == "__main__":
    client = ChatClient(SERVER_HOST, SERVER_PORT)
    client.connect_to_server()
    client.setup_gui()

