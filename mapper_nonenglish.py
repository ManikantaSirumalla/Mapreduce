#!/usr/bin/env python3
# DOB: 28-10-1999
import sys, re
eng=set()
with open("words.txt","r",encoding="utf-8",errors="ignore") as f:
    for w in f:
        w=w.strip().lower()
        if w:
            eng.add(w)
token_re = re.compile(r"[A-Za-z']+")
for line in sys.stdin:
    for t in token_re.findall(line):
        w=t.lower()
        if w not in eng and len(w) > 1:
            print(f"{w}\t1")
