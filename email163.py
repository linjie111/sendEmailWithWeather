import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send(text):
    # 这里使用的是163.com
    mail_host = "smtp.163.com"  # 设置服务器
    mail_user = "*******@163.com"  # 用户名
    mail_pass = "******"  # 口令 邮箱密码

    sender = '*****@163.com'  #发送邮箱  和上方用户名一致
    receivers = ['***@163.com']  # 接收者的邮箱
    message = MIMEText(text, 'plain', 'utf-8')
    message['From'] = Header('wanglin')
    message['To'] = Header("toyou")

    subject = 'python send email'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        print(1)
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        print(2)
        smtpObj.login(mail_user, mail_pass)
        print(3)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
