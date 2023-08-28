from time import sleep
import tm1637
import _thread
from machine import Pin
from neopixel import NeoPixel
import socket
import ujson, network

# 定义RGB控制对象
pin = 15
rgb_num = 1
rgb_led = NeoPixel(Pin(pin, Pin.OUT), rgb_num)

# 定义RGB颜色
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 155, 0)
COLORS = [RED, GREEN, YELLOW]

smg = tm1637.TM1637(clk=Pin(17), dio=Pin(16))


def show_single_color(color, duration):
    for i in range(rgb_num):
        rgb_led[i] = color
    rgb_led.write()

    for i in range(duration, 0, -1):
        smg.show("%04d" % i)
        sleep(1)


def set_color(color):
    for i in range(rgb_num):
        rgb_led[i] = color
    rgb_led.write()


def traffic_light(seconds, led_color):
    if led_color == 'red':
        show_single_color(RED, seconds)
    elif led_color == 'green':
        show_single_color(GREEN, seconds)
    elif led_color == 'yellow':
        show_single_color(YELLOW, seconds)
    else:
        print('无效的颜色')


def receive_and_parse():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', 8080))

    while True:
        print('等待连接...')
        # 接收数据
        data, addr = sock.recvfrom(1024)
        print('收到数据:', data)

        try:
            # 解析JSON数据
            parsed_data = ujson.loads(data.decode())

            # 获取解析后的数据
            seconds = parsed_data.get('seconds')
            led_color = parsed_data.get('led')

            # 控制红绿灯
            traffic_light(seconds, led_color)

        except ValueError:
            print('无效的JSON数据')

        except KeyError:
            print('缺少关键字')


# 执行数据接收和控制函数
def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        # wlan.ifconfig(('192.168.1.9', '255.255.255.0', '192.168.1.2', '192.168.1.2'))
        wlan.connect('ChinaNet-PEs9', '13789569653')
        # wlan.connect('AP', '1234561017')
        i = 1
        led.value(1)
        while not wlan.isconnected():
            print("正在链接...{}".format(i))
            led.value(1)
            i += 1
            time.sleep(1)
            led.value(0)
    print('network config:', wlan.ifconfig())


do_connect()
receive_and_parse()

