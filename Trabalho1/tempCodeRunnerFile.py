
# def column(board, row, collumn):
#     for i in range(row, -1, -1):
#         if board[i][collumn] == 1:
#             return False
#     return True

# def diagonal(board, row, collumn):
#     for i, j in zip(range(row, -1,-1), range(collumn,-1,-1)):
#         if board[i][j] == 1:
#             return  False
#     for i, j in zip(range(row,-1,-1), range(collumn, n)):
#         if board[i][j] == 1: 
#             return False
#     return True

# def n_rainha(board, row):
#     if row == n:
#         return True
#     for  i in range(n):
#         if (column(board, row,i)== True and diagonal(board, row,i)== True):
#             board[row][i] == 1
#             if n_rainha(board, row + 1 ):
#                 return True
#             board [row][i] = 0

#     return False
# n_rainha(board, 0)

# for row in board:
#     print(row)