import socket
import threading

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8888))

servidor.listen()

print("[SERVER] Server opened.")

cliente, end = servidor.accept()

print("[SERVER] Client Connect.")

terminado = False

while not terminado:
    msg = cliente.recv(1024).decode('utf-8')
    if msg == 'tt':
        terminado = True
    else:
        print(msg)
    cliente.send(input('Mensagem: ').encode('utf-8'))

cliente.close()
servidor.close()