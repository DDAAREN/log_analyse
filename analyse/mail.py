#!/bin/usr/env python
import smtplib
from email.mime.text import MIMEText

__author__ = 'pt'

mailto_list = ['787351047@qq.com']
mail_host = "smtp.163.com"
mail_user = "ddaaren@163.com"
mail_pass = ""
mail_postfix = "163.com"


def send_mail(to_list, sub, content):
        me = "<"+mail_user+">"
        msg = MIMEText(content, _subtype='html', _charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
                server = smtplib.SMTP()
                server.connect(mail_host)
                server.login(mail_user, mail_pass)
                server.sendmail(me, to_list, msg.as_string())
                server.close()
                return True
        except Exception, e:
                print str(e)
                return False