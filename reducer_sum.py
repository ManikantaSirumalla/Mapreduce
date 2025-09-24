#!/usr/bin/env python3
# DOB: 28-10-1999
import sys
cur=None; s=0
for line in sys.stdin:
    parts=line.rstrip("\n").split("\t",1)
    if len(parts)!=2: 
        continue
    k,v=parts
    try:
        n=int(v)
    except:
        continue
    if k==cur:
        s+=n
    else:
        if cur is not None:
            print(f"{cur}\t{s}")
        cur, s = k, n
if cur is not None:
    print(f"{cur}\t{s}")
