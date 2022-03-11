from collections import deque

null = None


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.val}'


def build_tree(val_list):
    if not val_list:
        return None
    root = []
    for item in val_list:
        if item==None:
            root.append(item)
        else:
            root.append(TreeNode(item))

    head = root[0]
    root = root[::-1]
    queue = deque()
    queue.append(root.pop())
    while root:
        item = queue.popleft()
        left = root.pop()
        item.left = left
        right = root.pop()
        item.right = right
        if left:
            queue.append(left)
        if right:
            queue.append(right)

    return head



