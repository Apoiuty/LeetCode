class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        if node.neighbors is []:
            return Node(val=node.val)
        stack = [node]
        visited = set()
        while stack:
            tmp = stack.pop()
            if tmp not in visited:
                stack.extend(tmp.neighbors)
                visited.add(tmp)
                tmp.copy = Node(val=tmp.val)

        stack = [node]
        visited.clear()
        while stack:
            item = stack.pop()
            if item not in visited:
                visited.add(item)
                for neighbor in item.neighbors:
                    item.copy.neighbors.append(neighbor.copy)
                stack.extend(item.neighbors)

        return node.copy
