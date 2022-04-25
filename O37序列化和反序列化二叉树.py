from leetcode import *


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        from collections import deque
        if not root:
            return ''
        result = []
        queue = deque()
        queue.append(root)
        while queue or root:
            root = queue.popleft()
            if root:
                result.append(root.val)
                queue.extend([root.left, root.right])
            else:
                result.append(None)

        return str(result).strip('[]')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None

        data = data.split(',')
        data = [eval(i) for i in data]
        return self.build_tree(data)

    def build_tree(self, val_list):
        if not val_list:
            return None
        root = []
        for item in val_list:
            if item == None:
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


c = Codec()
tree = build_tree([1, 2, 3, null, null, 4, 5])
tree=c.deserialize(c.serialize(tree))
tree

