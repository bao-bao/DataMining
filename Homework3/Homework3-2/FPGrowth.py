"""
    A sample for FP-growth algorithm
    ===============================================================    
    :param:
    *** dataset: dictionary of transactions     eg: {name: list(items, ...), ...}
    *** minSupport: minimum support number rather than percentage
    
    :return:
    *** freqItems: frequent itemsets in dataset restricted by minSupport
"""


class treeNode:
    def __init__(self, name, num, parent):
        self.name = name
        self.count = num
        self.nextnode = None
        self.parent = parent
        self.children = {}

    def increase(self, num):
        self.count += num

    def display(self, ind=1):
        print ' ' * ind, self.name, ' ', self.count
        for child in self.children.values():
            child.display(ind + 1)


"""
    Building a FPTree
"""


def createTree(dataSet, minSup=1):
    # first traversal, get headerTable
    headerTable = {}
    for key, value in dataSet.items():
        for item in key:
            headerTable[item] = headerTable.get(item, 0) + value

    for k in headerTable.keys():
        if headerTable[k] < minSup:
            del (headerTable[k])

    freqItemSet = set(headerTable.keys())
    if len(freqItemSet) == 0:
        return None, None

    # second traversal, get FP-Tree
    for k in headerTable:
        headerTable[k] = [headerTable[k], None]

    retTree = treeNode('Root', 1, None)
    for key, value in dataSet.items():
        localD = {}
        for item in key:
            if item in freqItemSet:
                localD[item] = headerTable[item][0]
        if len(localD) > 0:
            orderedItems = [v[0] for v in sorted(localD.items(), key=lambda p: p[1], reverse=True)]
            updateTree(orderedItems, retTree, headerTable, value)

    return retTree, headerTable


def updateTree(items, inTree, headerTable, count):
    if items[0] in inTree.children:
        inTree.children[items[0]].increase(count)
    else:
        inTree.children[items[0]] = treeNode(items[0], count, inTree)
        if headerTable[items[0]][1] is None:
            headerTable[items[0]][1] = inTree.children[items[0]]
        else:
            updateHeader(headerTable[items[0]][1], inTree.children[items[0]])

    if len(items) > 1:
        updateTree(items[1::], inTree.children[items[0]], headerTable, count)


def updateHeader(node, target):
    while node.nextnode is not None:
        node = node.nextnode
    node.nextnode = target


def createInitSet(dataSet):
    Dict = dict()
    for key, value in dataSet.items():
        reduced = set(value)
        Dict[frozenset(reduced)] = 1
    return Dict


"""
    Mining in FPTree
"""


def findPrefixPath(headerTable, basePat):
    condPats = {}
    node = headerTable[basePat][1]
    while node is not None:
        prefixPath = []
        ascendTree(node, prefixPath)
        if len(prefixPath) > 1:
            condPats[frozenset(prefixPath[1:])] = node.count
        node = node.nextnode
    return condPats


def ascendTree(leaf, prefixPath):
    if leaf.parent is not None:
        prefixPath.append(leaf.name)
        ascendTree(leaf.parent, prefixPath)


def mineTree(inTree, headerTable, minSup, preFix, freqItemList):
    bigL = [v[0] for v in sorted(headerTable.items(), key=lambda p: p[1])]
    for basePat in bigL:
        newFreqSet = preFix.copy()
        newFreqSet.add(basePat)
        freqItemList.append(newFreqSet)
        condPattBases = findPrefixPath(headerTable, basePat)
        condTree, head = createTree(condPattBases, minSup)

        if head is not None:
            # print 'conditional tree for:', newFreqSet
            # condTree.display()
            mineTree(condTree, head, minSup, newFreqSet, freqItemList)


def FPgrowth(dataSet, minsupport=1):
    print "FPGrowth Running..."
    FPtree, HeaderTable = createTree(createInitSet(dataSet), minsupport)
    freqItems = []
    mineTree(FPtree, HeaderTable, minsupport, set([]), freqItems)
    return freqItems

if __name__ == '__main__':
    simpDat = {100: ['r', 'z', 'h', 'j', 'p'],
               200: ['z', 'y', 'x', 'w', 'v', 'u', 't', 's'],
               300: ['z'],
               400: ['r', 'x', 'n', 'o', 's'],
               500: ['y', 'r', 'x', 'z', 'q', 't', 'p'],
               600: ['y', 'z', 'x', 'e', 'q', 's', 't', 'm']}
    # FPtree, HeaderTable = createTree(createInitSet(TestData.gettest()), 2)
    # FPtree, HeaderTable = createTree(createInitSet(simpDat), 3)
    # freqItems = []
    # mineTree(FPtree, HeaderTable, 2, set([]), freqItems)
    # print freqItems
