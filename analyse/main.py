#!/usr/bin/env python
#!_*_coding:UTF-8_*_

import datetime
from analyse import *
from build_html import *
from config import *
from mail import *


last_date = datetime.date.today() - datetime.timedelta(days=1)
last_d_month = last_date.strftime('%Y%m')
last_day = last_date.strftime('%Y%m%d')


def get_pro_host(project):
    count = 0
    for i in pro_dic:
        for j in pro_dic[i]:
            if j == project:
                count += 1
                return i
            else:
                continue
    if count == 0:
        print "no such project !"


def create_pro_table(project):
    h_group = get_pro_host(project) + '_group'
    pro_log_list = []
    for host in host_group[h_group]:
        log_path = log_file_root + host + '/' + last_d_month + '/' + str(project) + '_access_log-' + last_day + '.gz'
        pro_log_list.append(log_path)

    a = Log(pro_log_list)
    a.analys_group()
    table_title = 'Log analyse for ' + project + ': '
    pro_table = Table(table_title)
    pro_table.add_row(['RT', 'TIMES', 'PERCENT'])
    for i in a.get_result('rt'):
        pro_table.add_row(i)
    pro_table.add_row(['CODE', 'TIMES', 'PERCENT'])
    for j in a.get_result('code'):
        pro_table.add_row(j)
    
    return(pro_table)


# ==============创建表格和页面====================
page = Page()
for x in pro_dic:
    for y in pro_dic[x]:
        table = create_pro_table(y)
        page.add_table(table)
page.print_page(page_path)


# ==============以邮件方式发送=====================
mail_text = ('')
with open(page_path, 'r') as text:
    for line in text:
        mail_text += line

if send_mail(mailto_list, 'Log analyse on '+last_date.strftime('%Y-%m-%d'), mail_text):
    print "发送成功" + " " + datetime.date.today().strftime('%Y-%m-%d')
else:
    print "发送失败" + " " + datetime.date.today().strftime('%Y-%m-%d')
# =================================================
