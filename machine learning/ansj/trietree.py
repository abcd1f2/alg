#coding=utf-8

class Node(object):
    def __init__(self,contents=None):
        self.contents_ = contents
        self.fre_ = -1
        self.is_root_ = False
        self.is_end_ = False
        self.childrens_ = {}
    def GetContents(self):
        return self.contents_
    def SetContents(self, contents):
        self.contents_ = contents
    def GetFre(self):
        return self.fre_
    def SetFre(self, fre):
        self.fre_ = fre
    def IsEnd(self):
        return self.is_end_;
    def SetIsEnd(self,flag):
        self.is_end_ = flag
    def IsRoot(self):
        return is_root_
    def SetIsRoot(self,flag):
        is_root_ = flag
    def GetChildrens(self):
        return self.childrens_

class TrieTree(object):
    def __init__(self):
        self.root_ = Node("root")
        self.root_.SetIsRoot(True)
        self.root_.SetFre(0)
        self.root_.SetIsEnd(False)
    def GetRootNode(self):
        return self.root_
    def Insert(self,contents):
        node = self.root_
        for i in xrange(len(contents)):
            if contents[i] in node.childrens_:
                if i == len(contents)-1:
                    t = node.childrens_[contents[i]]
                    t.SetIsEnd(True)
                    t.SetFre(t.GetFre()+1)
            else:
                t = Node()
                if i == len(contents) - 1:
                    t.SetFre(1)
                    t.SetIsEnd(True)
                else:
                    t.SetFre(0)
                node.childrens_[contents[i]] = t
            node = node.childrens_[contents[i]]

    def SearchFre(self, contents):
        node = self.root_
        for i in xrange(len(contents)):
            if contents[i] in node.childrens_:
                t = node.childrens_[contents[i]]
                if i == len(contents) - 1 and t.IsEnd():
                    return t.GetFre()
                node = node.childrens_[contents[i]]
        return -1


if __name__ == '__main__':
    tree = TrieTree()
    tree.Insert('tree1')
    tree.Insert('tree1')
    tree.Insert('tree2')
    tree.Insert('tree3')
    tree.Insert('tree4')
    tree.Insert('tree4')
    print tree.SearchFre('tree1')
    print tree.SearchFre('tre')
    print tree.SearchFre('tree4')
