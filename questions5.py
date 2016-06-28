####################################################################
####################################################################
####################################################################

from trees import getHeight
from trees import Tree
from trees import Node
from stacks import Stack
from queue import Queue

t1 = False
t2 = False
t3 = False
t4 = True

def ifBalanced(tree_root):
    if tree_root is None:
        return True
    heightDiff = abs(getHeight(tree_root.l) - getHeight(tree_root.r))
    if heightDiff > 1:
        return False
    else:
        return ifBalanced(tree_root.l) and ifBalanced(tree_root.r)

def heightAlt(tree_root):
    if tree_root is None:
        return 0
    leftHeight = heightAlt(tree_root.l)
    if leftHeight == -1:
        return -1
    rightHeight = heightAlt(tree_root.r)
    if rightHeight == -1:
        return -1
    height_diff = abs(rightHeight - leftHeight)
    if height_diff > 1:
        return -1
    else:
        return max(leftHeight, rightHeight) + 1

def isBalancedAlt(tree_node):
    if heightAlt(tree_node) == -1:
        return False
    return True

if t1:
    x = Tree()
    x.add(5)
    x.add(3)
    x.add(2)
    x.add(4)
    print isBalancedAlt(x.root)
    y = Tree()
    y.add(4)
    y.add(3)
    y.add(5)
    y.add(6)
    print isBalancedAlt(y.root)

def searchDFS(graph, start):
    visited = []
    stack = Stack()
    stack.push(start)
    while not stack.isEmpty():
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            print 'VERTEX', vertex
            for edges in graph[vertex]:
                stack.push(edges)
    return visited

def searchBFS(graph, start):
    visited = []
    queue = Queue()
    queue.enqueue(start)
    while not queue.isEmpty():
        current = queue.dequeue()
        if current not in visited:
            visited.append(current)
            for edges in graph[current]:
                queue.enqueue(edges)
    return visited

def searchDFSTrace(graph, start, end):
    stack = Stack()
    stack.push([start])
    while not stack.isEmpty():
        path = stack.pop()
        last = path[-1]
        if last == end:
            return path
        for adjacent in graph.get(last, []):
            new_path = list(path)
            new_path.append(adjacent)
            stack.push(new_path)

def searchBFSTrace(graph, start, end):
    queue = []
    queue.append([start])
    while queue:
        path = queue.pop(0)
        last = path[-1]
        if last == end:
            return path
        for adjacent in graph.get(last, []):
            new_path = list(path)
            new_path.append(adjacent)
            queue.append(new_path)


if t2:
    g1 = {
        'A': ['B', 'C', 'E'],
        'B': ['D', 'F', 'A'],
        'C': ['G', 'A'],
        'D': ['B'],
        'E': ['A','F'],
        'F': ['B'],
        'G': ['C']
    }
    g = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12']
        }
    # print searchDFSTrace(g, '1', '10')
    # print searchDFS(g1, 'A')
    # print searchBFS(g1, 'A')

def arrayToBST(arr, start, end):
    if end < start:
        return None
    mid = ( start + end )/ 2
    node = Node(arr[mid])
    node.l = arrayToBST(arr, start, mid-1)
    node.r = arrayToBST(arr, mid + 1, end)
    return node

def createArrayToBST(arr):
    return arrayToBST(arr, 0, (len(arr)- 1))

if t3:
    arr = [1,2,3]
    n = createArrayToBST(arr)
    print n.v
    print n.l.v
    print n.r.v

def ifBTisBST(tree_root, min, max):

    if tree_root.v <= tree_root.l.v and tree_root.v >= tree_root.r.v:
        return False
    ifBTisBST(tree_root.l)
    ifBTisBST(tree_root.r)
    return True
