import pygame

surface = pygame.display.get_surface()
TILE_PADDING = 30

LIGHT_GRAY = (235, 235, 240)
WHITE = (255, 255, 255)

BLUE = (205, 205, 255)
RED = (255, 25, 25)

def draw_X(x, y, size):
    size -= TILE_PADDING * 2
    x += TILE_PADDING
    y += TILE_PADDING

    pygame.draw.line(surface, RED, (x, y), (x + size, y + size), 6)
    pygame.draw.line(surface, RED, (x, y + size), (x + size, y), 6)

def draw_O(x, y, radius):
    radius -= TILE_PADDING
    x += TILE_PADDING
    y += TILE_PADDING
    
    
    pygame.draw.circle(surface, BLUE, (x + radius, y + radius), radius, 6)
    pygame.transform.smoothscale(surface, (x/2, y/2))

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

    def pixelpos_to_tile(self, x, y):

        # translate given position in reference to the board
        board_x = x - self.board_position[0]
        board_y = y - self.board_position[1]

        if board_x < 0 or board_y < 0 or board_x > self.board_size or board_y > self.board_size:
            print('Position out-of-bounds')
            return
        
        return (int(board_y // self.tile_size), int(board_x // self.tile_size))

    def play(self, row, col):
        if self.winner or self.board[row][col] != 0:
            return

        current_player = (self.current_turn % 2 == 1 and 1 or -1)
        self.current_turn += 1
        self.board[row][col] = current_player

        if self.current_turn > 4: 
            row1 = self.board[0][0] + self.board[0][1] + self.board[0][2]
            row2 = self.board[1][0] + self.board[1][1] + self.board[1][2]
            row3 = self.board[2][0] + self.board[2][1] + self.board[2][2]
            col1 = self.board[0][0] + self.board[1][0] + self.board[2][0]
            col2 = self.board[0][1] + self.board[1][1] + self.board[2][1]
            col3 = self.board[0][2] + self.board[1][2] + self.board[2][2]
            cross1 = self.board[0][0] + self.board[1][1] + self.board[2][2]
            cross2 = self.board[0][2] + self.board[1][1] + self.board[2][0]

            if (row1 == 3 or row2 == 3 or row3 == 3 or col1 == 3 or col2 == 3 or col3 == 3 or cross1 == 3 or cross2 == 3):
                print('X win')
                self.winner = 1
            elif (row1 == -3 or row2 == -3 or row3 == -3 or col1 == -3 or col2 == -3 or col3 == -3 or cross1 == -3 or cross2 == -3):
                print("O win")
                self.winner = 2

    def render(self):
        for y in range(0, 3):
            row = self.board[y]
            for x in range(0, 3):
                tile = row[x]

                if tile == 1:
                    draw_X(x * self.tile_size, y * self.tile_size, self.tile_size)
                elif tile == -1:
                    draw_O(x * self.tile_size, y * self.tile_size, self.tile_size / 2)

        pygame.draw.line(surface, LIGHT_GRAY, (self.tile_size, 0), (self.tile_size, self.board_size), 4)
        pygame.draw.line(surface, LIGHT_GRAY, (self.tile_size * 2, 0), (self.tile_size * 2, self.board_size), 4)
        pygame.draw.line(surface, LIGHT_GRAY, (0, self.tile_size), (self.board_size, self.tile_size), 4)
        pygame.draw.line(surface, LIGHT_GRAY, (0, self.tile_size * 2), (self.board_size, self.tile_size * 2), 4)