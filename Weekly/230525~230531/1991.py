import sys

nodes = int(sys.stdin.readline().strip()) # 몇개의 노드를 받을지
tree = {} # 트리를 dict형태로 받음.
 
for n in range(nodes): # 노드의 개수 만큼
    root, left, right = sys.stdin.readline().strip().split() # root, left, right 순으로 입력받음.
    tree[root] = [left, right] # root를 key로 받고 left와 right를 value로 list형태로 받음.


# 전위 순회 
def preorder(root):
    if root != '.': # root가 .이면 단말 노드이기 때문에 실행하지 않음
        print(root, end = '') # 루트노드 처리
        preorder(tree[root][0]) # 왼쪽 서브트리 처리
        preorder(tree[root][1]) # 오른쪽 서브트리 처리

# 중위 순회
def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end = '')
        inorder(tree[root][1])

# 후위 순회
def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end = '')


# 'A'가 제일 위에 있는 루트 노드이기에 A로 시작한다는 것.
preorder("A")
print()
inorder("A")
print()
postorder("A")
