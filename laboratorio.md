# Laboratorio: Comunicación entre servidor y clientes en red local.

Este tutorial guiará a los estudiantes a configurar una red local entre una máquina servidor y varios clientes en Windows, permitiendo la comunicación a través de un puerto específico.

## Objetivos:

- Configurar una máquina servidor y varios clientes en una red local usando direcciones IP estáticas.

- Verificar la comunicación entre las máquinas usando herramientas como ping y telnet.

- Probar la comunicación usando una aplicación cliente-servidor simple.

- Resolver posibles problemas de red y firewall.

### 1. Preparación del entorno:

Antes de comenzar con la configuración, asegúrate de que tanto la máquina servidor como las máquinas cliente estén conectadas a la misma red local.

### 2. Configuración de la máquina servidor (Windows)

**Asignar una IP estática**: La máquina servidor será el punto central de la comunicación. Para asignar una dirección IP estática:

- Ve a Panel de Control > Centro de redes y recursos compartidos > Cambiar configuración del adaptador.

- Haz clic derecho sobre tu adaptador de red (por ejemplo, Ethernet) y selecciona Propiedades.

- Selecciona Protocolo de Internet versión 4 (TCP/IPv4) y haz clic en Propiedades.

- Marca Usar la siguiente dirección IP y asigna una IP estática, por ejemplo:

**IP**: 192.168.100.139

**Máscara de subred**: 255.255.255.0

**Puerta de enlace predeterminada (si es necesario)**: 192.168.100.1 (o la IP del enrutador si es necesario).

**Configuración del firewall**: Asegúrate de que el firewall de Windows permite conexiones al puerto en el que se ejecutará el servidor. Por ejemplo, si tu servidor usa el puerto 12345:

- Abre el Panel de Control > Sistema y seguridad > Firewall de Windows.

- Haz clic en Configuración avanzada a la izquierda.

- En el panel izquierdo, selecciona Reglas de entrada y haz clic en Nueva regla.

- Selecciona Puerto, luego elige TCP y coloca el puerto 12345.

- Permite la conexión y asigna un nombre a la regla, como "Puerto 12345".

- **Verificar la conexión**: Puedes verificar que el servidor esté escuchando en el puerto con el siguiente comando en la terminal:

```bash
netstat -tuln | findstr 12345
```

**Aplicación servidor**: Asegúrate de tener una aplicación simple en el servidor que escuche en el puerto configurado. Un ejemplo básico sería una aplicación Python con socket.

### 3. Configuración de las máquinas cliente (Windows)

Asignar una IP estática en las máquinas cliente: Similar al servidor, debes asignar una IP estática en las máquinas cliente para que estén en la misma red que el servidor.

- Abre Panel de Control > Centro de redes y recursos compartidos > Cambiar configuración del adaptador.

- Haz clic derecho en el adaptador de red y selecciona Propiedades.

- Selecciona Protocolo de Internet versión 4 (TCP/IPv4) y haz clic en Propiedades.

- Marca Usar la siguiente dirección IP y asigna una IP estática dentro del mismo rango que el servidor, por ejemplo:

**IP del cliente**: 192.168.100.140 (o cualquier otra IP dentro de 192.168.100.2 a 192.168.100.254)

**Máscara de subred**: 255.255.255.0

**Puerta de enlace predeterminada**: 192.168.100.1 (si es necesario).

#### Verificar la conexión:

Abre Símbolo del sistema (cmd) y ejecuta:

```bash
ping 192.168.100.139
```

Si la máquina cliente recibe respuestas del servidor, la comunicación básica está funcionando.

#### Probar la conectividad al puerto del servidor:

- Instala Telnet si aún no está disponible:

- Abre el Panel de Control > Programas > Activar o desactivar características de Windows.

- Marca Cliente Telnet y haz clic en Aceptar.

- Desde el cliente, abre Símbolo del sistema y ejecuta:

```bash
telnet 192.168.100.139 12345
```

Si la conexión es exitosa, el servidor está disponible en ese puerto.

### 4. Resolución de problemas comunes

**Problema 1**: No se puede hacer ping entre las máquinas

- Verifica que las IPs configuradas están en el mismo rango de red.

- Asegúrate de que el firewall no está bloqueando las solicitudes de ping.

- Si estás utilizando un software de seguridad adicional, verifica que no esté bloqueando la comunicación en la red local.

**Problema 2**: El puerto no está accesible (telnet o nc no conecta)

- Asegúrate de que el servidor está escuchando en el puerto correcto y que el firewall de Windows en el servidor está configurado para permitir conexiones al puerto.

- Revisa que la máquina cliente pueda acceder al puerto del servidor sin restricciones.

**Problema 3**: Dirección IP de cliente fuera de rango

- Asegúrate de que la IP asignada en el cliente esté dentro del mismo rango de red que el servidor (192.168.100.x).

- Verifica que la máscara de subred sea 255.255.255.0 en todas las máquinas.

### 5. Resumen de la configuración

- Componente Dirección IP Máscara de Subred Puerta de Enlace

**Servidor** 192.168.100.139 255.255.255.0 192.168.100.1

**Cliente 1** 192.168.100.140 255.255.255.0 192.168.100.1

**Cliente 2** 192.168.100.141 255.255.255.0 192.168.100.1

### 6. Verificación final

- Verifica que todos los clientes pueden hacer ping al servidor.

- Verifica que el servidor está escuchando en el puerto adecuado.

- Verifica que los clientes pueden conectarse al puerto del servidor con telnet o nc.
