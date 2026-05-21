class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        # Trie Creation
        trie = {}

        for word in words:
            node = trie

            for ch in word:
                if ch not in node:
                    node[ch] = {}

                node = node[ch]

            node["word"] = word

        rows = len(board)
        cols = len(board[0])

        result = []

        # DFS Function
        def dfs(r, c, node):

            letter = board[r][c]

            # character not found
            if letter not in node:
                return

            next_node = node[letter]

            # word found
            if "word" in next_node:
                result.append(next_node["word"])

                # avoid duplicates
                del next_node["word"]

            # mark visited
            board[r][c] = "#"

            # 4 directions
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr, dc in directions:

                nr = r + dr
                nc = c + dc

                if 0 <= nr < rows and 0 <= nc < cols:

                    if board[nr][nc] != "#":
                        dfs(nr, nc, next_node)

            # backtrack
            board[r][c] = letter

        # Start DFS
        for i in range(rows):
            for j in range(cols):
                dfs(i, j, trie)

        return result