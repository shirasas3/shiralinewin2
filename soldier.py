import screen
def check_player_index():
    for x in range(100):
        screen.blit(background, position, position)  # erase
        position = soldier.move(2, 0)  # move player
        screen.blit(player, position)  # draw new player
        pygame.display.update()  # and show it all
        clock.tick(60)  # update 60 times per second

