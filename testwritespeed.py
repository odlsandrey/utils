#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test python 3.8

Example dataset (file xaa):
20201222 080000 0640000;3673.5;3673.5;3673.75;1
20201222 080000 0640000;3673.5;3673.5;3673.75;4
20201222 080000 0640000;3673.5;3673.5;3673.75;3
20201222 080000 0680000;3673.5;3673.5;3673.75;2
20201222 080000 0680000;3673.5;3673.5;3673.75;5
20201222 080000 0680000;3673.5;3673.5;3673.75;6
"""




import time
from prettytable import PrettyTable

x = PrettyTable()

# dataset
fn = 'xaa'

# write file path
fn1 = 'fn1'
fn2 = 'fn2'
fn3 = 'fn3'

# Create heading
x.field_names = ["FName", "What is used", "Time (sec.)"]

def read(fn):
    arr = []
    with open(fn, 'r') as f:
        [arr.append(string.rstrip()) for string in f]
    return arr

# make list of lists
# [
# [20201222 080000 0640000],
# [3673.5],
# [3673.5],
# [3673.75],
# [1]
# ]
def mlist(arr):
    a, b, c, d, e = [], [], [], [], []
    for r in arr:
        new = r.split(';')
        a.append(new[0])
        b.append(new[1])
        c.append(new[2])
        d.append(new[3])
        e.append(new[4])
    # list of lists
    mlist = list(zip(a, b, c, d, e))
    return mlist

arr = read(fn)
mlist = mlist(arr)

# use format %s
def f1(mlist):
    stime = time.time()
    a = []
    for r in mlist:
        a.append('%s,%s,%s,%s,%s' % (r[4], r[3], r[2], r[1], r[0]))
    return (time.time() - stime)

x.add_row(['f1', 'create string use format "%s"', f1(mlist)])

# use "..."
def f2(mlist):
    stime = time.time()
    a = []
    for r in mlist:
        s = r[4] + ',' + r[3] + ',' + r[2] + ',' + r[1] + ',' + r[0]
        a.append(s)
    return (time.time() - stime)

x.add_row(['f2', 'create string use "..."', f2(mlist)])

# use function format()
def f3(mlist):
    stime = time.time()
    a = []
    for r in mlist:
        a.append('{0},{1},{2},{3},{4}'.format(r[4], r[3], r[2], r[1], r[0]))
    return (time.time() - stime)

x.add_row(['f3', 'create string use "function format"', f3(mlist)])

# use function print f
def f4(mlist):
    stime = time.time()
    a = []
    for r in mlist:
        a.append(f'{r[4]},{r[3]},{r[2]},{r[1]},{r[0]}')
    return (time.time() - stime)

x.add_row(['f4', 'create string use "function printf"', f4(mlist)])

# full lists
def f0(mlist):
    a = []
    for r in mlist:
        a.append(f'{r[4]},{r[3]},{r[2]},{r[1]},{r[0]}')
    return a

z=f0(mlist)

def w1(fn, arr):
    stime = time.time()
    with open(fn, 'w+') as file:
        file.writelines("%s\n" % l for l in arr)
    return (time.time() - stime)

x.add_row(['w1', 'Write list use "writelines"', w1(fn1, z)])

def w2(fn, arr):
    stime = time.time()
    with open(fn, 'w+') as file:
        print(*arr, file=file, sep='\n')
    return (time.time() - stime)

x.add_row(['w2', 'Write list use "print"', w2(fn2, z)])

def w3(fn, arr):
    stime = time.time()
    with open(fn, 'w+') as file:
        print(f'{arr}', file=file, sep='\n')
    return (time.time() - stime)

x.add_row(['w3', 'Write list use "printf"', w3(fn3, z)])

def w4(fn, arr):
    stime = time.time()
    with open(fn, 'w+') as file:
        for lines in arr:
            file.write(lines + '\n')
    return (time.time() - stime)

x.add_row(['w4', 'Write list use "write"', w3(fn3, z)])

print(x)


"""
Result:
+-------+-------------------------------------+---------------------+
| FName |             What is used            |     Time (sec.)     |
+-------+-------------------------------------+---------------------+
|   f1  |    create string use format "%s"    |  0.6461334228515625 |
|   f2  |       create string use "..."       |  0.8853142261505127 |
|   f3  | create string use "function format" |  0.8304479122161865 |
|   f4  | create string use "function printf" |  0.5112171173095703 |
|   w1  |     Write list use "writelines"     |  0.9371774196624756 |
|   w2  |        Write list use "print"       |  1.2561814785003662 |
|   w3  |       Write list use "printf"       | 0.44773173332214355 |
|   w4  |        Write list use "write"       |  1.639937400817871  |
+-------+-------------------------------------+---------------------+
"""














