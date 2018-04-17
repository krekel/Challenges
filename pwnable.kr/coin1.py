import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = 'localhost'
port = 9007

s.connect((server, port))
s.recv(10024)

for _ in range(100):
    response = s.recv(1024).decode('utf-8')
    print(response)
    values = response.strip().split(' ')
    n = int(values[0].split('=')[1])
    c = int(values[1].split('=')[1])
    low = 0
    hi = n

    for _ in range(c):
        mid = int((low + hi)/2)

        payload = ' '.join(str(x) for x in range(low, mid)).encode('utf-8')
        s.send(payload + b'\n')

        value = s.recv(4096).decode('utf-8').replace('\n', '')

        if int(value) % 10 == 0:
            # go right
            low = int((low + hi)/2)
        else:
            # go left
            hi = int((low + hi)/2)
    s.send(str(low).encode('utf-8') + b'\n')
    print(s.recv(1024))
print(s.recv(1024))
