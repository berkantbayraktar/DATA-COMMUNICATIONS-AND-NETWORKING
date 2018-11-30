#!/usr/bin/env python
# -*- coding: utf-8 -*- 

f1 = open("demofile.txt","r")
mes = f1.readlines
f = open("output.txt", "w+")
for line in f1:
    f.write(line)