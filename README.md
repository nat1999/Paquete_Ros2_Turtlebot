
## Paquetes del TurtleBot

Los paquetes del TurtleBot están organizados en diferentes ramas dentro del repositorio.  
A continuación, se presentan los principales paquetes incluidos en el proyecto:

- `kobuki_ros`
- `turtlebot2_bringup`
- `turtlebot2_commander`
- `turtlebot2_description`
- `turtlebot2_gazebo`
- `turtlebot2_nav`
- `turtlebot2_navigation`
- `turtlebot2_ros2`
- `turtlebot2_slam`
- `turtlebot_description`


## Instalación de Gazebo

Para ejecutar la simulación del TurtleBot es necesario instalar **Gazebo**.

### 1. Actualizar el sistema
```bash
sudo apt update
sudo apt upgrade
```
### 2. Instalar gazebo 
```bash
sudo apt install gazebo
```
### 3. Verificación de instalación
```bash
gazebo
```

## Instalar paquetes adicionales (recomendado para ROS / TurtleBot)
```bash
sudo apt install ros-humble-gazebo-ros-pkgs
```

## Visualización del robot en Gazebo

Para visualizar el robot en Gazebo, ejecuta el siguiente comando:

```bash
ros2 launch turtlebot2_gazebo turtlebot2_world.launch.py
```
<p align="center">
<img width="670" height="511" alt="image" src="https://github.com/user-attachments/assets/a54a003f-1f76-44c7-bd35-ea907f8a4a83" />
</p>

## Prueba de movimiento del robot

Para verificar si el robot realiza algún movimiento, se pueden enviar comandos de velocidad al tópico `/cmd_vel`.

### Movimiento en trayectoria recta
```bash
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.2}, angular: {z: 0.0}}" -1
```

### Movimiento en trayectoria circular 
```bash
ros2 topic pub /cmd_vel geometry_msgs/msg/Twist "{linear: {x: 0.0}, angular: {z: 0.5}}" -1
```

## 🤖 Pruebas con robot físico

Se realizan pruebas con el robot físico.  
➡️ [Ver detalles aquí](Funcionamiento_Robot_Físico.md)

