from typing import List


def exist(self, board: List[List[str]], word: str) -> bool:
    def _find_str(index, past_index, matrix, word):
        i, j = index
        row = len(board)
        col = len(board[0])
        if word[0] == board[i][j]:
            past_index.add((i, j))
            if not word[1:]:
                return True
        else:
            return False

        if i + 1 < row and (i + 1, j) not in past_index:
            find_one = _find_str((i + 1, j), past_index, matrix, word[1:])
            if find_one:
                return True
        if j + 1 < col and (i, j + 1) not in past_index:
            find_one = _find_str((i, j + 1), past_index, matrix, word[1:])
            if find_one:
                return True

        if i - 1 >= 0 and not (i - 1, j) in past_index:
            find_one = _find_str((i - 1, j), past_index, matrix, word[1:])
            if find_one:
                return True
        if j - 1 >= 0 and not (i, j - 1) in past_index:
            find_one = _find_str((i, j - 1), past_index, matrix, word[1:])
            if find_one:
                return True

        past_index.remove((i, j))
        return False

    for i in range(len(board)):
        for j in range(len(board[0])):
            if _find_str((i, j), set(), board, word):
                return True

    return False


print(exist(0, board=[["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]], word="ABCESEEEFS"))
