Tarea Computer Security ARP Spoofing.

En este repositorio se encuentran los dos programas de la tarea de ARP Spoofing.

El programa 1 llamado spoofer.py es el programa que se encarga de realizar el spoofing a la maquina destino.

El programa 2 detector.py detecta si hay cambios en la tabla ARP en lapsos de 10 segundos y verifica si
existen ips con la misma MAC, si esto es detectado, lanza el mensaje de posible ARP Spoofing y lista las
direcciones MAC duplicadas y las ips que están asociadas a ellas.

Requisitos previos:
- Tener Python 3 instalado.
- Tener pip y venv instalado.

Para usar el script spoofer.py en la computadora atacante es necesario realizar lo siguiente:
```
// Ingresar a la carpeta ráiz del repositorio
cd cs-tarea-arp
// Instalar dependencias
python -m venv .env && source .env/bin/activate && pip install -r requirements.txt
```
Para ejecutar el script spoofer.py:
```
sudo .env/bin/python spoofer.py IP_DESTINO IP_ROUTER
```
![image](https://github.com/acyclicstudent/cs-tarea-arp/assets/20765048/81c2ee5c-4552-4243-9454-cc7c7df9956e)

El script recibe los siguientes argumentos:
- IP_DESTINO (Requerido): Dirección ip del objetivo.
- IP_ROUTER (Requerido): Dirección ip del router.

Para usar el script detector.py en la computadora atacada, solo basta con ejecutar el script de la siguiente forma (ya que no tiene dependencias externas):
```
// Ingresar a la carpeta ráiz del repositorio
python3 detector.py
```
![image](https://github.com/acyclicstudent/cs-tarea-arp/assets/20765048/8323b0ec-da9d-4765-84b4-7f353f82c241)


Al hacer ejecutar el script spoofer.py, podremos ver que en la maquina atacada el comando ARP nos da una salida como está:
![image](https://github.com/acyclicstudent/cs-tarea-arp/assets/20765048/533345a9-f7e6-42ae-a3ec-0478504dd0dc)
En la cuál podemos observar que la ip del router tiene la misma dirección mac que el de la maquina atacante, además que mientras el 
spoofer se encuentra activo y hasta que la maquina vuelva a actualizar su tabla ARP, no se tendrá acceso a internet
ya que la maquina atacante no redirecciona los paquetes recibidos por la maquina atacada.

