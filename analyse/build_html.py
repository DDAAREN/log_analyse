#!/usr/bin/env python
#! _*_ coding:UTF-8 _*_
import sys


class Html(object):
    def print_head(self):
        print '''
<html>
<body>
'''
    def print_tail(self):
        print '''
</body>
</html>
'''

class Table(Html):
    def __init__(self, table_name):
        self.table_name = table_name
        self.text = []
        #self.text = head1

    def add_row(self, data=['']):
        self.text.append(data[:])

    def print_table(self):
        print '<h4>'+self.table_name+'</h4>'
        print '<table border="1">'
        for contact in self.text:
            if contact[1] == 'TIMES':
                print '    <tr bgcolor=#6A5ACD>'
            else:
                print '    <tr>'
        # print '    <tr bgcolor=#6A5ACD>'
            for column in contact:
                print "        <td width=\"100\">"+str(column)+"</td>"
            print '    </tr>'
        print '''</table>'''


class Page(Html):
    def __init__(self):
        self.table_list = []

    def add_table(self, table):
        # self.table_list += table
        self.table_list.append(table)

    def print_page(self, path='/tmp/.page.html'):
        __stdout = sys.stdout
        sys.stdout = open(path,'w+')
        self.print_head()
        for a in self.table_list:
            a.print_table()
        self.print_tail() 
        sys.stdout = __stdout



#a = Table('第一张表',['第一列','第二列','第三列'])
#a.add_row(['1x1','1x2','1x3'])
#a.add_row(['2x1','2x2','2x3'])
#a.add_row(['3x1','3x2','3x3'])
#
#b = Table('第二张表',['第一列','第二列','第三列'])
#b.add_row(['1x1','1x2','1x3'])
#b.add_row(['2x1','2x2','2x3'])
#b.add_row(['3x1','3x2','3x3'])
#
#page = Page()
#page.add_table(a)
#page.add_table(b)
#page.print_page()
