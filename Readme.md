# Chat Cliente-Servidor en Python

Este es un proyecto de chat en tiempo real utilizando sockets en Python, con una interfaz gráfica construida con Tkinter. Permite la comunicación entre múltiples clientes a través de un servidor central.

## Requisitos

- Python 3.x
- Tkinter (generalmente incluido con Python)
- Socket (también incluido con Python)

## Instalación

1. Asegúrate de tener Python 3.x instalado en tu máquina.
2. Clona el repositorio o descarga los archivos del proyecto.
3. Abre una terminal y navega a la carpeta donde guardaste el proyecto.

## Ejecutar el servidor

Para iniciar el servidor, abre una terminal y ejecuta:

```bash
python server.py
```

Esto iniciará el servidor escuchando en la dirección 127.0.0.1 y el puerto 12345.

```bash
Salida esperada del servidor:
Servidor escuchando en 127.0.0.1:12345
Diego (('127.0.0.1', 42770)) se ha conectado
Mensaje recibido de Diego: Hola
Juan (('127.0.0.1', 36438)) se ha conectado
Mensaje recibido de Juan: Hola
Ejecutar el cliente
Para ejecutar el cliente, abre una nueva terminal y ejecuta:
```

```bash
python cliente.py
```

### Instrucciones para usar el cliente

- Cuando se inicie el cliente, aparecerá una ventana solicitando que ingreses tu nombre de usuario (nickname).

- Después de ingresar tu nickname, presiona el botón "OK".

- La ventana de chat se abrirá y podrás comenzar a enviar y recibir mensajes en tiempo real.

### Interfaz gráfica del cliente

**Ventana de nickname**: Solicita al usuario que ingrese un nombre de usuario (nickname).
**Ventana de chat**: Una vez ingresado el nombre, se muestra una ventana de chat donde el usuario puede enviar y recibir mensajes.

### Características

- Soporta múltiples clientes conectados.

- Los mensajes se muestran en la interfaz gráfica de cada cliente.

- El servidor maneja la comunicación entre los clientes.

### Problemas conocidos

- Asegúrate de que el servidor esté ejecutándose antes de iniciar el cliente.

- Si ves dos ventanas del cliente, asegúrate de que el cliente esté correctamente configurado para ocultar la ventana de nickname después de ingresar el nombre.

# Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo LICENSE para más detalles.

# Créditos

Este proyecto fue desarrollado por [Diego Saavedra](https://statick88.github.io) como parte de una práctica de programación en Python. Agradezco a todos los colaboradores que contribuyeron al desarrollo del código y la interfaz gráfica.
