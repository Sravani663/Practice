from __future__ import print_function

class pointsList(object):
    def __init__(self):
        self.List = {}

    def addPoint(self, start, end):
        
        if start in self.List.keys():
            self.List[start].append(end)
        else:
            self.List[start] = [end]

    def printList(self):
        for i  in self.List:
            print((i,'->',' -> '.join([str(j) for j in self.List[i]])))

if __name__ == '__main__':
    lst = pointsList()
    lst.addPoint(0, 5)
    
    lst.addPoint(0, 5)
    lst.addPoint(4, 1)
    lst.addPoint(2, 3)
    lst.addPoint(2, 0)
    lst.addPoint(2, 4)
    
    lst.printList()
    
