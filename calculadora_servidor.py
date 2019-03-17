import socket
ip = "10.0.2.15"
puerto = 8080
respuestas = 2
def lee_mensaje(cliente):
    condicion = True
    while condicion:
        operacion = cliente.recv(2048).decode("utf-8")
        op=["Salir","Sumar","Multiplicar"]

        try:
            print("Usted ha elegido la operacion: ",op[int(operacion)])

            if int(operacion) == 0:
                print("Ha seleccionado Salir")
                cliente.close()

            if int(operacion) == 1:
                num_1 = cliente.recv(2048).decode("utf-8")
                num_2 = cliente.recv(2048).decode("utf-8")
                resultado = int(num_1) + int(num_2)
                resultado = str.encode(str(resultado))
                cliente.send(resultado)

            if int(operacion) == 2:
                num_1 = cliente.recv(2048).decode("utf-8")
                num_2 = cliente.recv(2048).decode("utf-8")
                resultado = int(num_1) * int(num_2)
                resultado = str.encode(str(resultado))
                cliente.send(resultado)

        except Exception:
            print("Introduce un valor válido!")



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    serversocket.bind((ip, puerto))
    serversocket.listen(respuestas)
    print("Esperando conexion en el puerto:",puerto,"y en la ip:",ip)
    (cliente, address) = serversocket.accept()
    lee_mensaje(cliente)

except OSError:
    print("Fallo")

except KeyboardInterrupt:
    cliente.close()
    serversocket.close()
print("La conversación se acabó...")
