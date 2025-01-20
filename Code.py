import socket

# Configuración del servidor (ajusta la IP y el puerto)
host = 'IP'
port = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    while True:
        mensaje = input("Tú: ")
        if mensaje == 'salir':
            break
        s.sendall(mensaje.encode())
        datos = s.recv(1024)
        print('Servidor:', datos.decode())
