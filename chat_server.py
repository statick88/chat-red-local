import socket
import threading

# Configuración del servidor
host = "127.0.0.1"  # Cambia a la IP local si ejecutas el servidor en otra máquina
port = 12345  # Puerto para la conexión

# Crear socket y enlazarlo
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []


# Transmitir mensajes a todos los clientes conectados
def broadcast(message):
    for client in clients:
        client.send(message)


# Manejar conexiones de cada cliente
def handle_client(client):
    while True:
        try:
            # Recibir mensaje y transmitirlo
            message = client.recv(1024)
            broadcast(message)
        except:
            # Remover cliente si se desconecta
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} salió del chat.".encode("utf-8"))
            nicknames.remove(nickname)
            break


# Aceptar conexiones de nuevos clientes
def receive():
    while True:
        client, address = server.accept()
        print(f"Conectado con {str(address)}")

        # Solicitar nickname al cliente
        client.send("NICK".encode("utf-8"))
        nickname = client.recv(1024).decode("utf-8")
        nicknames.append(nickname)
        clients.append(client)

        # Anunciar conexión del cliente y agregarlo a la lista de conexiones
        print(f"Nickname del cliente es {nickname}")
        broadcast(f"{nickname} se unió al chat!".encode("utf-8"))
        client.send("Conectado al chat!".encode("utf-8"))

        # Iniciar un hilo para manejar al cliente
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()


print("Servidor en ejecución...")
receive()
