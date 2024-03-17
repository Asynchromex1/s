require 'socket'

# Sunucunun IP adresi ve port numarası
HOST = '0.0.0.0'  # Tüm ağ arayüzlerini dinle
PORT = 8080

# IPv4, TCP soketi oluştur
server = TCPServer.new(HOST, PORT)
puts "Sunucu #{HOST}:#{PORT} üzerinde dinlemede..."

# Sonsuz döngüde bağlantıları kabul et
loop do
  # İstemci bağlantısını kabul et
  client = server.accept
  addr = client.peeraddr[3]
  puts "Bağlantı alındı from #{addr}"

  # Ekrana eşek yazdır
  puts "Eşşek!"

  # İstemciye cevap gönder
  response = "HTTP/1.1 200 OK\n\nHello, client!"
  client.puts response

  # Bağlantıyı kapat
  client.close
end
