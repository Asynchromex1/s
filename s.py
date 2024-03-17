import socket

# Sunucunun IP adresi ve port numarası
HOST = '0.0.0.0'  # Tüm ağ arayüzlerini dinle
PORT = 8080

# IPv4, TCP soketi oluştur
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Soketi belirtilen HOST ve PORT'a bağla
    s.bind((HOST, PORT))
    # Bağlantıları dinlemeye başla, en fazla 5 bağlantıyı kabul et
    s.listen(5)
    print(f"Sunucu {HOST}:{PORT} üzerinde dinlemede...")

    # Sonsuz döngüde bağlantıları kabul et
    while True:
        # İstemci bağlantısını kabul et
        conn, addr = s.accept()
        print(f"Bağlantı alındı from {addr}")

        # İstemciden gelen veriyi al
        data = conn.recv(1024)
        if not data:
            break  # Veri yoksa döngüden çık

        # Gelen veriyi ekrana yazdır
        print(f"Gelen veri: {data.decode()}")

        # İstemciye cevap gönder
        response = "HTTP/1.1 200 OK\n\nHello, client!"
        conn.sendall(response.encode())

        # Bağlantıyı kapat
        conn.close()
