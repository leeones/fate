#!/usr/bin/python
# -*- coding: utf-8 -*-

import smtplib
from email.header import Header
from email.mime.text import MIMEText
import sys
import time

#邮箱服务信息
mail_host = 'smtp.qq.com'
mail_port = '465'
mail_user = '********@qq.com'
mail_pass = '1234********'
mail_postfix = 'qq.com'

#邮件内容
def send_mail(to_list,subject,content):
    me = ("%s<***********@qq.com>")%(Header('丢你个扑街','utf-8'),)
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = subject + time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime())
    msg['From'] = me
    msg['to'] = to_list
    try:
        print('1')
        s = smtplib.SMTP_SSL(mail_host,mail_port)
        #s = a.connect(mail_host,587)
        #s.starttls()
        print('2')
        s.login(mail_user,mail_pass)
        print('3')
        s.sendmail(me,to_list,msg.as_string())
        s.close()
        return True
    except Exception,e:
        print str(e)
        return False
if __name__ == "__main__":
    send_mail(sys.argv[1], sys.argv[2], sys.argv[3])
