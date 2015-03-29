#!/usr/bin/env python
# _*_coding=utf-8_*_
import re
from collections import defaultdict
from heapq import nlargest

with open('test.log') as f:
    count = defaultdict(int) #dict value的默认类型为int
    for line in f:
        match = re.search(r' "\w+ (.*?) HTTP/', line)
        if match is None:
            continue
        uri = match.group(1).split('?')[0] #只取？前的部分
        count[uri] = count[uri] + 1 if uri in count else 1 #条件赋值

most_common = nlargest(5, count.items(), key=lambda x: x[1])  #nlargest(获取满足条件的最N个值,对象迭代器,排序指标[方法])
print most_common					      #.items()：返回键值对的数组
