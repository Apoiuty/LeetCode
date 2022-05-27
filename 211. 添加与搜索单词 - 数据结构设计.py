class TierTree:
    def __init__(self):
        self.root = Node()
        self.cnt = 0

    def get_string(self, node, s, d):
        """
        :param node: 节点
        :param s: 字符串
        :param d: 匹配的长度
        :return:
        """
        if node == None:
            return
        elif len(s) == d:
            return node
        else:
            char = s[d]
            return self.get_string(node.next[char], s, d + 1)

    def get(self, s):
        """
        返回是否有字符串
        :param s:
        :return:
        """
        node = self.get_string(self.root, s, 0)
        if node == None:
            return None
        else:
            return node.val

    def put_string(self, node, s, d):
        """
        将字符串插入树中
        :param node:
        :param s:
        :param d:
        :return:
        """
        if node == None:
            node = Node()
        if d == len(s):
            node.val = s
            return node
        else:
            char = s[d]
            node.next[char] = self.put_string(node.next[char], s, d + 1)
            return node

    def put(self, s):
        self.root = self.put_string(self.root, s, 0)

    def puts(self, l):
        """
        列表装填
        :param l:
        :return:
        """
        for item in l:
            self.put(item)

    def prefix_with(self, s):
        '''
        返回以s为前缀的字符
        :param s:
        :return:
        '''
        queue = []
        self.collect(self.get_string(self.root, s, 0), s, queue)
        return queue

    def collect_pattern(self, node, pre, pattern, queue):
        if not node:
            return
        n = len(pre)
        if n == len(pattern) and node.val:
            queue.append(node.val)
        if n == len(pattern):
            return
        char = pattern[n]
        for key in node.next:
            if char == key or char == '.':
                self.collect_pattern(node.next[key], pre + key, pattern, queue)

    def match(self, s):
        queue = []
        self.collect_pattern(self.root, '', s, queue)
        return queue

    def collect(self, node, pre, queue):
        """
        收集一棵单词查找树中所有键
        :param node:
        :param pre:
        :param queue:
        :return:
        """
        if node == None:
            return
        if node.val:
            queue.append(pre)
        for key in node.next:
            self.collect(node.next[key], pre + key, queue)

    def delete(self, s):
        self.root = self.__delete(self.root, s, 0)

    def long_prefix(self, s):
        return self.__long_prefix(self.root, s, 0, '')

    def __long_prefix(self, node, s, d, pre):
        if node == None:
            return pre
        if node.val == s[:d]:
            pre = node.val
        if d < len(s):
            return self.__long_prefix(node.next[s[d]], s, d + 1, pre)
        else:
            return pre

    def __delete(self, node, s, d):
        if node is None:
            return None
        if d == len(s):
            node.val = None
        else:
            node.next[s[d]] = self.__delete(node.next[s[d]], s, d + 1)

        if node.val:
            return node
        else:
            if any(node.next[c] for c in node.next):
                return node
            else:
                return None


class WordDictionary:

    def __init__(self):
        self.tree = TierTree()
        self.words = set()

    def addWord(self, word: str) -> None:
        self.tree.put(word)
        self.words.add(word)

    def search(self, word: str) -> bool:
        if '.' not in word:
            return word in self.words
        return bool(self.tree.match(word))


s = WordDictionary()
s.addWord('bad')
s.addWord('dad')
s.addWord('mad')
print(s.search())
