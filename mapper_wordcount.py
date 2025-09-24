#!/usr/bin/env python3
# DOB: 28-10-1999
import sys, re
token_re = re.compile(r"[A-Za-z']+")
for line in sys.stdin:
    for t in token_re.findall(line):
        print(f"{t.lower()}\t1")
