# !/usr/bin/python
# -*- coding: UTF-8 -*-

my_sender = '1019177406@qq.com'  # 发件人邮箱账号
my_pass = 'fswuvoapwowfbgai'  # 发件人邮箱密码
my_user = '1019177406@qq.com'  # 收件人邮箱账号，我这边发送给自己
import smtplib
from email.mime.text import MIMEText
_user = "1019177406@qq.com"
_pwd  = "fswuvoapwowfbgai"
_to   = "1019177406@qq.com"

msg = MIMEText("Test")
msg["Subject"] = "don't panic"
msg["From"]    = _user
msg["To"]      = _to

try:
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print "Success!"
except smtplib.SMTPException,e:
    print "Falied,%s"%e