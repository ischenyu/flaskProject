import socket,time

target_ip = '192.168.1.9'
target_port = 8080
jieshou_ip = '0.0.0.0'
jieshou_port= 1145

def jieshou():
    sock.listen(1)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        print('等待连接...')
        # 等待客户端连接
        client_socket, client_address = sock.accept()
        print('新连接：', client_address)

        try:
            while True:
                # 接收数据
                data = client_socket.recv(1024)
                if not data:
                    # 如果数据为空，则表示连接已关闭
                    print('连接已关闭')
                    break
                # 处理接收到的数据
                print(f'接收到的数据：{data.decode()}')
                time.sleep('0.5')
                return data
        except KeyError:
            exit(e)

import json
def send(miao, deng):
    send_miao = miao
    send_deng = deng
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 构造要发送的消息
    message = json.dumps({'seconds': send_miao, 'led': send_deng})
    try:
        # 发送消息给目标地址
        sock.sendto(message.encode(), (target_ip, target_port))
        print("Message sent successfully.")
    except socket.error as e:
        print("Error occurred while sending message:", e)
    # 关闭 Socket 连接
    sock.close()
