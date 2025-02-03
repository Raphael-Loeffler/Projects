from socket import socket, AF_INET, SOCK_STREAM, timeout



PORT: int = 80
BYTE_BUFFER_SIZE: int = 4096

def get_url(url: str) -> str:
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
   return response.decode('latin-1')


if __name__ == "__main__":
   url: str = "www.codemanufaktur.com"
   response: str = get_url(url)
   print(f"{response}")
