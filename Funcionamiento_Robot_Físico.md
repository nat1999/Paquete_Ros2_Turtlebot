## 🔌 Conexión de USB a WSL

Se utiliza el siguiente comando para conectar un dispositivo USB desde Windows a WSL:
```bash
usbipd attach --busid 1-2 --wsl
```
Esto permite que el dispositivo (USB Serial Converter) sea reconocido dentro de Ubuntu como, por ejemplo, `/dev/ttyUSB0`.

## 🔍 Verificación del dispositivo en WSL

Una vez conectado el USB, se verifica que el sistema lo reconozca con:

```bash
ls /dev/ttyUSB*
```

Si el dispositivo está correctamente conectado, aparecerá una salida como:

```bash
/dev/ttyUSB0
```
Esto confirma que el convertidor USB-Serial está disponible para su uso en Ubuntu.


## 🚀 Ejecución del nodo Kobuki

Una vez detectado el dispositivo USB, se lanza el nodo del robot con:

```bash
ros2 launch kobuki_node kobuki_node-launch.py
```
Este comando inicia el driver de Kobuki, permitiendo la comunicación con el robot a través del puerto serial (`/dev/ttyUSB0`).

Con esto, el robot queda listo para recibir comandos y operar desde ROS 2.

## 🎮 Movimiento del robot

Se envían comandos de velocidad utilizando mensajes tipo `Twist`. Por ejemplo:

```bash
publishing #33: geometry_msgs.msg.Twist(linear=geometry_msgs.msg.Vector3(x=0.2, y=0.0, z=0.0), angular=geometry_msgs.msg.Vector3(x=0.0, y=0.0, z=0.0))
```
Este comando genera un movimiento lineal del robot hacia adelante.

Al ejecutar el nodo que publica estos mensajes, el robot responde de forma inmediata, confirmando la correcta comunicación entre ROS 2 y el robot físico.
