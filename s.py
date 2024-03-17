import socket

 
HOST = '0.0.0.0'  # 
PORT = 8080
print("Bağlantı başarılı")
 
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
 
    s.bind((HOST, PORT))
    
    s.listen(5)
    print(f"Sunucu {HOST}:{PORT} üzerinde dinlemede...")

     
    while True:
      
        conn, addr = s.accept()
        print(f"Bağlantı alındı from {addr}")

        
        data = conn.recv(1024)
        if not data:
            break  

     
        print(f"Gelen veri: {data.decode()}")

 
        response = "HTTP/1.1 200 OK\n\nHello, client!"
        conn.sendall(response.encode())

     
        conn.close()
