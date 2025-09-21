# 전위순회: 노드 방문 → 왼쪽 자식 → 오른쪽 자식 (DFS 생각하기)
# 중위순회: 왼쪽 자식 → 노드 방문 → 오른쪽 자식
# 후위순회: 왼쪽 자식 → 오른쪽 자식 → 노드 방문 

import sys

n = int(sys.stdin.readline())
tree = {}

for i in range(n):
    parent, left, right = input().split()
    tree[parent] = (left, right)

# 전위순회
def preorder(node):
    if node == ".":
        return
    print(node, end='')
    preorder(tree[node][0])
    preorder(tree[node][1])
    
# 중위순회
def inorder(node):
    if node == ".":
        return
    inorder(tree[node][0])
    print(node, end='')
    inorder(tree[node][1])

# 후위순회
def postorder(node):
    if node == ".":
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')

