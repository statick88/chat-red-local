import socket
import threading

# Configuración del cliente
host = "127.0.0.1"  # Cambia a la IP del servidor si está en otra máquina
port = 12345  # Asegúrate de que coincide con el puerto del servidor

nickname = input("Elige tu nickname: ")

# Crear socket y conectarse al servidor
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))


# Escuchar mensajes del servidor
def receive():
    while True:
        try:
            # Recibir mensaje del servidor
            message = client.recv(1024).decode("utf-8")
            if message == "NICK":
                client.send(nickname.encode("utf-8"))
            else:
                print(message)
        except:
            # Cerrar conexión si hay un error
            print("¡Error! Conexión cerrada.")
            client.close()
            break


# Enviar mensajes al servidor
def write():
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode("utf-8"))


# Iniciar hilos para recibir y escribir mensajes
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()
