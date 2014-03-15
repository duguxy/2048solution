# -*- coding: utf-8 -*-
"""
Spyder Editor

This temporary script file is located here:
C:\Users\liu\.spyder2\.temp.py
"""

from random import *
import numpy as np
import msvcrt
import os

HELP='''q:quit
h:help
r:restart
ijkl:direction'''

trans={"left":[np.array],
       "right":[np.fliplr],
        "up":[np.transpose],
        "down":[np.transpose, np.fliplr]}

recvr={"left":[np.array],
       "right":[np.fliplr],
        "up":[np.transpose],
        "down":[np.fliplr, np.transpose]}

def merge(row, x):
    if row[-1]==0:
        row[-1]=x
    elif row[-1]==x:
        row[-1]=x*2
        row.append(0)
    else:
        row.append(x)
    return row

def fill(row):
    return row+[0]*(4-len(row))

def removeZeros(row):
    return filter(lambda x:x>0, row)

def moveRow(row):
    return fill(reduce(merge,removeZeros(row),[0]))
    
def moveLeft(cells):
    return map(moveRow, cells)

def move(cells, direct):
    cells2=reduce(lambda x,y:y(x), trans[direct]+[moveLeft]+recvr[direct], cells)
    if np.array_equal(cells, cells2):
        return False
    else:
        cells[:]=newCell(cells2)
        return True

def checkCells(cells):
    return [(i,j) for i in range(4) for j in range(4) if cells[i][j]==0]

def newValue():
    if random()<0.9:
        return 2
    else:
        return 4

def newCell(cells):
    availcells=[(i,j) for i in range(4) for j in range(4) if cells[i][j]==0]
    cells[availcells[randint(0,len(availcells)-1)]]=newValue()
    return cells

def printCell(cells):
    print "="*19
    for row in cells:
        print "%4d|%4d|%4d|%4d" % tuple(row.tolist())
    print "="*19

def initGame():
    os.system('cls')
    print "2048 game by duguxy@gmail.com"
    cells=np.zeros((4,4),dtype=int)
    newCell(cells)
    newCell(cells)
    printCell(cells)
    return cells

def main():
    keymap={"i":"up","j":"left","k":"down","l":"right"}
    cells=initGame()   
    while True:
        print 'Input direction (h for help): ',
        cmd=msvcrt.getch()
        print cmd
        if cmd=="q":
            break
        elif cmd=="h":
            print HELP
        elif cmd=="r":
            cells=initGame()
        elif cmd in keymap:
            os.system('cls')
            print "Move Direction:",
            direct=keymap[cmd]
            print direct
            move(cells, direct)
            printCell(cells)
            
def test():
    a=np.array([[2,2,4,0],
                [4,8,0,0],
                [0,2,4,0],
                [0,0,2,2]])
    printCell(trans["right"][0](a))
    #printCell(apply(trans["left"][0],a))
    b=move(a,"left")
    printCell(a)
    printCell(b)

if __name__=="__main__":
    main()
    #test()