#!/usr/bin/python
#-*-coding:utf8-*-


class binTree():
    def __init__(this, left = None, right = None, data = 0):
        if data == 0:
            this = None
        else:
            this.leftNode = left
            this.rightNode = right
            this.data = data

def creatBT():
    temp = input('Please input a number, input "0" for end!')
    if temp == 0:
        return None
    else:
        tree = binTree()
        tree.data = temp
        tree.leftNode = creatBT()
        tree.rightNode = creatBT()
        return tree


def viewAll(tree):
    if tree != None:
        print tree.data,
        viewAll(tree.leftNode)
        viewAll(tree.rightNode)

if __name__ == "__main__":
    root = creatBT()
    viewAll(root)