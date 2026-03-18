## 🔌 Conexión de USB a WSL

Se utiliza el siguiente comando para conectar un dispositivo USB desde Windows a WSL:
```bash
usbipd attach --busid 1-2 --wsl
```
Esto permite que el dispositivo (USB Serial Converter) sea reconocido dentro de Ubuntu como, por ejemplo, `/dev/ttyUSB0`.

## 🔍 Verificación del dispositivo en WSL

Una vez conectado el USB, se verifica que el sistema lo reconozca con:

ls /dev/ttyUSB*

Si el dispositivo está correctamente conectado, aparecerá una salida como:

/dev/ttyUSB0

Esto confirma que el convertidor USB-Serial está disponible para su uso en Ubuntu.
