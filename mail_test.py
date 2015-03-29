#!/usr/bin/env python
#_*_ coding=utf-8 _*_
import smtplib,sys
from email.mime.text import MIMEText

mailto_list = ['liulei@yongche.com']
mail_host="smtp.yongche.com"
mail_user="noreply@yongche.com"
mail_pass="87fe556f31f24ddd2c05"
mail_postfix="yongche.com"

def send_mail(to_list, sub, content):
	me = "<"+mail_user+">"
	msg = MIMEText(content, _subtype='plain', _charset='utf-8')
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

#if __name__ == '__main__':
#	if send_mail(mailto_list, "hello", "hello world! "):
#		print "发送成功"
#	else:
#		print "发送失败"
text = ('')
while True:
	line = sys.stdin.readline()
	if not line:
		break
	text += line
if __name__ == '__main__':
       if send_mail(mailto_list, "log_status", text):
               print "发送成功"
       else:
               print "发送失败"
