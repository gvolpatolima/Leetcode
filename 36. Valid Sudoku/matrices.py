class Solution:
    def isValidSudoku(board: List[List[str]]) -> bool:
        
        
        rows = [0] * 9
        cols = [0] * 9
        squares = [0] * 9

        for row in range(len(board)):
            for col in range(len(board[0])):
                num = board[row][col]
                if num == ".":
                    continue
                square = row // 3 * 3 + col // 3

                bit = 1 << (int(num) - 1)
                if rows[row] & bit or cols[col] & bit or squares[square] & bit:
                    return False
                rows[row] |= bit
                cols[col] |= bit
                squares[square] |= bit
        return True

    boards = map(loads, stdin)
    f = open('user.out', 'w')
    for board in boards:
        result = isValidSudoku(board)
        print('true' if result else 'false', file=f)
