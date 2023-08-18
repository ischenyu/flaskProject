import socket

# 目标地址和端口
target_ip = '192.168.1.9'
target_port = 8080

# 创建 UDP Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 发送的消息
message = 'light on'

try:
    # 发送消息给目标地址
    sock.sendto(message.encode(), (target_ip, target_port))
    print("Message sent successfully.")
except socket.error as e:
    print("Error occurred while sending message:", e)

# 关闭 Socket 连接
sock.close()