import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import markdown2
import html2text

with open('data/data.txt','r',encoding='utf-8') as readfile:
    sendfile = readfile.read()

# 邮件配置
SMTP_SERVER = 'smtp.163.com'  # SMTP服务器地址
SMTP_PORT = 25  # SMTP服务器端口号
SMTP_USERNAME = 'abb1234aabb'  # 发件人用户名
SMTP_PASSWORD = 'PRKRDTZHOGVRDCBN'  # 发件人密码
SENDER_EMAIL = 'abb1234aabb@163.com'  # 发件人邮箱
RECIPIENT_EMAIL = '3469134108@qq.com'  # 收件人邮箱

def send_email(subject, markdown_content):
    # 将Markdown内容转换为HTML
    html_content = markdown2.markdown(markdown_content)

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = RECIPIENT_EMAIL
    msg['Subject'] = subject

    # 添加纯文本形式的邮件内容（可选）
    txt_content = html2text.html2text(html_content)
    msg.attach(MIMEText(txt_content, 'plain'))

    # 添加HTML形式的邮件内容
    msg.attach(MIMEText(html_content, 'html'))

    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SMTP_USERNAME, SMTP_PASSWORD)
        server.send_message(msg)
        server.quit()
        print("邮件发送成功")
    except Exception as e:
        print("邮件发送失败:", str(e))

# 发送邮件示例
subject = "信息"
markdown_content = sendfile

send_email(subject, markdown_content)
