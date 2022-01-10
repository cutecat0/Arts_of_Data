#!/usr/bin/env python3

import re
import sys

for line in sys.stdin:
    year, temp, q = line.strip().split()
    if temp != '9999' and re.match('[01459]', q):
        print('%s\t%s' % year, temp)


"""
    hive> ADD FILE /users/Gwendolynhai/Hadoop_Intro/hive.py;
    hive>from records2
        >select transform(year, temperature, quality)
        >using 'hive.py'
        >as year, temperature;
"""
