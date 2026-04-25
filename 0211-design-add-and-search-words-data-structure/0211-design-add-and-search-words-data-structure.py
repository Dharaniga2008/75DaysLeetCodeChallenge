class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node:
                node[ch] = {}
            node = node[ch]
        node["#"] = True   # end of word marker

    def search(self, word: str) -> bool:
        
        def dfs(node, i):
            if i == len(word):
                return "#" in node

            ch = word[i]

            # normal character
            if ch != '.':
                if ch not in node:
                    return False
                return dfs(node[ch], i + 1)

            # wildcard '.'
            for child in node:
                if child != "#" and dfs(node[child], i + 1):
                    return True

            return False

        return dfs(self.root, 0)


# Usage:
# obj = WordDictionary()
# obj.addWord("bad")
# print(obj.search("b.."))  # True