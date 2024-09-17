#!/usr/bin/env python

from operator import itemgetter
import sys

curkey = None
curkey_2 = None
total = 0
counter = 0
for line in sys.stdin:
    key, key_2, val, counter_temp = line.split("\t", 3)
    val = int(val)
    counter_temp = int(counter_temp)
    if key == curkey and key_2 == curkey_2:
        counter += counter_temp
        total += val
    else:
        if curkey is not None and curkey_2 is not None:
            print(curkey + "\t" + curkey_2 + "\t" + str(int(total) / counter))
        curkey = key
        curkey_2 = key_2
        total = val
        counter = counter_temp

print(curkey + "\t" + curkey_2 + "\t" + str(int(total) / counter))
