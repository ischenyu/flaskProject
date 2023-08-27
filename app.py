from flask import Flask, render_template, request
import markdown2, json, datetime
import urllib.parse,threading


app = Flask(__name__)
history = []

@app.route('/')
def home():
    with open('data/data.txt', 'r', encoding='utf-8') as readfile:
        ggfile = readfile.read()
    html_content = markdown2.markdown(ggfile)
    return render_template('index.html', iw66k_data=html_content)

@app.route('/process', methods=['POST'])
def process():
    text = request.form['text']  # 获取前端发送的数据
    # 构建一个包含序号、日期时间和内容的字典
    data = {
        'number': len(history) + 1,
        'datetime': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'word': text
    }
    # 将字典添加到历史记录中
    history.append(data)

    # 将历史记录写入到 history.json 文件
    with open('data/history.json', 'w', encoding='utf-8') as file:
        json.dump(history, file, ensure_ascii=False, indent=4)
    # 返回处理完毕的响应给前端
    return "处理完毕！"

@app.route('/history')
def show_history():
    # 读取已有的历史记录
    with open('data/history.json', 'r', encoding='utf-8') as file:
        history = json.load(file)
    return render_template('history.html', history=history)

@app.route('/index.css')
def css():
    return render_template('index.css')

@app.route('/add')
def add_gg():
    with open('data/data.txt', 'r', encoding='utf-8') as readfile:
        info = readfile.read()
    return render_template('add_gg.html',ggfile = info)

@app.route('/returngg', methods=['POST','GET'])
def jsgg():
    text = request.form['text']
    decoded_text = urllib.parse.unquote(text)
    with open('data/data.txt','w',encoding = 'utf-8') as gg :
        gg.write(decoded_text)
    import send_email
    return '收到数据：' + decoded_text

@app.route('/hld', methods=['GET'])
def hld():
    red_light = "gray"
    yellow_light = "gray"
    green_light = "gray"
    return render_template('hld.html', red_light=red_light, yellow_light=yellow_light, green_light=green_light)

@app.route('/addhld', methods=['POST'])
@app.route('/addhld', methods=['POST'])
def add_hld():
    import hld
    try:
        seconds = int(request.form["seconds"])
        color = request.form["color"]
        if color == "red":
            red_light = "red"
            yellow_light = "gray"
            green_light = "gray"
        elif color == "yellow":
            red_light = "gray"
            yellow_light = "yellow"
            green_light = "gray"
        else:  # color is "green"
            red_light = "gray"
            yellow_light = "gray"
            green_light = "green"
        hld.send(seconds, color)  # 将参数传递给send函数
        return render_template('hld.html', red_light=red_light, yellow_light=yellow_light, green_light=green_light)
    except ValueError:
        pass



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=2233)