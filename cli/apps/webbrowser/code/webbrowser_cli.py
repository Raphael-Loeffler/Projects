from socket import socket, AF_INET, SOCK_STREAM, timeout

# TODO: in webbrowser_cli.py
# TODO: EXERCISES:
# TODO: 1. Get an input
# TODO: 2. Create an -html file. For example for input 'www.google.com' -> google.html

# TODO! Delete data at the beginning

PORT: int = 80
BYTE_BUFFER_SIZE: int = 4096

def get_url(url: str, filename: str) -> None:
   print("")
   client_socket: socket = socket(AF_INET, SOCK_STREAM) # AF_INET -> IPv4 & IPv6, SOCK_STREAM -> TCP
   client_socket.settimeout(5) # DoS -> Decline of Service
   client_socket.connect((url, PORT)) # HTTP: 80, HTTPS: 443
   request: bytes = b"GET / HTTP/1.1\r\nHost: " + url.encode() + b"\r\n\r\n"
   client_socket.sendall(request)
   response: bytes = b""
   while True:
      try:
         data = client_socket.recv(BYTE_BUFFER_SIZE) # 10_000: 4_000 (6_000), 4_000 (2_000), 2_000 (0)
         if not data:
            break
         response += data
      except timeout:
         break
   client_socket.close()

   with open(f"/home/raphael/GitHub/Projects/cli/apps/webbrowser/files/{filename}.html", 'w') as file:
      file.write(response.decode('latin-1'))



if __name__ == "__main__":
   url: str = input("Please enter url: ")
   name: str = input("Please enter filename: ")
   get_url(url=url, filename=name)
