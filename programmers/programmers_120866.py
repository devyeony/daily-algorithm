# https://school.programmers.co.kr/learn/courses/30/lessons/120866
from typing import List


def solution(board):
    dangerous_area_count = 0
    side_length = len(board)
    for i in range(0, side_length):
        for j in range(0, side_length):
            if board[i][j] == 1:
                board[i][j] = -1
                if 0 <= i - 1:
                    board[i - 1][j] = (-1 if board[i - 1][j] != 1 else 1)
                    if 0 <= j - 1:
                        board[i - 1][j - 1] = (-1 if board[i - 1][j - 1] != 1 else 1)
                    if j + 1 < side_length:
                        board[i - 1][j + 1] = (-1 if board[i - 1][j + 1] != 1 else 1)
                if i + 1 < side_length:
                    board[i + 1][j] = (-1 if board[i + 1][j] != 1 else 1)
                    if 0 <= j - 1:
                        board[i + 1][j - 1] = (-1 if board[i + 1][j - 1] != 1 else 1)
                    if j + 1 < side_length:
                        board[i + 1][j + 1] = (-1 if board[i + 1][j + 1] != 1 else 1)
                if 0 <= j - 1:
                    board[i][j - 1] = (-1 if board[i][j - 1] != 1 else 1)
                if j + 1 < side_length:
                    board[i][j + 1] = (-1 if board[i][j + 1] != 1 else 1)

    for i in range(0, side_length):
        dangerous_area_count += board[i].count(-1)

    return side_length * side_length - dangerous_area_count


board1: List[List[int]] = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
board2: List[List[int]] = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 1, 0], [0, 0, 0, 0, 0]]
board3: List[List[int]] = [[1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1]]
print(solution(board1))
print(solution(board2))
print(solution(board3))
