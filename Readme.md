# Aplicación de Chat en Red (Cliente-Servidor)

Este proyecto es una implementación sencilla de una aplicación de chat en red usando el modelo cliente-servidor en Python. El servidor escucha las conexiones de los clientes y retransmite los mensajes que recibe entre ellos. El cliente puede enviar mensajes y recibir los de otros usuarios conectados al mismo servidor.

## Requisitos

- Python 3.x instalado.
- Conexión a una red local para probar la comunicación entre los clientes y el servidor.

## Archivos del Proyecto

### **chat_server.py**

Este archivo contiene el código para el servidor que gestiona las conexiones de los clientes. El servidor escucha en un puerto específico y retransmite los mensajes entre los clientes conectados.

### **chat_client.py**

Este archivo contiene el código para el cliente. El cliente se conecta al servidor y puede enviar y recibir mensajes en tiempo real.

## Instrucciones de Uso

### Paso 1: Configuración de Direcciones IP

Asegúrate de que todas las computadoras (o dispositivos) estén en la misma red local. Asigna una dirección IP estática a cada máquina en la misma subred.

1. **Servidor**: El servidor debe tener una dirección IP estática (por ejemplo, **192.168.1.100**).
2. **Clientes**: Los clientes se conectarán usando la IP del servidor.

### Paso 2: Ejecutar el Servidor

1. En la computadora que actuará como servidor, abre una terminal y navega hasta la carpeta donde se encuentra **chat_server.py**.
2. Ejecuta el servidor con el siguiente comando:

```bash
python chat_server.py
```
El servidor estará en ejecución y esperando conexiones de los clientes.

## Paso 3: Ejecutar los Clientes

En las computadoras que actuarán como clientes, abre una terminal y navega hasta la carpeta donde se encuentra chat_client.py.

Cambia la variable host en el archivo chat_client.py para que apunte a la dirección 
IP del servidor. 

Por ejemplo:

```python
host = '192.168.1.100'  # IP del servidor
```
Ejecuta el cliente con el siguiente comando:

```bash
python chat_client.py
```
El cliente pedirá al usuario que elija un nombre (nickname). Después, el cliente estará listo para enviar y recibir mensajes en el chat.

## Paso 4: Usar el Chat

Una vez que el servidor y los clientes estén en ejecución, los clientes podrán enviar mensajes.

Los mensajes enviados por un cliente serán recibidos y retransmitidos por el servidor a todos los demás clientes conectados.

# Notas

El servidor permite que múltiples clientes se conecten al mismo tiempo y maneja los mensajes en hilos separados para cada cliente.

El cliente muestra los mensajes enviados por otros usuarios y permite a los usuarios enviar mensajes a través de la terminal.


## Comandos Básicos

Servidor: Escucha en todas las interfaces (0.0.0.0) y en el puerto 12345.

Cliente: El cliente pide un "nickname" para identificarse y luego interactúa en el chat enviando y recibiendo mensajes.

## Consideraciones de Seguridad

Este proyecto es una implementación básica sin características avanzadas de seguridad como autenticación o cifrado. En un entorno de producción real, se deben implementar medidas para garantizar la privacidad y seguridad de la comunicación.

## Mejoras Posibles

- Implementar mensajes privados entre usuarios.

- Agregar manejo de desconexión y reconexión de clientes.

- Implementar cifrado de mensajes (por ejemplo, usando TLS).

- Añadir una interfaz gráfica usando bibliotecas como Tkinter o PyQt.

# Contribuciones

Si deseas contribuir al proyecto, por favor realiza un fork del repositorio y abre un pull request con tus cambios. Asegúrate de seguir las buenas prácticas de desarrollo y pruebas.