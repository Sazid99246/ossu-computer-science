import socket

url = input("Enter a URL: ")
try:
    host = url.split("/")[2]
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect((host, 80))
    cmd = f'GET {url} HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    received_chars = 0
    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        received_chars += len(data)
        if received_chars <= 3000:
            print(data.decode(), end='')

    mysock.close()

    print("\nTotal number of characters received:", received_chars)

except (IndexError, ValueError, socket.gaierror) as e:
    print("Error: Invalid URL or failed to connect.")
    print("Please make sure you enter a valid URL and try again.")
