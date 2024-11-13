import socket
import threading

SERVER_HOST = "127.0.0.1"
SERVER_PORT = 12345


class ChatServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = {}

    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Servidor escuchando en {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            threading.Thread(
                target=self.handle_client, args=(client_socket, client_address)
            ).start()

    def handle_client(self, client_socket, client_address):
        nickname = client_socket.recv(1024).decode("utf-8")
        self.clients[client_socket] = nickname
        print(f"{nickname} ({client_address}) se ha conectado")

        # Notificar a los demás usuarios sobre la conexión
        self.broadcast(f"{nickname} se ha unido al chat", client_socket)

        while True:
            try:
                message = client_socket.recv(1024).decode("utf-8")
                if not message:
                    break
                print(
                    f"Mensaje recibido de {nickname}: {message}"
                )  # Mensaje de depuración
                self.broadcast(f"{nickname}: {message}", client_socket)
            except Exception as e:
                print(f"Error al recibir mensaje de {nickname}: {e}")
                break

        # Desconectar al cliente
        print(f"{nickname} ({client_address}) se ha desconectado")
        self.broadcast(f"{nickname} se ha desconectado", client_socket)
        client_socket.close()
        del self.clients[client_socket]

    def broadcast(self, message, sender_socket):
        for client_socket in self.clients.keys():
            if client_socket != sender_socket:
                try:
                    client_socket.sendall(message.encode("utf-8"))
                    print(f"Mensaje enviado a {client_socket}")  # Depuración
                except Exception as e:
                    print(f"Error al enviar mensaje a {client_socket}: {e}")


# Iniciar servidor
if __name__ == "__main__":
    server = ChatServer(SERVER_HOST, SERVER_PORT)
    server.start_server()

