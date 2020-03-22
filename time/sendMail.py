#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/8 21:51
# @Author  : zqj
# coding: utf-8

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.header import Header
import sys


# 设置smtplib所需的参数
# 下面的发件人，收件人是用于邮件传输的。
smtpserver = 'smtp.163.com'
username = 'zqj16210240057@163.com'
password = '18516587127zqj'
sender = 'zqj16210240057@163.com'
# receiver='XXX@126.com'
# 收件人为多个收件人
receiver = ['471365897@qq.com<471365897@qq.com>']

subject = '定时发送任务'
# 通过Header对象编码的文本，包含utf-8编码信息和Base64编码信息。以下中文名测试ok
# subject = '中文标题'
# subject=Header(subject, 'utf-8').encode()

# 构造邮件对象MIMEMultipart对象
# 下面的主题，发件人，收件人，日期是显示在邮件页面上的。
msg = MIMEMultipart('mixed')
msg['Subject'] = subject
msg['From'] = 'zqj16210240057@163.com<zqj16210240057@163.com>'
# msg['To'] = 'XXX@126.com'
# 收件人为多个收件人,通过join将列表转换为以;为间隔的字符串
msg['To'] = ";".join(receiver)
# msg['Date']='2012-3-16'

# 构造文字内容
text = "Hi!\ncrontab定时发送任务\n现在时间是{t1}\n不是什么链接"
text_plain = MIMEText(text, 'plain', 'utf-8')
msg.attach(text_plain)

# 构造图片链接
#sendimagefile = open(r'D:\pythontest\testimage.png', 'rb').read()
#image = MIMEImage(sendimagefile)
#image.add_header('Content-ID', '<image1>')
#image["Content-Disposition"] = 'attachment; filename="testimage.png"'
#msg.attach(image)

# 构造html
# 发送正文中的图片:由于包含未被许可的信息，网易邮箱定义为垃圾邮件，报554 DT:SPM ：<p><img src="cid:image1"></p>
html = """
<html>  
  <head></head>  
  <body>  
    <p>Hi!<br>  
       How are you?<br>  
       Here is the <a href="123">link</a> you wanted.<br> 
    </p> 
  </body>  
</html>  
"""
text_html = MIMEText(html, 'html', 'utf-8')
text_html["Content-Disposition"] = 'attachment; filename="texthtml.html"'
msg.attach(text_html)

# 构造附件
#sendfile = open(r'D:\pythontest\1111.txt', 'rb').read()
#text_att = MIMEText(sendfile, 'base64', 'utf-8')
#text_att["Content-Type"] = 'application/octet-stream'
# 以下附件可以重命名成aaa.txt
# text_att["Content-Disposition"] = 'attachment; filename="aaa.txt"'
# 另一种实现方式
#text_att.add_header('Content-Disposition', 'attachment', filename='aaa.txt')
# 以下中文测试不ok
# text_att["Content-Disposition"] = u'attachment; filename="中文附件.txt"'.decode('utf-8')
#msg.attach(text_att)

import smtplib
from email.header import Header
from email.mime.text import MIMEText


smtpserver = 'smtp.163.com'
username = 'zqj16210240057@163.com'
password = '18516587127zqj'
sender = 'zqj16210240057@163.com'
# 第三方 SMTP 服务
mail_host = 'smtp.163.com' # SMTP服务器
mail_user = 'zqj16210240057@163.com' # 用户名
mail_pass = '18516587127zqj'  # 授权密码，非登录密码

sender = 'zqj16210240057@163.com'  # 发件人邮箱(最好写全, 不然会失败)
receivers = ['471365897@qq.com<471365897@qq.com>']
 # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

#content = "Hi!\ncrontab定时发送任务\n现在时间是'{t1}'\n不是什么链接".format(t1=dt)
#title = "发送邮件时间{t1}".format(t1=dt)  # 邮件主题


def sendEmail(dt):
    title = "发送邮件时间{t1}".format(t1=dt)  # 邮件主题
    content = "Hi!\ncrontab定时发送任务\n现在时间是'{t1}'\n不是什么链接".format(t1=dt)
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
    print(content)
    print(title)

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()


if __name__ == '__main__':
    dt=sys.argv[1]
    print(dt)
    sendEmail(dt)
