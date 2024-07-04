class Solution:
    def isValidSudoku(board) -> bool:    
        for i in board:
            memory_row = []
            for j in range(0,9):
                if i[j] != ".":
                    if i[j] not in memory_row:
                        memory_row.append(i[j])
                    else: return False
        
        for k in range(0,9):
            memory_column = []
            for l in board:
                if l[k] != ".":
                    if l[k] not in memory_column:
                        memory_column.append(l[k])
                    else: return False
        
        for z in (0,3,6):
            for zi in (0,3,6):
                memory_box = []
                for w in range(z, z+3):
                    for y in range(zi, zi+3):  
                        if board[y][w] != ".":
                            if board[y][w] not in memory_box:
                                memory_box.append(board[y][w])
                            else: return False

        return True