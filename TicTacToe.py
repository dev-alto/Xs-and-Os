import pygame
from pygame import gfxdraw

surface = pygame.display.get_surface()
TILE_PADDING = 30

LIGHT_GRAY = (235, 235, 240)
WHITE = (255, 255, 255)

BLUE = (90, 115, 255)
RED = (255, 115, 90)

def draw_X(x, y, size):
    size -= TILE_PADDING * 2
    x += TILE_PADDING
    y += TILE_PADDING

    pygame.draw.line(surface, RED, (x, y), (x + size, y + size), 9)
    pygame.draw.line(surface, RED, (x, y + size), (x + size, y), 9)

def draw_O(x, y, radius):
    radius -= TILE_PADDING
    x += TILE_PADDING
    y += TILE_PADDING
    
    pygame.draw.circle(surface, BLUE, (x + radius, y + radius), radius, 7)
    gfxdraw.aacircle(surface, int(x + radius), int(y + radius), int(radius - 1), BLUE)

class TicTacToe:
    
    def __init__(self, x, y, size):
        self.board = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        
        self.board_size = size
        self.board_position = (x, y)
        self.winner = None

        self.tile_size = self.board_size / 3
        self.current_turn = 0

    def position_to_tile(self, x, y):

        # translate given position in reference to the board
        board_x = x - self.board_position[0]
        board_y = y - self.board_position[1]

        if board_x < 0 or board_y < 0 or board_x > self.board_size or board_y > self.board_size:
            return print('Position out-of-bounds')
        
        return (int(board_y // self.tile_size), int(board_x // self.tile_size))

    def play(self, row, col):
        if self.winner or self.board[row][col] != 0:
            return

        current_player = (self.current_turn % 2 == 1 and 1 or -1)
        self.current_turn += 1
        self.board[row][col] = current_player

        if self.current_turn > 4:
            win_patterns = [
                [self.board[0][0], self.board[0][1], self.board[0][2]], # row1
                [self.board[1][0], self.board[1][1], self.board[1][2]], # row2
                [self.board[2][0], self.board[2][1], self.board[2][2]], # row3
                [self.board[0][0], self.board[1][0], self.board[2][0]], # col1
                [self.board[0][1], self.board[1][1], self.board[2][1]], # col2
                [self.board[0][2], self.board[1][2], self.board[2][2]], # col3
                [self.board[0][0], self.board[1][1], self.board[2][2]], # cross1
                [self.board[0][2], self.board[1][1], self.board[2][0]]  # cross2
            ]
            for pattern in win_patterns:
                sum = 0
                for tile in pattern:
                    sum += tile

                if sum == 3:
                    print("X wins")
                    self.winner = 1
                elif sum == -3:
                    print("O wins")
                    self.winner = -1

    def render(self):
        for y in range(0, 3):
            row = self.board[y]
            for x in range(0, 3):
                tile = row[x]

                if tile == 1:
                    draw_X(x * self.tile_size + self.board_position[0], y * self.tile_size + self.board_position[1], self.tile_size)
                elif tile == -1:
                    draw_O(x * self.tile_size + self.board_position[0], y * self.tile_size + self.board_position[0], self.tile_size / 2)

        pygame.draw.line(surface, LIGHT_GRAY, (self.tile_size + self.board_position[0], 0 + self.board_position[1]), (self.tile_size + self.board_position[0], self.board_size + self.board_position[1]), 4)
        pygame.draw.line(surface, LIGHT_GRAY, ((self.tile_size * 2) + self.board_position[0], 0 + self.board_position[1]), ((self.tile_size * 2) + self.board_position[0], self.board_size + self.board_position[1]), 4)
        pygame.draw.line(surface, LIGHT_GRAY, (0 + self.board_position[0], self.tile_size + self.board_position[1]), (self.board_size + self.board_position[0], self.tile_size + self.board_position[1]), 4)
        pygame.draw.line(surface, LIGHT_GRAY, (0 + self.board_position[0], (self.tile_size * 2) + self.board_position[1]), (self.board_size + self.board_position[0], (self.tile_size * 2) + self.board_position[1]), 4)