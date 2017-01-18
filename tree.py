#!/usr/bin/env python
# coding: utf-8

"""
@file: tree.py
@time: 2017/1/18 16:56
"""


class Node(object):
    def __init__(self):
        self.left = None
        self.right = None
        self.data = None


def list_pre(node):
    print node.data
    list_pre(node.left)
    list_pre(node.right)


def list_middle(node):
    list_middle(node.left)
    print node.data
    list_middle(node.right)

if __name__ == "__main__":
    node = Node()

