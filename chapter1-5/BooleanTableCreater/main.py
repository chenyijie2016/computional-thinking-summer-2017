#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Time    : 2017/7/2 22:51
# Copyright (c) 2017  cyj <chenyijiethu@gmail.com>
# File    : main.py
import sys

Out = sys.stdout
Flush = sys.stdout.flush()

A = [False, True]


def main():
    Out.write('table = ')
    Out.write('{')
    Xor()
    Out.write('};\n')

    Out.write('F = BooleanFunction[table][x,y];\n')

    Out.write('BooleanConvert[F,"NAND"]\n')


def And():
    for x in A:
        for y in A:
            Out.write('{' + str(x) + ',' + str(y) + '}')
            Out.write('->')
            if not (x and y):
                Out.write(str(x and y) + ',')
            else:
                Out.write(str(x and y))
    Flush


def Or():
    for x in A:
        for y in A:
            Out.write('{' + str(x) + ',' + str(y) + '}')
            Out.write('->')
            if not (x and y):
                Out.write(str(x or y) + ',')
            else:
                Out.write(str(x or y))
    Flush


def Xor():
    for x in A:
        for y in A:
            Out.write('{' + str(x) + ',' + str(y) + '}')
            Out.write('->')
            if not (x and y):
                if x == y:
                    Out.write('False' + ',')
                else:
                    Out.write('True' + ',')
            else:
                if x == y:
                    Out.write('False')
                else:
                    Out.write('True')
    Flush


def Mux():
    for x in A:
        for y in A:
            for sel in A:
                Out.write('{' + str(x) + ',' + str(y) + ',' + str(sel) + '}')
                Out.write('->')
                if not (sel and x and y):
                    if not sel:
                        Out.write(str(x) + ',')
                    else:
                        Out.write(str(y) + ',')
                else:
                    if not sel:
                        Out.write(str(x))
                    else:
                        Out.write(str(y))
    Flush


if __name__ == '__main__':
    main()
