#!/usr/bin/env python
# _*_coding=utf-8_*_
import re,os,sys
from collections import defaultdict
from heapq import nlargest
from htmltable import table

#sys.stdout = open('python_output.txt','w+')

a="0~50ms   ";
b="50~150ms ";
c="150~300ms";
d=">300ms   ";


count_code = defaultdict(int) #dict value的默认类型为int
count_rt = defaultdict(int) 
count_line = 0


for line in sys.stdin:
    count_line += 1
    match = re.search(r' ([0-9]+) ([0-9]+|-) (\".*\") ([0-9]+) ', line)
    if match is None:
        print line
        continue
    code = match.group(1)
    rt = int(match.group(4))
    count_code[code] += 1 if code in count_code else 1
    if rt > 0 and rt <= 50000:
        count_rt[a] += 1 if a in count_rt else 1
    elif rt > 50000 and rt <= 150000:
        count_rt[b] += 1 if b in count_rt else 1
    elif rt > 150000 and rt <= 300000:
        count_rt[c] += 1 if c in count_rt else 1
    else:
        count_rt[d] += 1 if d in count_rt else 1
	
print '===============Code==================='
print "%-15s%-15s%-10s" % ("Code", "times", "percent")
for i in count_code:
    print "%-15s%-15s%.4f%%" % (str(i),str(count_code[i]),(count_code[i]*100.0/count_line))

print '================RT===================='
print "%-15s%-15s%-10s" % ("RT", "times", "percent")
for j in [a,b,c,d]:
    print "%-15s%-15s%.4f%%" % (str(j),str(count_rt[j]),(count_rt[j]*100.0/count_line))


sys.stdout = open('python_output.txt','w+')
print '<html>'
print '<body>'

code_table = table('Code',["Code", "times", "percent"])
for i in count_code:
    code_table.append_row([str(i),str(count_code[i]),(count_code[i]*100.0/count_line)])
code_table.print_table()

rt_table = table('RT',["RT", "times", "percent"])
for j in [a,b,c,d]:
    rt_table.append_row([str(j),str(count_rt[j]),(count_rt[j]*100.0/count_line)])
rt_table.print_table()

print '</body>'
print '</html>'
