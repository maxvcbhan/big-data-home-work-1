#!/usr/bin/env python

from operator import itemgetter
import sys

for line in sys.stdin:
    words = line.split(",")
    print(words[0] + "\t" + words[1] + "\t" + words[2][:-1] + "\t1")
