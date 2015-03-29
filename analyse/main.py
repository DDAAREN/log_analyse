#!/usr/bin/env python
#!_*_ coding:UTF-8 _*_

from analyse import *
from build_html import *

import smtplib, sys
from email.mime.text import MIMEText

a = Log('/home/y/var/log/fe3/201502/yongche-app-api_access_log-20150219.gz')
a.analys()

rt_table = Table('openapi accesslog analyse RTime on fe3(Date:20150219)',['RT','times','percent'])
for i in a.get_result('rt'):
    rt_table.add_row(i)


code_table = Table('openapi accesslog analyse Code on fe3(Date:20150219)',['Code','times','percent'])
for j in a.get_result('code'):
    code_table.add_row(j)

page = Page()
page.add_table(rt_table)
page.add_table(code_table)

page.print_page('/home/liulei/log/analyse/page.html')


mailto_list = ['liulei@yongche.com']
mail_host="smtp.yongche.com"
mail_user="noreply@yongche.com"
mail_pass="87fe556f31f24ddd2c05"
mail_postfix="yongche.com"

def send_mail(to_list, sub, content):
        me = "<"+mail_user+">"
        msg = MIMEText(content, _subtype='html', _charset='utf-8')
        msg['Subject'] = sub
        msg['From'] = me
        msg['To'] = ";".join(to_list)
        try:
                server = smtplib.SMTP()
                server.connect(mail_host)
                server.login(mail_user,mail_pass)
                server.sendmail(me, to_list, msg.as_string())
                server.close()
                return True
        except Exception, e:
                print str(e)
                return False


mail_text = ('')
with open('/home/liulei/log/analyse/page.html','r') as text:
    for line in text:
        mail_text += line

if send_mail(mailto_list, "test_0328", mail_text):
    print "发送成功"
else:
    print "发送失败"
