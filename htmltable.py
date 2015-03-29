#!/usr/bin/env python
#!_*_ coding:UTF-8 _*_

class table(object):
    def __init__(self, table_name, head=['']):
        self.table_name = table_name
        self.text = [head]

    def append_row(self, data=['']):
        self.text.append(data)

    def print_table(self):
        print '<h4>'+self.table_name+'</h4>'
        print '<table border="1">'
        for contact in self.text:
            print '    <tr>'
            for column in contact:
                print "        <td>"+str(column)+"</td>"
            print '    </tr>'
        print '''</table>'''

    def print_test(self):
        print self.table_name
        print self.text

class page(object):
    def __init__(self):
        pass

    def insert_table(self,tablelist=[]):
        pass
    
    def print_page(self):
        pass
