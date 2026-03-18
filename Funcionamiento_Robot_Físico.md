## 🔌 Conexión de USB a WSL

Se utiliza el siguiente comando para conectar un dispositivo USB desde Windows a WSL:
```bash
usbipd attach --busid 1-2 --wsl
```
Esto permite que el dispositivo (USB Serial Converter) sea reconocido dentro de Ubuntu como, por ejemplo, `/dev/ttyUSB0`.
