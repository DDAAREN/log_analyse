#!/usr/bin/env python
#!_*_ coding:UTF-8 _*_
import os
import gzip
import re
import sys
from collections import defaultdict


class Log(object):
    def __init__(self,path_list=['/root/log/fe1_openapi.tgz','/root/log/fe2_openapi.tgz','/root/log/fe3_openapi.tgz','/root/log/fe4_openapi.tgz','/root/log/fe5_openapi.tgz']):
        self.path_list=path_list
        self.a="0~50ms   ";
        self.b="50~150ms ";
        self.c="150~300ms";
        self.d=">300ms   ";
        self.count_code = defaultdict(int) #dict value的默认类型为int
        self.count_rt = defaultdict(int)
        self.count_line = 0

    def analys_group(self):
        for log in self.path_list :
            if os.path.exists(log): 
                with gzip.open(log, 'rb') as pf:
                    for line in pf:
                        self.count_line += 1
                        match = re.search(r' ([0-9]+) ([0-9]+|-) (\".*\") ([0-9]+) ', line)
                        if match is None:
                            print line
                            continue
                        code = str(match.group(1))
                        rt = int(match.group(4))
                        self.count_code[code] += 1 if code in self.count_code else 1
                        
                        if rt > 0 and rt <= 50000:
                            self.count_rt[self.a] += 1 if self.a in self.count_rt else 1
                        elif rt > 50000 and rt <= 150000:
                            self.count_rt[self.b] += 1 if self.b in self.count_rt else 1
                        elif rt > 150000 and rt <= 300000:
                            self.count_rt[self.c] += 1 if self.c in self.count_rt else 1
                        else:
                            self.count_rt[self.d] += 1 if self.d in self.count_rt else 1
            else:
                print('the log [{}] is not exist!'.format(path))

    def get_result(self, col):
        result = []
        if col == 'code':
            for key in self.count_code:
                percent = "%.4f" % (float(self.count_code[key])*100/self.count_line)
                result = result + [[key, str(self.count_code[key]), str(percent)+'%']]
            return result
        elif col == 'rt':
            for key in [self.a, self.b, self.c, self.d]:
                percent = "%.4f" % (float(self.count_rt[key])*100/self.count_line)
                result = result + [[key, str(self.count_rt[key]), str(percent)+'%']]
            return result
        
                
