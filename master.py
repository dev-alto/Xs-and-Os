import pygame

pygame.init()
screen = pygame.display.set_mode((805, 805))

from TicTacToe import TicTacToe

current_game = TicTacToe(0, 0, 240)
current_game2 = TicTacToe(405, 405, 350)
running = True

background_color = (55, 55, 60)

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pos = pygame.mouse.get_pos()
            tile = current_game.position_to_tile(mouse_pos[0], mouse_pos[1])
            if tile:
                current_game.play(tile[0], tile[1])
                current_game.render()
                if (current_game.current_turn % 2 == 1):
                    background_color = (55, 55, 70)
                else:
                    background_color = (65, 55, 60)

                if current_game.winner:
                    print("1: heard the news")

            tile2 = current_game2.position_to_tile(mouse_pos[0], mouse_pos[1])
            if tile2:
                current_game2.play(tile2[0], tile2[1])
                current_game2.render()
                if (current_game2.current_turn % 2 == 1):
                    background_color = (55, 55, 70)
                else:
                    background_color = (65, 55, 60)

                if current_game2.winner:
                    print("2: heard the news")

    screen.fill(background_color)
    pygame.transform.smoothscale(pygame.display.get_surface(), (400/2, 400/2))

    current_game.render()
    current_game2.render()
    pygame.display.update()

pygame.quit()